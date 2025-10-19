#!/usr/bin/env python3

import argparse
import json
import os.path
import string
from config.stopwords import stopwords
from nltk.stem import PorterStemmer
from typing import Iterable



def remove_stopwords(words):
    cleaned_words = []
    for word in words:
        if word in stopwords:
            continue
        cleaned_words.append(word)
    return cleaned_words



def remove_punctuation(sentence: str):
    m = {
        pun_char: None for pun_char in string.punctuation
    }
    trans_table = str.maketrans(m)
    res = str.translate(sentence, trans_table)
    # print(res)
    return res

def do_stemming(words: Iterable[str]):
    stemmer = PorterStemmer()
    return set(stemmer.stem(w) for w in words)



def search(term: str):
    filepath = os.path.abspath(os.path.join("data", "movies.json"))
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        movies = data.get("movies", [])

        term_words = set(do_stemming(remove_stopwords(remove_punctuation(term.lower()).split(" "))))
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
        if not matched:
            print("No movies found.")
        else:
            matched.sort(key=lambda x: x["id"])
            for i, r in enumerate(matched[:5], start=1):
                print(f"{i}. {r['title']}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            search(args.query)
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()
