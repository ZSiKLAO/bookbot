from stats import get_book_text, get_num_words, get_char_counts, sort_char_counts

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document\n")

    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    for entry in sorted_chars:
        char = entry["char"]
        count = entry["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

if __name__ == "__main__":
    main()
