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

def sort_list(char_count_dict):
    sorted_list_of_dict = []
    
    for key, value in char_count_dict.items():
        individual_dict = {"char": key, "num": value}
        sorted_list_of_dict.append(individual_dict)
    
    # Sort using a lambda function instead of a separate sort_num function
    sorted_list_of_dict.sort(reverse=True, key=lambda d: d["num"])

    return sorted_list_of_dict










        


        

    


