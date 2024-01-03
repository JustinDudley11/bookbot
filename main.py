def main():
    path_to_book = "books/frankenstein.txt"
    text = book_text(path_to_book)
    num_words = num_words_text(text)
    num_letters = num_let_text(text)
    sorted_let = let_sort(num_letters)
    print(f"--- Begin report of {path_to_book}")
    print(f"{num_words} words found in the document")
    print()
    for letter in sorted_let:
        if not letter["let"].isalpha():
            continue
        else:
            print(f"The {letter['let']} character was found {letter['num']} times")
    print()
    print("--- End report ---")
    
    
def book_text(book_path):
    with open(book_path) as x:
        return x.read()
        
def num_words_text(text):
    total_words = 0
    words = text.split()
    for word in words:
        total_words += 1
    return total_words

def num_let_text(text):
    letters = {}
    for word in text:
        lower_case = word.lower()
        if lower_case in letters:
            letters[lower_case] += 1
        else:
            letters[lower_case] = 1
    return letters

def sort_type(y):
    return y["num"]

def let_sort(num_letters):
    sorted_letters = []
    for let in num_letters:
        sorted_letters.append({"let": let, "num": num_letters[let]})
        sorted_letters.sort(reverse = True, key = sort_type)
    return sorted_letters
    


main()