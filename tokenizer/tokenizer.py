from nltk.tokenize import sent_tokenize, word_tokenize

eg = "Hello, World this is Mr. Pranav Kanade and this is the 1st NLP " \
     "program that I am typing. BUt it feels pretty awesome!!"

for i in sent_tokenize(eg):
    print(i)
