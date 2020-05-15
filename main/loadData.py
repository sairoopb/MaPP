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
        fields = {'Review' : ('r', REVIEW), 'Input Hidden' : ('h',INPUT_H), 'Input Final' : ('f', INPUT_F), 'Output' : ('o', OUTPUT)}
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
        train_iterator, val_iterator, test_iterator = BucketIterator.splits((train, val, test), sort=False, batch_sizes=(Batch_Size, Batch_Size, 1), device=self.device, shuffle=True)
        return train_iterator, val_iterator, test_iterator, length