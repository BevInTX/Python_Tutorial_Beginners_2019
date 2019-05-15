
def emoji_converter(words):
    emojis = {
        ":)": "😀",
        ":-)": "😄",
        ":(": "🙁",
        ":-(": "😫"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word)
    return output

def main():
    
    words = input(">").split(' ')
    print(words)

    print(emoji_converter(words))

if __name__ == "__main__":
    main()
    