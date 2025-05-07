#imports the get_word_count func from stats.py in the project
from stats import get_word_count
from stats import get_character_count
from stats import sort_list


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list_char_counts = sort_list(character_count)
    print_book_report(book_path, word_count, sorted_list_char_counts)


def get_book_text(path_to_book_file):
    with open(path_to_book_file) as f:
        file_contents = f.read()
        return file_contents
    
def print_book_report(book_path, word_count, sorted_list_char_counts):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for char_dict in sorted_list_char_counts:
        if char_dict["char"].isalpha():
            print (f"{char_dict['char']}: {char_dict['num']}")
        else:
            continue
    print ("============= END ===============")
    
    #Can use a if not format instead of the if loop above
    #for item in chars_sorted_list:
        #if not char_dict["char"].isalpha():
            #continue
        #print(f"etc. etc. etc.

main()
