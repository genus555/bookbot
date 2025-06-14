def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def count_words(content):
    words = content.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def main():
    content = get_book_text("/mnt/d/code/github/bookbot/books/frankenstein.txt")
    word_count = count_words(content)
    print(f"{word_count} words found in the document")

main()
