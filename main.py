def count_chars(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts



def main():
    with open("books/frankenstein.txt") as f:
        read_content = f.read()
        

    wordcount = read_content.split()
    print(f"{len(wordcount)} words found in the document")

 
    result = count_chars(read_content)


    char_list = [{'character': char, 'num': count} for char, count in result.items()]


    char_list.sort(key=lambda x: x['num'], reverse=True)


    print("--- Begin report of books/frankenstein.txt ---")
    for char_info in char_list:
        print(f"The '{char_info['character']}' character was found {char_info['num']} times")
    print("--- End report ---")

main()

            