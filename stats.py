def get_word_count(book_text):
    split_text = book_text.split()
    return len(split_text)

def get_character_count(book_text):
    characters_dict = {}
    book_text = book_text.lower()

    for char in book_text:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    
    return characters_dict









        


        

    


