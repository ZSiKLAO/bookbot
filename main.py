from stats import get_book_text, get_num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
