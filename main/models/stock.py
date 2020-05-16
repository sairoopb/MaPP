# This model is just used to encompass all the other models

import torch
import torch.nn as nn

MAXLEN = 10

class StockModel(nn.Module):
    
    def __init__(self, newsEncoder, stockEncoder, outputRegressor, device):
        
        super().__init__()
        
        self.news = newsEncoder
        self.stock = stockEncoder
        self.outRegressor = outputRegressor
        self.device = device

    def forward(self, review, in_hidden, final, targets, train):

        batch_size = review.shape[1]

        in_hidden = in_hidden.permute(1, 0, 2)
        targets = targets.permute(1, 0, 2)
        targetSize = self.outRegressor.output_dim

        outputs = torch.zeros(MAXLEN, batch_size, targetSize).to(self.device)

        newsHidden = self.news(review)
        stockHidden = self.stock(in_hidden)

        hidden = torch.cat((newsHidden, stockHidden), dim=1)
        output = final

        for i in range(MAXLEN):
            output, hidden = self.outRegressor(output, hidden)
            outputs[i] = output
            output = (targets[i] if train else outputs[i])

        return outputs