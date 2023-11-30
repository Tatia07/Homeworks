#დავალება
#ლექსიკონების დახმარებით შექმენი პითონში პროგრამა, რომელიც წარგიდგენს რესტორნის მენიუს. მიიღებს შეკვეთას.
#შექმნის ფაილს და ჩაწერს შეკვეთასა და მის ღირებულებას. პროგრამა გადააქციე exe ფაილად და დაუყენე რესტორნის სურათი.

from collections import defaultdict
import os

def display_menu(menu):
    print("მენიუ:")
    for i, (item, price) in enumerate(menu.items(), start=1):
        print(f"{i}. {item}: {price} ლარი")

def take_order(menu):
    total_price = 0
    order = defaultdict(int)

    while True:
        try:
            user_input = int(input("შეიყვანეთ პროდუქტის ნომერი(0 ნიშნავს შეკვეთის დასრულებას): "))

            if user_input == 0:
                print("შეკვეთა დასრულებულია")
                break
            elif user_input in range(1, len(menu) + 1):
                product_ordered = list(menu.keys())[user_input - 1]
                quantity = int(input("შეიყვანეთ რაოდენობა: "))

                order[product_ordered] += quantity
                total_price += quantity * menu[product_ordered]
        except ValueError:
            print("შეიყვანეთ სწორი რიცხვი!")

    return order, total_price

def write_order_to_file(order, total_price, filename):
    with open(filename, "w", encoding="utf-8") as order_file:
        order_file.write("შეკვეთა:\n")
        for key, value in order.items():
            order_file.write(f"{key} - რაოდენობა: {value}, ღირებულება: {value * menu[key]:.2f} ლარი\n")

        order_file.write("\nჯამში გადასახდელია: {:.2f} ლარი".format(total_price))
        order_file.write("\nგემრიელად მიირთვით!")


    print(f"\nშეკვეთის დეტალები იხილეთ - {filename}")

menu = {
    'ხინკალი': 0.7, 'მწვადი': 6, 'ლობიანი': 5, 'ხაჭაპური': 8, 'კარტოფილი ფრი': 4, 'ბურგერი': 9, 'შემწვარი ქათამი': 12, 'პიცა': 15,
    'წყალი': 1, 'კოკა-კოლა': 3, 'ფორთოხლის წვენი': 6, 'ლიმონათი': 3
}

display_menu(menu)
order, total_price = take_order(menu)
order_filename = "order_details.txt"
write_order_to_file(order, total_price, order_filename)
