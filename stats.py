def count_words(pathfile):
    number_of_words = 0
    with open(pathfile) as f:
        text = f.read()
        words = text.split()
        for word in words:
            if word != "":
                number_of_words += 1
    return f"Found {number_of_words} total words"

def count_character(pathfile):
    characters = {}
    letters = []
    new = []
    final = []
    with open(pathfile) as f:
        text = f.read()
        low_case = text.lower()
        letters = list(low_case)
        letters.sort()
        for letter in letters:
            if letter.isalpha() == True :
                if letter in characters:
                    characters[letter] +=1
                else:
                    characters[letter] = 1
        for key, value in characters.items():
            new.append({"character": key, "count": value})
        new.sort(key=lambda item: item["count"], reverse=True)
        for item in new:
            message = f"{item['character']}: {item['count']}"
            final.append(message)
        return '\n'.join(final)
    


def sorted_list(pathfile):
    print("============ BOOKBOT ============")
    print(f"Analyzing book at {pathfile}...")
    print("----------- Word Count -----------")
    print(count_words(pathfile))
    print("--------- Character Count ---------")
    print(count_character(pathfile))
    print("============= END =============")


