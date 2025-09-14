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

def sort_char_counts(char_dict):
    # Step 1: Convert the input dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]

    # Step 2: Define a helper function to extract the "num" value
    def get_num(entry):
        return entry["num"]

    # Step 3: Sort the list in-place using the helper, in descending order
    char_list.sort(key=get_num, reverse=True)

    return char_list
