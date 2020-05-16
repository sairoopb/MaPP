import matplotlib.pyplot as plt

class showTrain():

    def __init__(self, trainLoss, valLoss, epochs):
        
        self.trainLoss = trainLoss
        self.valLoss = valLoss
        self.epochs = [i+1 for i in range(epochs)]

    def plotSave(self):

        fig, ax = plt.subplots()
        ax.plot(self.epochs, self.trainLoss, color='blue', label='Train Loss')
        ax.plot(self.epochs, self.valLoss, color='red', label='Validation Loss')
        ax.set(xlabel='Epoch', ylabel='Loss',title='Loss Curve Statistics')
        ax.legend()
        fig.savefig('result.png')
        plt.show()

class showResults():

    def __init__(self, args):
        
        self.prediction = args['Predicted']
        self.target = args['Correct']
        self.y_pred = {'Open' : [], 'Low' : [], 'High' : [], 'Close' : []}
        self.y_true = {'Open' : [], 'Low' : [], 'High' : [], 'Close' : []}
        self.x = [i for i in range(len(self.target))]

        self.dictMap = {'ax1' : 'Open', 'ax2' : 'Close', 'ax3' : 'Low', 'ax4' : 'High'}

        for day in self.prediction:
            self.y_pred['Open'].append(day[0][0])
            self.y_pred['Low'].append(day[0][1])
            self.y_pred['High'].append(day[0][2])
            self.y_pred['Close'].append(day[0][3])

        for day in self.target:
            self.y_true['Open'].append(day[0][0])
            self.y_true['Low'].append(day[0][1])
            self.y_true['High'].append(day[0][2])
            self.y_true['Close'].append(day[0][3])

    def plotSave(self):

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

        ax1.plot(self.x, self.y_pred[self.dictMap['ax1']], color='red', label='Prediction')
        ax1.plot(self.x, self.y_true[self.dictMap['ax1']], color='blue', label='Correct')
        ax1.set(xlabel='Time', ylabel='Cost', title=self.dictMap['ax1'])
        ax1.legend()

        ax2.plot(self.x, self.y_pred[self.dictMap['ax2']], color='red', label='Prediction')
        ax2.plot(self.x, self.y_true[self.dictMap['ax2']], color='blue', label='Correct')
        ax2.set(xlabel='Time', ylabel='Cost', title=self.dictMap['ax2'])
        ax2.legend()

        ax3.plot(self.x, self.y_pred[self.dictMap['ax3']], color='red', label='Prediction')
        ax3.plot(self.x, self.y_true[self.dictMap['ax3']], color='blue', label='Correct')
        ax3.set(xlabel='Time', ylabel='Cost', title=self.dictMap['ax3'])
        ax3.legend()

        ax4.plot(self.x, self.y_pred[self.dictMap['ax4']], color='red', label='Prediction')
        ax4.plot(self.x, self.y_true[self.dictMap['ax4']], color='blue', label='Correct')
        ax4.set(xlabel='Time', ylabel='Cost', title=self.dictMap['ax4'])
        ax4.legend()

        fig.tight_layout(pad=2.0)
        fig.savefig('example.png')
        plt.show()