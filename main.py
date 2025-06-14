from stats import count_words, count_characters, sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    content = get_book_text("/mnt/d/code/github/bookbot/books/frankenstein.txt")
    word_count = count_words(content)
    char_count = count_characters(content)
    sorted_count = sort_characters(char_count)

    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_count:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()
