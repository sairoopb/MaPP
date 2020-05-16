# This is the final output network for predicting stock prices

import torch.nn as nn

class OutputRegressor(nn.Module):

    def __init__(self, input_dim, hid_dim):
        super().__init__()

        self.output_dim = input_dim
        self.hid_dim = 2 * hid_dim

        self.rnn = nn.GRU(self.output_dim, self.hid_dim)

        self.fc1 = nn.Linear(self.hid_dim, hid_dim)
        self.fc2 = nn.Linear(hid_dim, self.output_dim)

    def forward(self, x, hidden):
        
        x, hidden = self.rnn(x.unsqueeze(0), hidden.unsqueeze(0))
        x = self.fc1(x)
        x = self.fc2(x)

        # X is of dim [1, Batch Size, Input Dim == dim([Open, Lown, High, Close])]
        # Hidden is of dim [1, Batch Size, Hidden Dim]
        return x.squeeze(0), hidden.squeeze(0)