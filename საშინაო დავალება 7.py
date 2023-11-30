# ჩაძირობანა:
# შეადგინე ჩაძირობანას თამაში. სადაც კომპიუტერი შემთხვევითად შეუტევს შენს პოზიციებს და შენც უპასუხებ მას. ორივე მოთამაშეს გააჩნია 20 პოზიცია, 
# რომელზეც შეუძლია სამი ხომალდის განლაგება. ყველაზე მცირე ხომალდი ერთ პოზიციას იკავებს, საშუალო ორს, დიდი კი სამს. თითოეულ ხომალდს აქვს 
# სახელი და პოზიციის აღმნიშვნელი კოორდინატები. თუ ხომალდის ყველა პოზიცია დაიბომბა, პროგრამამ უნდა გვაცნობოს რომელი ხომალდი ჩაიძრა. ასევე 
# პროგრამამ უნდა გამოიტანოს გამარჯვებულის სახელი.
# კოდის დასაწერად გამოიყენეთ სიები. მომხმარებელს ინფორმაცია შეჰყავს ხომალდებზე input ფუნქციის გამოყენებით. კომპიუტერის ფლოტს განლაგების 
# რამდენიმე ვარიანტი შეუდგინე წინასწარ და იქიდან შემთხვევითად აარჩევინე ერთერთი.
# მაგ. [ [„Maverick“, [4]], [„Gunner“, [10, 11]], [„Matilda“, [17, 18, 19]] ]
# სექტორის აფეთქებისას პოზიცია სიაში იქსით უნდა შეიცვალოს.

# import random

# def place_ships():
#     ships = []
#     for ship_size in [1, 2, 3]:
#         while True:
#             try:
#                 positions = input(f"Enter positions for a {ship_size}-size ship (e.g., 1 2 3): ").split()
#                 positions = [int(pos) for pos in positions]
#                 if len(positions) == ship_size and all(1 <= pos <= 10 for pos in positions):
#                     ships.append(positions)
#                     break
#                 else:
#                     print("Invalid positions. Please try again.")
#             except (ValueError, IndexError):
#                 print("Invalid input. Please enter valid positions.")
#     return ships

# def random_computer_ships():
#     computer_ships = []
#     for ship_size in [1, 2, 3]:
#         while True:
#             positions = random.sample(range(1, 11), ship_size)
#             if positions not in computer_ships:
#                 computer_ships.append(positions)
#                 break
#     return computer_ships

# def display_board(player_board, computer_board):
#     print("Your board:")
#     for pos in range(1, 11):
#         if pos in player_board:
#             print("S", end=" ")
#         else:
#             print("O", end=" ")
#     print("\nComputer's board:")
#     for pos in range(1, 11):
#         if pos in computer_board:
#             print("O", end=" ")
#         else:
#             print("X", end=" ")
#     print("\n")

# def play_game():
#     player_ships = place_ships()
#     computer_ships = random_computer_ships()
#     player_board = set(sum(player_ships, []))
#     computer_board = set(sum(computer_ships, []))
#     player_hits = set()
#     computer_hits = set()
#     winner = None

#     while True:
#         display_board(player_board, computer_board)
#         player_move = int(input("Enter your attack position (1-10): "))

#         if player_move in computer_board:
#             print("You hit a ship!")
#             computer_board.remove(player_move)
#             player_hits.add(player_move)
#         else:
#             print("You missed!")

#         if not computer_board:
#             winner = "Player"
#             break

#         computer_move = random.randint(1, 10)

#         if computer_move in player_board:
#             print("Computer hit your ship!")
#             player_board.remove(computer_move)
#             computer_hits.add(computer_move)
#         else:
#             print("Computer missed!")

#         if not player_board:
#             winner = "Computer"
#             break

#     display_board(player_board, computer_board)
#     print(f"{winner} wins!")

# play_game()