#!/usr/bin/env python3
import os

def main():
   while True: 
        book = input("Please enter book name: (or type 'exit' to quit): ")
        book_name = book.lower()

        if book_name == "exit":
            print("-----------------------------")
            print("now leaving program")
            print("-----------------------------")
            break

        path = os.path.join("books/", book_name + ".txt")
        
        if os.path.isfile(path) and path.endswith(".txt"):
            try:
                text = get_contents(path)
                words = word_count(text)
                letter_count = letters(text)
                sorted_letters = letter_sort(letter_count)

                print("-----------------------------")
                print(f"For the book {book}")
                print("-----------------------------")      
                print("Letters found in descending order")
                print("-----------------------------")
                for dict in sorted_letters:
                    if not dict["letter"].isalpha():
                        continue
                    print(f"Letter '{dict['letter']}' was found {dict['count']} times.")
                print("-----------------------------")
                print (f"Total words found: {words}")
                print("-----------------------------")
            except Exception as e:
                print(e)
        else:
            print(f"{book} not found, please ensure you have typed name correctly!")
        
def letter_sort(letter_dict):
    letter_lst_dicts = []
    for letter, count in letter_dict.items():
        letter_lst_dicts.append({"letter" : letter, "count" : count})
    letter_lst_dicts.sort(reverse=True, key=lambda letters: letters["count"])
    return letter_lst_dicts
 
def letters(text):
    letter_dict = {}
    lowered_string = (text.lower())
    for i in lowered_string:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    return letter_dict
        
    
def word_count(text):
    word_list = text.split()
    return len(word_list)

def get_contents(path):
    with open(path) as f:
        return f.read()
        
main()
