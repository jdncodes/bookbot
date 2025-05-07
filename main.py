#imports the get_word_count func from stats.py in the project
from stats import get_word_count
from stats import get_character_count


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    #print (f"{word_count} words found in the document")
    print (character_count)

def get_book_text(path_to_book_file):
    with open(path_to_book_file) as f:
        file_contents = f.read()
        return file_contents
    

main()
