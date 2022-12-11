import random

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}
words = ['code', 'bit', 'list', 'soul', 'next']
answers = []


def morse_encode(word):
    encode_word = []
    for char in word:
        encode_word.append(morse_code.get(char, ''))
    return ' '.join(encode_word)


def get_word():
    return random.choice(words)


def print_statistics():
    pass


def main():
    print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
    print('Нажмите Enter и начнем')
    input()
    for i in range(1, len(words) + 1):
        current_word = get_word()
        word_encoded = morse_encode(current_word)
        print(f'Слово {i} - {word_encoded}')
        answer = input('Расшифровать: ')
        if answer == current_word:
            answers.append(True)
            print(f'Верно! Слово, {current_word}')
        else:
            answers.append(False)
            print(f'Не верно! Слово {current_word}')
    print(answers)


main()
