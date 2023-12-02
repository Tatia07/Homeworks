# პირველი დავალება
# 1.დაასრულე ჯეირანის თამაშის პროგრამა ციკლის გამოყენებით. თამაშის დასასრულებლად რომელიმე მოთამაშემ უნდა დააგროვოს 3 ქულა.

from random import choice

choice_list = ["rock", "scissors", "paper"]
human_score = 0
computer_score = 0

while human_score < 3 and computer_score < 3:
    computer_choice = choice(choice_list)

    human_choice = input("Choose one of the following: rock / scissors / paper: ").lower()

    if human_choice in choice_list:
        if human_choice == computer_choice:
            print("Draw!")
        elif (human_choice == "rock" and computer_choice == "scissors") or (human_choice == "scissors" and computer_choice == "paper") or (human_choice == "paper" and computer_choice == "rock"):
            print("Human Wins!")
            human_score += 1
        else:
            print("Computer Wins!")
            computer_score += 1
    else:
        print("You must only choose from the list!")

if human_score >= 3:
    print("Human wins the game!")
else:
    print("Computer wins the game!")


# მეორე დავალება
# 2.ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.

num = int(input("Enter number: "))

for i in range(1, num + 1):
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")


# მესამე დავალება
# 3.შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია თანხა 3000 ლარის ოდენობით. პროგრამა გეკითხება გაწეულ ხარჯს 
# და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0_ს. შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა 
# ნაკლებია დანახარჯის თანხაზე, პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.

bank_account = 3000

while True:
    answer = int(input("Enter your expense: "))
    if answer == 0:
        print(f"There's {bank_account - answer}$ in your bank account.")
        break
    if answer > bank_account:
        print("There is not enough money in the account")
    else:
        bank_account -= answer
    

# მეოთხე დავალება
# 4.დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?” 
# მაგ.
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება 
# „User Said Whaaat!?” 
# “User Said Hello”

while True:
    user_input = input("Enter a word: ")
    if user_input.lower() == "quit":
        print("User said whaaat!?")
        print(f"User said {user_input}")
        break
    else:
        print("User said whaaat!?")
        print(f"User said {user_input}")