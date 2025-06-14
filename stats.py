def count_words(content):
    words = content.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_characters(content):
    content = content.lower()
    chars = {}
    for character in content:
        if character != " " and character not in chars:
            chars[character]  = 1
        elif character != " " and character in chars:
            chars[character] += 1
    return chars