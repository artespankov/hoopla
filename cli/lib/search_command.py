import json
import os.path
import string
from .stopwords import stopwords
from nltk.stem import PorterStemmer
from typing import Iterable

def remove_stopwords(words):
    cleaned_words = []
    for word in words:
        if word in stopwords:
            continue
        cleaned_words.append(word)
    return cleaned_words



def remove_punctuation(text: str):
    m = {
        pun_char: None for pun_char in string.punctuation
    }
    trans_table = str.maketrans(m)
    return text.translate(trans_table)

def do_stemming(words: Iterable[str]):
    stemmer = PorterStemmer()
    return set(stemmer.stem(w) for w in words)



def search(query: str):
    filepath = os.path.abspath(os.path.join("cli", "lib", "data", "movies.json"))
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        movies = data.get("movies", [])

        term_words = set(do_stemming(remove_stopwords(remove_punctuation(query.lower()).split(" "))))
        matched = []
        matched_titles = set()
        for movie in movies:
            normalized_title = remove_punctuation(movie["title"].lower())
            title_words = set(remove_stopwords(normalized_title.split(" ")))
            title_words = do_stemming(title_words)
            for term_word in term_words:
                for title_word in title_words:
                    if term_word in title_word and normalized_title not in matched_titles:
                        matched.append(movie)
                        matched_titles.add(normalized_title)
                        break
        return matched