# stats.py

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def get_num_words(text):  # renamed for clarity
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()  # Normalize to lowercase
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
