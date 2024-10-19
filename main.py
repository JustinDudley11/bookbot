def main():
    with open("books/frankenstein.txt") as b:
        file_contents = b.read()
        
    def count_word(file):
        words = file.split()
        word_sum = 0
        for word in words:
            word_sum += 1
        return word_sum

    print(count_word(file_contents))
main()

    