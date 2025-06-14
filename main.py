from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    content = get_book_text("/mnt/d/code/github/bookbot/books/frankenstein.txt")
    word_count = count_words(content)
    print(f"{word_count} words found in the document")
    print(count_characters(content))

main()
