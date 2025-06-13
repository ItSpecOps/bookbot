from stats import get_word_count,get_num_chars,convert_dic_to_dic_list
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])

    #headline
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    #data
    print(get_word_count(text))
    print("--------- Character Count -------")
    for entry in convert_dic_to_dic_list(get_num_chars(text)):
        key = list(entry.keys())[0]
        value = entry[key]
        print(f"{key}: {value}")
    print("============= END ===============")

main()
