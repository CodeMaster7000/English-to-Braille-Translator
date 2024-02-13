import time

print ("Welcome to CodeMaster7000's English ⇌ Braille translator. Choose from the menu below to get started:")
time.sleep(2)

eng_to_braille = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊',
    'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
    ' ': ' ', ',': '⠂', '.': '⠲', '!': '⠖', '?': '⠦'
}
braille_to_eng = {value: key for key, value in eng_to_braille.items()}

def english_to_braille(text):
    braille_text = ''
    for char in text.lower():
        braille_char = eng_to_braille.get(char, char)
        braille_text += braille_char
    time.sleep(1)
    return braille_text

def braille_to_english(text):
    english_text = ''
    braille_chars = [text[i:i+6] for i in range(0, len(text), 6)]
    for braille_char in braille_chars:
        english_char = braille_to_eng.get(braille_char, braille_char)
        english_text += english_char
    time.sleep(1)
    return english_text

def main():
    while True:
        print("1. English → Braille")
        print("2. Braille → English")
        print("3. Exit")
        time.sleep(1)
        choice = input("Input your choice: ")

        if choice == '1':
            text = input("Enter English text: ")
            braille_text = english_to_braille(text)
            print("Braille:", braille_text)
        elif choice == '2':
            text = input("Enter Braille text: ")
            english_text = braille_to_english(text)
            print("English:", english_text)
        elif choice == '3':
            break
        else:
            print("Invalid choice: please input 1, 2, or 3.")
        time.sleep(1)
        answer = input("Would you like to use the translator again? (yes/no): ")
        if answer.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
