def analyze_word(word):
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1

    twice_chars = {char: count for char, count in counts.items() if count >= 2}
    result_string = "Buchstaben, die mindestens zweimal vorkommen:\n"
    for char, count in twice_chars.items():
        result_string += f"- {char}: {count} mal\n"

    return result_string

def main():
    word = input("Bitte gib ein Wort ein: ")
    result = analyze_word(word)
    print(result)

if __name__ == "__main__":
    main()