# 1.დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).

# from random import randint

# numbers = []

# for i in range(10):
#     num = randint(1, 50)
#     numbers.append(num)

# print(numbers)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# 2.დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).

# from random import randint

# numbers = []

# for i in range(10):
#     num = randint(1, 50)
#     numbers.append(num)

# print(numbers)
# sorted_numbers = sorted(numbers, reverse = True)
# print(sorted_numbers)

# 3.დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით 
# (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე
# (1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.

# import random
# from time import time

# def show_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         func(*args, **kwargs)
#         end_time = time()
#         return end_time - start_time
#     return wrapper

# def bubble_sort(numbers):
#     n = len(numbers)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# def selection_sort(numbers):
#     n = len(numbers)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if numbers[j] < numbers[min_idx]:
#                 min_idx = j
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

# def generate_and_sort_list(length, method):
#     numbers = [random.randint(1, length) for _ in range(length)]
#     sorting_method = bubble_sort if method == "Bubble" else selection_sort

#     sorting_time = show_time(sorting_method)(numbers)
#     print(f"{method} sorted {length} items list took {sorting_time:.6f} seconds")


# generate_and_sort_list(1000, "Bubble")
# generate_and_sort_list(1000, "Selection")

# generate_and_sort_list(2000, "Bubble")
# generate_and_sort_list(2000, "Selection")

# generate_and_sort_list(3000, "Bubble")
# generate_and_sort_list(3000, "Selection")
