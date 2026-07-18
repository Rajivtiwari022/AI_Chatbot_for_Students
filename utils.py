import nltk
import string
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()


def clean_sentence(sentence):
    words = nltk.word_tokenize(sentence.lower())

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in string.punctuation
    ]

<<<<<<< HEAD
    return words
=======
    return words
>>>>>>> 39d268a86529baf6297ae635c38359e48839e4b9
