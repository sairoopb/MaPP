# **MaPP : Market Price Predictor**

## **Requirements**
1. Python 3.6+
2. PyTorch >= 1.4
3. Torchtext >= 0.4
4. Spacy (Also install the english tokenizer model)
5. Ta-Lib (Be cautious to download all requirements while downloading TA Lib)
6. Pandas
7. Beautiful Soup
8. Requests
9. Pandas Datareader
10. Sklearn if you did not split your dataset into test train and validation.

* The script was trained using a NVIDIA P-100 GPU and the results are shown below:
* Training:

![Loss Stats](/Results/result.png)

* And example for a test case:

![Stock Prices](/Results/example.png)

* Pretrained weights have also been included in the repo in the pretrainedWeights folder.
* Also the predictions are being made for a series of 10 days so the model has learnt the trend in the stock with fairly less training time.

#### Code is only written for Goldman Sachs Data and will be later extended for other companies and is tested for Linux based Operating Systems