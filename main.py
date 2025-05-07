def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print (f"{word_count} words found in the document")

def get_book_text(path_to_book_file):
    with open(path_to_book_file) as f:
        file_contents = f.read()
        return file_contents
    
def get_word_count(book_text):
    split_text = book_text.split()
    return len(split_text)

main()