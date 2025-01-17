def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text, book_path)

def print_report(text, path):
    print(f"--Begin report of {path}--")
    print(f"{get_word_count(text)} words found in text.")
    print(sort_by_num(text))


def sort_by_num(text):
    chars = count_characters(text)
    new_list = []
    for char in chars:
        if char.isalpha():
            new_list.append({char: chars[char]})
    return sorted(new_list, key=lambda d: d[0])
    


def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_word_count(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()