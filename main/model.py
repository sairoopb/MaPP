# =========================================================
#   Model is only available for Goldman Sachs Data and
#   will be updated for other companies soon after testing.
# =========================================================

# ==========================================================
#   Data coming from load data should be permuted since 
#   it is batch first for all numerical fields using permute
# ==========================================================

import torch
import torch.nn as nn
import time

from models.encoder import StockEncoder, NewsEncoder
from models.predictor import OutputRegressor
from models.stock import StockModel

from traintest.functions import learnParamter, predict
from loadData import Dataloader

from visualization.view import showResults, showTrain

BATCHSIZE = 16
EMBEDDING = 200
HIDDEN = 64
DROPOUT = 0.1
S_INPUT = 23
R_INPUT = 4
L2CONSTANT = 100
EPOCHS = 1000
PRETRAINED = False

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data = Dataloader()
train, val, test, length = data.get_iterator(BATCHSIZE)

newsEnc = NewsEncoder(length, EMBEDDING, HIDDEN, DROPOUT) 
stockEnc = StockEncoder(S_INPUT, HIDDEN)
outRegressor = OutputRegressor(R_INPUT, HIDDEN)

stockPredictor = StockModel(newsEnc, stockEnc, outRegressor, device).to(device)

optimizer = torch.optim.Adam(stockPredictor.parameters(), weight_decay=L2CONSTANT)
criterion = nn.MSELoss()

train_start = time.time()
trainer = learnParamter(stockPredictor, criterion, optimizer, PRETRAINED)
train_loss, val_loss = trainer.train(train, val, EPOCHS)
train_end = time.time()

trainTime = (train_end - train_start)
print(f'\n Total training time ==> [{time.strftime("%H:%M:%S",time.gmtime(trainTime))}] \n')

tester = predict(stockPredictor, criterion, PRETRAINED)
test_loss, results = tester.infer(test)

print(f'Test Loss ==> [{test_loss:5.3f}]\n')

trainShow = showTrain(train_loss, val_loss, EPOCHS)
resultShow = showResults(results)

trainShow.plotSave()
resultShow.plotSave()