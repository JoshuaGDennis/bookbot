from stats import get_character_dict
from stats import get_sorted_list
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        dict = get_character_dict(text)
        sorted = get_sorted_list(dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {len(text.split())} total words")
        print("--------- Character Count -------")

        for item in sorted:
            print(f"{item["char"]}: {item["num"]}")

        print("============= END ===============")


main()
