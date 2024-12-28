FILE_PATH = "books/frankenstein.txt"

def char_count_dict(book_text):
    str_lower = book_text.lower()
    count = {}
    for char in str_lower:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def dict_to_list(dict):
    return_list = []
    for item in dict:
        if item.isalpha():
            return_list.append({"char":item,"count":dict[item]})
    return return_list

def word_count(book_text):
    return len(book_text.split())

def read_file(file_path):
    with open(file_path) as f:
        return f.read()

def sort_on(dict):
    return dict["count"]

def print_report(count, list_of_dicts):
    print(f"--- Begin report of {FILE_PATH} ---")
    for item in list_of_dicts:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    
    print("--- End report ---")

def main():
    book_text = read_file(FILE_PATH)
    count = word_count(book_text)
    char_dict = char_count_dict(book_text)
    char_list = dict_to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    print_report(count,char_list)

main()