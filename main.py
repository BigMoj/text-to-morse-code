from data import morse_code

def translate(text):
    morse_text = ""
    for char in text:
        char = char.upper()
        if char in morse_code:
            morse_text += morse_code[char] + " "
        else:
            morse_text += "       "
    return morse_text

print(translate(input("please insert your text:\n")))


