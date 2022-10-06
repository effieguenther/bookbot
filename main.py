def main():

    with open("books/frankenstein.txt") as f:
        text = f.read()
    dictionary = letter_count(text)
    sorted_list = dict_to_sorted(dictionary)

    print("--- Begin report of books.frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    
def count_words(book):
    words = book.split()
    return len(words)   

def letter_count(book):
    dictionary = {}
    for l in book:
        lowered = l.lower()
        if lowered in dictionary:
            dictionary[lowered] += 1
        else:
            dictionary[lowered] = 1
    return dictionary
def sort_on(d):
    return d['num']

def dict_to_sorted(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()