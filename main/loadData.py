import torch
from torchtext.data import Field, BucketIterator, TabularDataset
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

class Dataloader():
    def __init__(self):
        self.en = spacy.load('en')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def en_tokenizer(self,sentence):
        sentence = sentence.replace(u'\xa0', u' ')
        return [key.text.lower() for key in self.en(sentence)]

    def get(self):
        REVIEW = Field(tokenize=self.en_tokenizer, init_token='<sos>', eos_token='<eos>', stop_words=STOP_WORDS, use_vocab=True)
        INPUT_H = Field(sequential=False,use_vocab=False,pad_token=None,unk_token=None)
        INPUT_F = Field(sequential=False,use_vocab=False,pad_token=None,unk_token=None)
        OUTPUT = Field(sequential=False,use_vocab=False,pad_token=None,unk_token=None)
        fields = {'Review' : ('r', REVIEW), 'Input_Hidden' : ('h',INPUT_H), 'Input_Final' : ('f', INPUT_F), 'Output' : ('o', OUTPUT)}
        trainds, valds, testds = TabularDataset.splits(
            path='./',
            train='train.json',
            validation='val.json',
            test='test.json',
            format='json',
            fields=fields
        )
        REVIEW.build_vocab(trainds, valds)
        length_of_vocab = len(REVIEW.vocab)
        return trainds, valds, testds, length_of_vocab

    def get_iterator(self, Batch_Size=3):
        train, val, test, length = self.get()
        train_iterator, val_iterator, test_iterator = BucketIterator.splits((train, val, test), sort=False, batch_size=Batch_Size, device=self.device, shuffle=True)
        return train_iterator, val_iterator, test_iterator, length

# ==========================================================================
    
    # import pandas as pd
    # from sklearn.model_selection import train_test_split

    # data = pd.read_csv('Data.csv')
    # data = data[['Review', 'Input Hidden', 'Input Final', 'Output']]

    # train, test = train_test_split(data, test_size=0.2, random_state = 1)
    # train, val = train_test_split(train, test_size=0.25, random_state = 1)

    # train.to_csv('train.csv', index=False)
    # val.to_csv('val.csv', index=False)
    # test.to_csv('test.csv', index=False)

    # class BatchGenerator():
    # def __init__(self, dl, review, input_hidden, input_final, Output):
    #     self.dl, self.review, self.input_H, self.input_F, self.out = dl, 
    #       review, input_hidden, input_final, Output
    
    # def __iter__(self):
    #     for batch in self.dl:
    #         review = getattr(batch, self.review)
    #         input_hidden = getattr(batch, self.input_H)
    #         input_final = getattr(batch, self.input_F)
    #         output = getattr(batch, self.out)
    #         yield (review, input_hidden, input_final, output)

    # train_batch_it = BatchGenerator(train_iterator, 'Review', '
    #                   Input_Hidden', 'Input_Final', 'Output') 
    # batch = next(iter(train_iterator))

# ==========================================================================