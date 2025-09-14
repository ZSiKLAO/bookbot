from stats import get_book_text, get_num_words, get_char_counts

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_counts(book_text)
    for char, count in sorted(char_counts.items()):
        print(f"'{char}': {count}")


if __name__ == "__main__":
    main()
