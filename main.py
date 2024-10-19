def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_word(text)
    print(f"{num_words} words found in the document")
    
def count_word(file):
    words = file.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

    