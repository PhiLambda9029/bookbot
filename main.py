import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
print(f"The book path you provided is: {book_path}")

def get_book_text (pathfile):
    with open(pathfile) as f:
        file_content= f.read()
    return file_content

from stats import count_words

from stats import count_character

from stats import sorted_list

def main():
    frankenstein = sorted_list(book_path)
    #return (frankenstein)

main()

