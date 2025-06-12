import sys
from stats import get_book_text, get_word_count, get_character_count, sort_chars

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    word_count = get_word_count(file_content)
    char_dict = get_character_count(file_content)
    sorted_chars = sort_chars(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()