# 1.შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * 3.14159 * self.radius 
        return perimeter

    def calculate_area(self):
        area = 3.14159 * (self.radius ** 2)
        return area

user_input = int(input('Enter the value of radius: '))
circle = Circle(user_input)

perimeter_result = circle.calculate_perimeter()
area_result = circle.calculate_area()

print(f"Perimeter: {perimeter_result}")
print(f"Area: {area_result}")

# 2.შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

calculator = Calculator()

result_add = calculator.add(15, 3)
result_subtract = calculator.subtract(81, 2)
result_multiply = calculator.multiply(48, 6)
result_divide = calculator.divide(100, 2)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")

# 3.შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები სასურველი ნივთის დასამატებლად და ამოსაშლელად, ასევე კალათაში არსებული 
# პროდუქტების სიისა და ჯამური ღირებულების გამოსატანად.
 
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity, price_per_unit):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'quantity': quantity, 'price_per_unit': price_per_unit}

    def remove_item(self, item, quantity):
        if item in self.items:
            if quantity >= self.items[item]['quantity']:
                del self.items[item]
            else:
                self.items[item]['quantity'] -= quantity

    def get_items(self):
        return self.items

    def calculate_total_cost(self):
        total_cost = 0
        for item, details in self.items.items():
            total_cost += details['quantity'] * details['price_per_unit']
        return total_cost

cart = ShoppingCart()

cart.add_item("Apples", 3, 1.5)
cart.add_item("Bananas", 2, 0.75)

current_items = cart.get_items()
print("Current items in the cart:")
for item, details in current_items.items():
    print(f"{item}: {details['quantity']} at ${details['price_per_unit']} each")

total_cost = cart.calculate_total_cost()
print(f"\nTotal cost: ${total_cost}")

cart.remove_item("Apples", 2)

updated_items = cart.get_items()
print("\nUpdated items in the cart:")
for item, details in updated_items.items():
    print(f"{item}: {details['quantity']} at ${details['price_per_unit']} each")

updated_total_cost = cart.calculate_total_cost()
print(f"\nUpdated total cost: ${updated_total_cost}")

# 4.შექმენი საბანკო ანგარიშის კლასი, თანხის შეტანის, გამოტანის და გადარიცხვის მეთოდებით.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."

    def transfer(self, recipient_account, amount):
        withdrawal_result = self.withdraw(amount)
        if "successful" in withdrawal_result:
            recipient_account.deposit(amount)
            return f"Transfer of ${amount} to {recipient_account.account_holder} successful. New balance: ${self.balance}"
        else:
            return f"Transfer failed: {withdrawal_result}"


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(account1.deposit(200))

print(account1.withdraw(150))

print(account1.transfer(account2, 100))

print(f"\n{account1.account_holder}'s final balance: ${account1.balance}")
print(f"{account2.account_holder}'s final balance: ${account2.balance}")
