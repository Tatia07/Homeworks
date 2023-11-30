# პირველი დავალება
# 1.ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული მომხმარებლის ინფორმაცია 
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის 
# შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად: 
# Name: Elene
# Lastname: Khardava
# Age: 21

# consumer_info = []

# for i in range(3):
#     first_name = input("Enter your name: ")
#     last_name = input("Enter your last name: ")
#     age = input("Enter your age: ")
    
#     user_info = [first_name, last_name, age]
#     consumer_info.append(user_info)

# index = int(input("Enter the index (0, 1, or 2): "))

# if 0 <= index < len(consumer_info):
#     user = consumer_info[index]
#     print(f"Name: {user[0]}\nLastname: {user[1]}\nAge: {user[2]}")
# else:
#     print("Invalid index. Please enter a valid index (0, 1, or 2).")

# მეორე დავალება
# 2.მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე თუ სახელის ველი არ იქნება ცარიელი, ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია. 
# მისი მონაცემები შეინახე ლისთში. შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ შემოყვანილი ინფორმაცია სიაში შენახულ 
# ინფორმაციას. დაბეჭდე შესაბამისი მესიჯი.

# user_name = input("Enter username: ")
# password = input("Enter password: ")

# user_info = []

# if user_name.strip() and len(password) >= 8:
#         info = [user_name, password]
#         user_info.append(info)

# answer = input("Would you like to sign in your account? Yes / No : ")

# if answer == "yes":
#         Name = input("Enter your username: ")
#         Password = input("Enter your password: ")
#         if Name == user_name and Password == password:
#                 print("You have access to your account")
#         else:
#                 print("Username or password is incorrect! Try again!")
# else:
#         print("Have a good day!")


# მესამე დავალება
# 3.შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია. მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. 
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდა მის შესახებ არსებული ინფორმაცია რეზუმის სახით.

# actors = [
#     {"first_name": "Angelina", "last_name": "Jolie", "age": 46},
#     {"first_name": "Jennifer", "last_name": "Lawrence", "age": 32},
#     {"first_name": "Leonardo", "last_name": "Dicaprio", "age": 47},
#     {"first_name": "Chris", "last_name": "Hemsworth", "age": 38},
#     {"first_name": "Brad", "last_name": "Pitt", "age": 58},
# ]

# search_name = input("Enter actor's first name or last name: ")

# found_actor = None

# for actor in actors:
#     if search_name.lower() in actor["first_name"].lower() or search_name.lower() in actor["last_name"].lower():
#         found_actor = actor
#         break

# if found_actor:
#     print(f"Actor Information: \nFirst Name: {found_actor['first_name']} \nLast Name: {found_actor['last_name']} \nAge: {found_actor['age']}")
# else:
#     print("Actor not found in the list.")

# მეოთხე დავალება
# არასავალდებულო დავალება:
# დაასრულე იქსიკის და ნულიკის თამაში

# 1.	შექმენი მატრიცა კვადრატების ნომრებით.
# 2.	შექმენი მთავარი ციკლი.
# 3.	შემოაყვანინე პირველ მომხმარებელს იქსიკის ჩასმის ლოკაცია (კვადრატის ნოომერი)
# 4.	ორმაგი for ციკლის მეშვეობით დაამუშავე ინფორმაცია და ჩასვი იქსიკი ლოკაციაზე.
# 5.	შემოაყვანინე მეორე მომხმარებელს ნულიკის ჩასმის ლოკაცია. (კვადრატის ნოომერი)
# 6.	ორმაგი for ციკლის მეშვეობით დაამუშავე ინფორმაცია და ჩასვი იქსიკი ლოკაციაზე.
# 7.	დაბეჭდე არსებული მდგომარეობა.
# 8.	გაამეორე ციკლი მანამ, სანამ ლოგიკური გამონათქვამის მეშვეობით არ დადგინდება რომ რომელიმე მოთამაშემ მოიგო.

# map = [    
#     [1, 2, 3],    
#     [4, 5, 6],    
#     [7, 8, 9]
# ]

# def print_map():
#     for row in map:
#         print(row)

# def check_win(player):
#     for row in map:
#         if all(cell == player for cell in row):
#             return True
#     for col in range(3):
#         if all(map[row][col] == player for row in range(3)):
#             return True
#     if all(map[i][i] == player for i in range(3)) or all(map[i][2 - i] == player for i in range(3)):
#         return True
#     return False

# while True:
#     player1 = int(input("Player 1 (X): Enter number 1-9: "))
#     for row in map:
#         for index, item in enumerate(row):
#             if player1 == item:
#                 row[index] = "X"
#                 break

#     print_map()
    
#     if check_win("X"):
#         print("Player 1 (X) wins!")
#         break
    
#     player2 = int(input("Player 2 (O): Enter number 1-9: "))
#     for row in map:
#         for index, item in enumerate(row):
#             if player2 == item:
#                 row[index] = "O"
#                 break

#     print_map()

#     if check_win("O"):
#         print("Player 2 (O) wins!")
#         break
