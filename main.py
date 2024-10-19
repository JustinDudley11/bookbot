def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_word(text)
    num_character = count_character(text)
    print(f"{num_words} words found in the document")
    print(num_character)
    
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
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

main()

    