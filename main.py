def character_printer(count):
    for key in count:
        print(f"The {key} character was found {count[key]} times\n")
                
              
def character_dict(text):
    count={}
    words=text.split()
    for word in words:
        for char in word:
            lowered=char.lower()
            if lowered in count:
                count[lowered]+=1
            else:
                count[lowered]=0
    return count

def count_words(text):
    words= text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)

    print(text)

    print(f"--- Begin report of {book_path} ---")

    print (f"\nDocument has {count_words(text)} words")

    character_dictionary=character_dict(text)

    character_printer(character_dictionary)

    print("--- End report ---")

main()
