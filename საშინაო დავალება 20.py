# 1.დაწერე პროგრამა, რომელიც მომხმარებლისგან მიიღებს რაიმე ტიპის ინფორმაციას, შეინახავს პითონის ლექსიკონში. შემდეგ შექმნის JSON_ის ფაილს და მასში დაასაწყობებს ამ ინფორმაციას.

import json

def get_user_info():
    user_info = {}

    user_info['name'] = input("Enter your name: ")
    user_info['age'] = input("Enter your age: ")
    user_info['email'] = input("Enter your email: ")

    return user_info

def save(data):
    with open('user_info.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    user_info = get_user_info()

    save(user_info)

    print("User information has been saved to user_info.json")

if __name__ == "__main__":
    main()

# 2.დაწერე კოდი, რომელიც წინა სავარჯიშოში შენახულ ინფორმაციას გაუკეთებს დესერიალიზაციას. ჩაასწორებს რაიმე პარამეტრს და დაარედაქტირებს JSON ფაილში ინფორმაციას.

import json

def get_user_info():
    user_info = {}

    user_info['name'] = input("Enter your name: ")
    user_info['age'] = input("Enter your age: ")
    user_info['email'] = input("Enter your email: ")

    return user_info

def save_to_json(data):
    with open('user_info.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def load_from_json():
    try:
        with open('user_info.json', 'r') as json_file:
            user_info = json.load(json_file)
        return user_info
    except FileNotFoundError:
        print("User info file not found. Please run the program to create it.")
        return None

def update_user_info():
    user_info = load_from_json()

    if user_info:
        print("Current User Information:")
        print(json.dumps(user_info, indent=4))

        key_to_update = input("Enter the parameter to update (name, age, email): ")
        if key_to_update in user_info:
            user_info[key_to_update] = input(f"Enter the new {key_to_update}: ")

            save_to_json(user_info)
            print("User information has been updated and saved.")
        else:
            print("Invalid parameter.")

def main():
    update_user_info()

if __name__ == "__main__":
    main()
