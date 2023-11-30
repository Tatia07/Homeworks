# პირველი დავალება
# 1.მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი, ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში. 
# შედეგი დაბეჭდე. გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები. 

# text = input("Enter a sentence: ")
# letter_count = 0
# digit_count = 0
# other_count = 0

# for char in text:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     else:
#         other_count += 1

# print("Number of letters:", letter_count)
# print("Number of digits:", digit_count)
# print("Number of other symbols:", other_count)

# მეორე დავალება
# 2.მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე შემდეგ წესებზე დაყრდნობით. შექმნილი წინადადება უნდა იწყებოდეს 
# პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვება მეორე წინადადების ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების მეორე სიმბოლო
# და მეორე წინადადების ბოლოდან მეორე სიმბოლო.

# first = input("Enter a word: ")
# second = input("Enter a word: ")

# third = first[0] + second[-1] + first[1] + second[-2]

# print("The created word is:", third)

# მესამე დავალება
# 3.მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე წინადადებაში და პირიქით, 
# მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის პირველ წინადადებაში. თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე: „Strings are balanced!“
# თუ რომელიმე პირობა დაირღვა, დაბეჭდე: „Strings are not balanced!“

# first_sentence = input("Enter the first sentence: ")
# second_sentence = input("Enter the second sentence: ")

# first = set(first_sentence)
# second = set(second_sentence)

# if first.issubset(second) and second.issubset(first):
#     print("Strings are balanced!")
# else:
#     print("Strings are not balanced!")