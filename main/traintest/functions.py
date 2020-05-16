import torch
import time

# Call this module to train/test the Network for prediction

PATH = 'pretrainedWeights/weights'

class learnParamter():

    def __init__(self, model, criterion, optimizer, pretrained):
        super().__init__()

        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.pretrained = pretrained

    def normalize(self, batch):
        mean = torch.mean(batch, dim=1, keepdim=True)
        std = torch.std(batch, dim=1, keepdim=True)
        batch = (batch - mean)/std
        return batch

    def validate(self, val_iterator):

        self.model.eval()
        val_loss = 0

        with torch.no_grad():

            for _, batch in enumerate(val_iterator):

                review = batch.r
                i_hidden = batch.h
                i_hidden = self.normalize(i_hidden)
                i_final = batch.f

                target = batch.o

                output = self.model(review, i_hidden, i_final, target, False)
                target = target.permute(1, 0, 2)

                loss = self.criterion(output, target)
                val_loss+=loss.item()

        return val_loss/len(val_iterator)

    def train(self, train_iterator, val_iterator, epochs):
        
        trainLoss = []
        valLoss = []

        print('\nTraining\n')

        if self.pretrained :
            self.model.load_state_dict(torch.load(PATH))

        for i in range(epochs):
            self.model.train()
            train_loss = 0
            
            train_start = time.time()

            for _, batch in enumerate(train_iterator):

                review = batch.r
                i_hidden = batch.h
                i_hidden = self.normalize(i_hidden)
                i_final = batch.f

                target = batch.o

                self.optimizer.zero_grad()

                output = self.model(review, i_hidden, i_final, target, True)
                target = target.permute(1, 0, 2)

                loss = self.criterion(output, target)
                loss.backward()
                self.optimizer.step()
                train_loss+=loss.item()

            train_loss = train_loss/len(train_iterator)
            validation_loss = self.validate(val_iterator)

            train_end = time.time()
            elapsed_time = (train_end - train_start)

            if i > 0 and validation_loss < min(valLoss):
                torch.save(self.model.state_dict(), PATH)

            trainLoss.append(train_loss)
            valLoss.append(validation_loss)

            print(f'Epoch = [{i+1:4d}] || Training Loss = [{train_loss:5.3f}] || Validation Loss = [{validation_loss:5.3f}] || Time Elapsed = [{elapsed_time:3.3f}s]')

        return trainLoss, valLoss

class predict():

    def __init__(self, model, criterion, pretrained):

        self.model = model
        self.criterion = criterion
        self.pretrained = pretrained

    def normalize(self, batch):
        mean = torch.mean(batch, dim=1, keepdim=True)
        std = torch.std(batch, dim=1, keepdim=True)
        batch = (batch - mean)/std
        return batch

    def infer(self, test_iterator):

        if self.pretrained:
            self.model.load_state_dict(torch.load(PATH))

        self.model.eval()
        test_loss = 0
        flag = True
        best_loss = 0
        args = {}

        with torch.no_grad():

            for _, batch in enumerate(test_iterator):

                review = batch.r
                i_hidden = batch.h
                i_hidden = self.normalize(i_hidden)
                i_final = batch.f

                target = batch.o

                output = self.model(review, i_hidden, i_final, target, False)
                target = target.permute(1, 0, 2)

                loss = self.criterion(output, target)
                test_loss+=loss.item()
                best_loss = loss.item() if flag else min(loss, best_loss)
                flag = False

                if best_loss == loss:
                    args['Correct'] = target
                    args['Predicted'] = output
                    args['Loss'] = best_loss

        return test_loss/len(test_iterator), args