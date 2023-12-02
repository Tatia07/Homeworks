# 1 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

def unique_list(input_list):
    unique_elements = list(set(input_list))
    return unique_elements

print(unique_list([1, 1, 2, 5, 4, 3, 5, 3, 4]))

# 2 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).

def immutable_set(input_list):
    return frozenset(input_list)

my_list = [1, 2, 2, 3, 4, 4, 5]
result = immutable_set(my_list)

print(result)

# 3 შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

def set_to_tuple(set1, set2):
    united_set = set1.union(set2)
    tupled_sets = tuple(united_set)
    return tupled_sets

set_1 = {1, 2, 3, 4}
set_2 = {5, 6, 7, 8}

result = set_to_tuple(set_1, set_2)
print(result)

# 4 შექმენი ფუნქცია რომელიც მიიღებს მომხმარებლის სახელს და პაროლს, ასევე სიის სახელს. პაროლს გაუკეთებს ჰეშირებას და მონაცემს შეინახავს tuple ტიპის
# მონაცემად გადაცემულ სიაში. შედეგი უნდა დააბრუნოს [("user1", "pass1")]

import bcrypt

def user_info(name, password, list_name):
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    list_name = (name, hashed)

    return list_name

name = input("Enter your name: ")
password = input("Enter your password: ")
tuple_name = input("Enter your list name: ")

result = user_info(name, password, tuple_name)

print(result)