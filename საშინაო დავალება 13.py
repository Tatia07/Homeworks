# 1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ფაილში ინფორმაციას
# Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”. input_ ფუნქცია და ციკლი არ უნდა იყოს ფუნქციის შიგნით.
# ციკლში უნდა მოხდეს ფუნქციის გამოძახება, მაშინ თუ ფაილი გაშვებულია შიგნიდა (if __name__ == "__main__")

def add_info(new_info):
    with open('New_file.txt', 'a') as file:
        file.write(new_info + '\n') 

if __name__ == "__main__":
    while True:
        user_input = input('Enter text: ')
        if user_input.lower() == 'enough':
            break
        add_info(user_input)

# 2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, 
# შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os

def create_file(path, file_name):
    file_path = os.path.join(path, file_name)

    try:
        with open(file_path, 'x'):
            print(f"File '{file_name}' created successfully.")
    except FileExistsError:
        print(f"File '{file_name}' already exists.")

    files_in_folder = os.listdir(path)
    if files_in_folder:
        print("Existing files in the folder:")
        for file in files_in_folder:
            print(file)
    else:
        print("No other files in the folder.")

if __name__ == "__main__":
    path = input("Enter the folder path: ")
    file_name = input("Enter the file name: ")

    create_file(path, file_name)

# 3. შექმენი ფუნქცია რომელიც input_ით შეყვანილ ტექსტს დაშიფრავს მორზეს ანბანით და ისე შეინახავს ფაილში (2 დავალებაში შექმნილ ფაილში).

def latin_to_morse(word):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }

    word = word.upper()

    morse_result = ""

    for char in word:
        if char == ' ':
            morse_result += ' '
        elif char in morse_code_dict:
            morse_result += morse_code_dict[char] + ' '

    return morse_result


def fun(user_input):
    morse_text = latin_to_morse(user_input)
    with open('New_file.txt', 'a') as file:
        file.write(f"{user_input}\n")
        file.write(f"{morse_text}\n")

if __name__ == "__main__":
    input_text = input('Enter text: ')
    fun(input_text)