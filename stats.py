def count_words(content):
    words = content.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count