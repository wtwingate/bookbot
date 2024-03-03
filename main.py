import re


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}

    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        elif re.match("[a-z]", letter):
            letters[letter] = 1
    return letters


def print_report():
    pass


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)


main()
