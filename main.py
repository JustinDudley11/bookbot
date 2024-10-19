def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_word(text)
    num_character = count_character(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document.")
    for let in num_character:
        print(f"The {let} character was found {num_character[let]} times")
    print("--- End Report ---")
    
def count_word(file):
    words = file.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_character(file):
    chars_dict = {}
    for c in file:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars_dict:
                chars_dict[lowered] += 1
            else:
                chars_dict[lowered] = 1
    return dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))

main()

    