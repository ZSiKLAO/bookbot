# stats.py

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def get_num_words(text):  # renamed for clarity
    words = text.split()
    return len(words)
