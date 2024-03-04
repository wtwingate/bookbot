def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}

    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        elif letter.isalpha():
            letters[letter] = 1
    return letters


def print_report(book, word_count, letter_count):
    print(f"---Begin report of {book}---")
    print()
    print(f"{word_count} words found in this document")
    print()
    for letter in letter_count:
        for key, value in letter.items():
            print(f"The letter '{key}' was found {value} times")
    print()
    print("---End report---")


def sort_results(letter_count):
    sorted_list = []
    for key, value in letter_count.items():
        sorted_list.append({key: value})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def sort_on(dict):
    return list(dict.values())[0]


def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = sort_results(count_letters(file_contents))
        print_report(book, word_count, letter_count)


main()
