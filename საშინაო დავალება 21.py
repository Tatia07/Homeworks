# 1. საკლასო დავალებაში დაწერილ კოდს დაამატე dill_ით სერიალიზაციის და დესერიალიზაციის შესაძლებლობა.
# შეინახე ცვლადში მარტივი ლამბდა ფუნქცია და დატესტე კოდი.

import json
import pickle
import dill 

def serialize(obj, filename):
    try:
        with open(filename + '.json', 'w') as file:
            json.dump(obj, file)
        print(f"Object serialized using JSON and saved in {filename}")
    except:
        print(f"JSON serialization failed")
        try:
            with open(filename + '.pickle', 'wb') as file:
                pickle.dump(obj, file)
            print(f"Object serialized using pickle and saved in {filename}")
        except:
            print(f"Pickle serialization failed")
            try:
                with open(filename + '.dill', 'wb') as file:
                    dill.dump(obj, file)
                print(f"Object serialized using dill and saved in {filename}")
            except:
                print(f"Dill serialization failed")
                print("This object can't be serialized.")
 
def deserialize(filename):
    try:
        with open(filename + '.json', 'r') as file:
            obj = json.load(file)
            print("Object deserialized using JSON")
            print(obj)
    except:
        print(f"JSON deserialization failed")
        try:
            with open(filename + '.pickle', 'rb') as file:
                obj = pickle.load(file)
                print("Object deserialized using pickle")
                print(obj)
        except:
            print(f"Pickle deserialization failed")
            try:
                with open(filename + '.dill', 'rb') as file:
                    obj = dill.load(file)
                print("Object deserialized using dill")
                print(obj)
            except:
                print(f"Dill deserialization failed")
                print("Deserialization unsuccessful.")
 
if __name__ == "__main__":
    # Dictionary
    sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

    serialize(sample_dict, 'sample_dict_json')
    deserialize('sample_dict_json')

    serialize(sample_dict, 'sample_dict_pickle')
    deserialize('sample_dict_pickle')

    serialize(sample_dict, 'sample_dict_dill')
    deserialize('sample_dict_dill')

    # list
    sample_list = [1, 2, 3, 4, 5]

    serialize(sample_list, 'sample_list_json')
    deserialize('sample_list_json')

    serialize(sample_list, 'sample_list_pickle')
    deserialize('sample_list_pickle')

    serialize(sample_list, 'sample_list_dill')
    deserialize('sample_list_dill')

    # object
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    person_object = Person('Alice', 25)

    serialize(person_object, 'person_object_json')
    deserialize('person_object_json')

    serialize(person_object, 'person_object_pickle')
    deserialize('person_object_pickle')

    serialize(person_object, 'person_object_dill')
    deserialize('person_object_dill')

    # lambda function
    unserializable_object = lambda x: x + 1

    serialize(unserializable_object, 'unserializable_object_json')
    deserialize('unserializable_object_json')

    serialize(unserializable_object, 'unserializable_object_pickle')
    deserialize('unserializable_object_pickle')

    serialize(unserializable_object, 'unserializable_object_dill')
    deserialize('unserializable_object_dill')

# 2. დაწერე ჩაძირობანის თამაშის პროგრამა OOP_ის გამოყენებით.

import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.positions = []

    def place_ship(self, positions):
        if len(positions) == self.size and all(1 <= pos <= 10 for pos in positions):
            self.positions = positions
            return True
        else:
            return False

class Player:
    def __init__(self):
        self.ships = [Ship(size) for size in [1, 2, 3]]
        self.board = set()

    def place_ships(self):
        for ship in self.ships:
            while True:
                try:
                    positions = input(f"Enter positions for a {ship.size}-size ship (e.g., 1 2 3): ").split()
                    positions = [int(pos) for pos in positions]
                    if ship.place_ship(positions):
                        self.board.update(ship.positions)
                        break
                    else:
                        print("Invalid positions. Please try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter valid positions.")

class ComputerPlayer:
    def __init__(self):
        self.ships = [Ship(size) for size in [1, 2, 3]]
        self.board = set()

    def place_ships(self):
        for ship in self.ships:
            while True:
                positions = random.sample(range(1, 11), ship.size)
                if not any(set(positions).intersection(other_ship.positions) for other_ship in self.ships):
                    ship.positions = positions
                    self.board.update(ship.positions)
                    break

class Game:
    def __init__(self):
        self.player = Player()
        self.computer = ComputerPlayer()
        self.player_hits = set()
        self.computer_hits = set()
        self.winner = None

    def display_board(self):
        print("Your board:")
        for pos in range(1, 11):
            if pos in self.player.board:
                print("S", end=" ")
            else:
                print("O", end=" ")
        print("\nComputer's board:")
        for pos in range(1, 11):
            if pos in self.computer.board:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print("\n")

    def play_game(self):
        self.player.place_ships()
        self.computer.place_ships()

        while True:
            self.display_board()
            player_move = int(input("Enter your attack position (1-10): "))

            if player_move in self.computer.board:
                print("You hit a ship!")
                self.computer.board.remove(player_move)
                self.player_hits.add(player_move)
            else:
                print("You missed!")

            if not self.computer.board:
                self.winner = "Player"
                break

            computer_move = random.randint(1, 10)

            if computer_move in self.player.board:
                print("Computer hit your ship!")
                self.player.board.remove(computer_move)
                self.computer_hits.add(computer_move)
            else:
                print("Computer missed!")

            if not self.player.board:
                self.winner = "Computer"
                break

        self.display_board()
        print(f"{self.winner} wins!")

if __name__ == "__main__":
    game = Game()
    game.play_game()