# 1.დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას და filter_ის გამოყენებით.

# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = map(lambda x: x * 3, my_list)

# print(list(result))

# 2.დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა 
# სიმბოლოთი იწყება.  (გამოიყენე .isupper() მეთოდი)

# names_list = ["Jack", "john", "Nick", "Jordan", "Sam", "kate", "lily"]

# filtered = list(filter(lambda x: x[0].isupper(), names_list))
# result = len(filtered)

# print(result)

# 3.დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.

# numbers = [3, -5, 7, -2, 8, -1, -4]

# positive_numbers = list(filter(lambda x: x > 0, numbers))
# negative_numbers = list(filter(lambda x: x < 0, numbers))

# sum_positive = sum(positive_numbers)
# sum_negative = sum(negative_numbers)

# print("Sum of positive numbers:", sum_positive)
# print("Sum of negative numbers:", sum_negative)

# 4.დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა მომხმარებლისგან 
# დააზღვიე try და except ბლოკის მეშვეობით.

# user_name = input("Enter username: ")
# password = input("Enter password: ")

# user_info = []

# if user_name.strip() and len(password) >= 8:
#     info = [user_name, password]
#     user_info.append(info)

# answer = input("Would you like to sign in to your account? Yes / No: ")

# if answer.lower() == "yes":
#     Name = input("Enter your username: ")
#     Password = input("Enter your password: ")
#     try:
#         if Name == user_name and Password == password:
#             print("You have access to your account.")
#             action = input("Do you want to deposit money? Yes / No: ")
#             if action.lower() == "yes":
#                 try:
#                     amount = float(input("Enter the amount to deposit: "))
#                     if amount >= 0:
#                         print(f"Deposited ${amount} into your account.")
#                     else:
#                         print("Invalid deposit amount. Amount should be non-negative.")
#                 except ValueError:
#                     print("Invalid input. Please enter a valid amount.")
#             else:
#                 print("Have a good day!")
#         else:
#             print("Username or password is incorrect. Try again.")
#     except Exception as e:
#         print("An error occurred:", str(e))
# else:
#     print("Have a good day!")
