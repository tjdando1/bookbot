#!/usr/bin/env python3
def main():
    path = "books/frankenstein.txt"
    text = get_contents(path)
    words = word_count(text)

    print (words)

def word_count(text):
    word_list = text.split()
    return len(word_list)

def get_contents(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents
        
main()
