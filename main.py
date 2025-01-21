def count_words(book_text):
    return len(book_text.split())

def character_count(book_text):
    char_count = {}
    for word in book_text.lower().split():
        for char in list(word):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_count[" "] = book_text.count(" ")
    return char_count

def sort_on(dict):
    return dict["num"]

def dict_to_list_of_dict(book_text):
    char_dict = character_count(book_text)
    sorted_dict = []
    for key in char_dict:
        if key.isalpha():
            sorted_dict.append({"char": key, "num": char_dict[key]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def char_report(book_text, file_path):
    word_count = count_words(book_text)
    char_dict_list = dict_to_list_of_dict(book_text)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for dict in char_dict_list:
        char = dict["char"]
        num = dict["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    char_report(file_contents, file_path)

main()