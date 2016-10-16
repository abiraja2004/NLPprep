from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

sent = "This is the example sentence showing off the stop words filtration."

stop_words = set(stopwords.words("english"))

# print(stop_words)

filtered_words = []

words = word_tokenize(sent)

# for i in words:
#     if i not in stop_words:
#         filtered_words.append(i)
# print("original sentence : " + sent)
# print("\n\nList of filtered words after removing stop words : ")
# print(filtered_words)

f_words = [i for i in words if not i in stop_words]

print(f_words)
