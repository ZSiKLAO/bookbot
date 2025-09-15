import sys
from stats import get_book_text, get_num_words, get_char_counts, sort_char_counts

def main():
    # ✅ Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 📘 Use the second argument as the path to the book
    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"❌ File not found: {book_path}")
        sys.exit(1)
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
        sys.exit(1)

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words\n")

    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    for entry in sorted_chars:
        char = entry["char"]
        count = entry["num"]
        if char.isalpha():
            print(f"{char}: {count}")

if __name__ == "__main__":
    main()
