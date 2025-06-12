def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(char_dict):
    return char_dict["num"]

def sort_chars(dic):
    chars = []
    for char, count in dic.items():
        chars.append({"char": char, "num": count})
    chars.sort(reverse=True, key=sort_on)
    result = {}
    for char_info in chars:
        char = char_info["char"]
        count = char_info["num"]
        result[char] = count
    return result


