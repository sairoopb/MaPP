import torchtext
from torchtext.data import Field, BucketIterator, TabularDataset
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import pandas as pd
from sklearn.model_selection import train_test_split

en = spacy.load('en')

data = pd.read_csv('Data.csv')

data = data[['Review', 'Input Hidden', 'Input Final', 'Output']]

train, test = train_test_split(data, test_size=0.2, random_state = 1)
train, val = train_test_split(train, test_size=0.25, random_state = 1)

train.to_csv('train.csv', index=False)
val.to_csv('val.csv', index=False)
test.to_csv('test.csv', index=False)

COMPANY = 'GS'

def en_tokenizer(sentence):
    sentence = sentence.replace(u'\xa0', u' ')
    return [key.text.lower() for key in en(sentence)]

SRC = Field(tokenize=en_tokenizer, init_token='<sos>', eos_token='<eos>', stop_words=STOP_WORDS, use_vocab=True)

fields = [('Review', SRC), ('Input Hidden', None), ('Input Final', None), ('Output', None)]

trainds, valds = TabularDataset.splits(path='./', format='csv', train='train.csv', validation='val.csv', fields=fields, skip_header=True)

SRC.build_vocab(trainds, valds)