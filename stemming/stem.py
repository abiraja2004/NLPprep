# I was taking a ride in car.

# I was riding a car.

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["Playing", "faking", "minimizing", "maximizing", "played", "beautifully"]

for w in words:
    print(ps.stem(w))

    
