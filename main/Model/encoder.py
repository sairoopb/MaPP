import torch
import torch.nn as nn

# ====================Note=======================
    # This model architecture is still under 
    # construction and can be made better if 
    # more compute is available one improvement 
    # is to increase the number of hidden layers
    # and maybe add skip connections for gradient 
    # flow like in DenseNet
# ===============================================

BIDIRECTIONAL = True

# This if for encoding the data of the News text

class NewsEncoder(nn.Module):

    def __init__(self, vocab_len, emb_dim, hid_dim, dropout):
        super().__init__()

        self.input_dim = vocab_len
        self.emb_dim = emb_dim
        self.hid_dim = hid_dim

        self.bidirectional = BIDIRECTIONAL
        self.embedding = nn.Embedding(self.input_dim, self.emb_dim)
        self.rnn = nn.LSTM(self.emb_dim, self.hid_dim, bidirectional=self.bidirectional)
        self.fc = nn.Linear(self.hid_dim*2, self.hid_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, src):

        emb = self.dropout(self.embedding(src))
        _, internal_states = self.rnn(emb)
        cells = internal_states[-1]
        cells = torch.cat((cells[-2, :, :],cells[-1, :, :]), dim=1)
        cells = self.fc(cells)
        
        # Cells dimension is [Batch Size, Hidden Dim]

        return cells

# This is for encoding the previous Stock data

class StockEncoder(nn.Module):

    def __init__(self, input_dim, hid_dim):
        super().__init__()

        self.input_dim = input_dim
        self.hid_dim = hid_dim

        self.rnn = nn.GRU(self.input_dim, self.hid_dim)

    def forward(self, src):

        _, hidden = self.rnn(src)
        out = hidden[-1, :, :]
        
        # Out dimension is [Batch SIze, Hidden Dim]
        return out

        