# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად: 
# input: “ablabdabdab”
# Output: „Tripled: ablabdabdabablabdabdabablabdabdab“

# user_input = input("Enter something: ")

# def triple():
#     print(user_input * 3)
# triple()


# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

# def calculate():
#     weight = int(input("Enter your weight: "))

#     weight_on_moon = weight / 6
#     print(f"Your weight on moon would be {weight_on_moon} kg.")
# calculate()

# 3.შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input()   ფუნქციის დახმარებით (სამ მონაცემს _ 
# პირველ რიცხვს, მოქმედებას (+ - * / ^), მეორე რიცხვს)  მაგ. „2 * 6“.  ფუნქცია დაშლის სტრიქონს split() ფუნქციის გამოყენებით. 
# დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი. 
# ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)

# def calculator():
#     user_input = input("Enter an expression :")
#     parts = user_input.split()

#     num1, operator, num2 = parts

#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#     except ValueError:
#         return "Invalid input. Please enter valid numbers."

#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             return "Numbers can't be divided by 0."
#         return num1 / num2
#     else:
#         return "Invalid operator. Please choose only one of the operators: +, -, /, *."

# result = calculator()
# print("Result", result)

# გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური სიმბოლოებით დაწერილ სიტყვას,
# დაშიფრავს მორსეს ანბანით და დააბრუნებს შედეგს. 

# def latin_to_morse(word):
#     morse_code_dict = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
#         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
#         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
#         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
#         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
#         'Z': '--..',
#         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#     }

#     word = word.upper()

#     morse_result = ""

#     for char in word:
#         if char == ' ':
#             morse_result += ' '  
#         elif char in morse_code_dict:
#             morse_result += morse_code_dict[char] + ' '  

#     print(morse_result)

# latin_to_morse("Hello")
