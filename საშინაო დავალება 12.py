"1. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და ამოშლის მასში ყველა დუბლირებულ ინფორმაციას."

def unique_dict(dict1):
    unique_dict = {}
    values_set = set()

    for key, value in dict1.items():
        if value not in values_set:
            unique_dict[key] = value
            values_set.add(value)

    return unique_dict

original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
result = unique_dict(original_dict)

print(result)

"2. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და შეამოწმებს ცარიელია თუ არა ის (დააბრუნებს True თუ ცარიელია ან False_ს თუ არაა ცარიელი.)"

def check_dict(dict2):
    if len(dict2) == 0:
        return True
    else:
        return False
    
my_dict = {'Name': 'Tatia', 'Age': 16}
result = check_dict(my_dict)

my_dict1 = { }
result1 = check_dict(my_dict1)

print(result)
print(result1)

"""3. დაწერე ფუნქცია რომელიც მიიღებს სტრიქონის ტიპის მონაცემს, შექმნის მისგან ლექსიკონს და დააბრუნებს. (ლექსიკონის გასაღები სტრიქონში არსებული სიმბოლოებია, მნიშვნელობები კი განმეორების რაოდენობა. 
მაგ: 'w3schools'
Expected output: {'w': 1, '3': 1, ‘s': 2, ‘c': 1, ‘h': 1, 'o': 2, ‘l': 1}"""

def create_dict(dict3):
    char_count = {}

    for char in dict3:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

user_input = str(input("Enter a string: "))
result_dict = create_dict(user_input)

print(result_dict)

"4. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და დააბრუნებს  ერთ სიაში გაერთიანებულ key, value წყვილებს."

def dict_to_list(dict4):
    return list(dict4.items())
    
my_dict = {'Name': 'Tatia', 'Age': 16, 'Class': 11}
result = dict_to_list(my_dict)

print(result)