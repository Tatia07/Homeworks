# პირველი დავალება

# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?”
# სავარაუდო პასუხები: 
# 1.	შუმერთა 
# 2.	სელჩუკთა 
# 3.	რომის 
# 4.	მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი. 
# შეცდომის შემთხვევაში იბეჭდება: „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება: „სწორია!“

print("რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?")
print("1.შუმერთა 2.სელჩუკთა 3.რომის 4.მონღოლთა")

answer = str(input("შეიყვანეთ პასუხი : "))

if answer == "რომის" or answer == "3" or answer == "3.რომის":
    print("სწორია!")
else:
    print("არა! სწორი პასუხია რომის!")


# მეორე დავალება

# 2. ონლაინ მაღაზია
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას. 
# მაგ. 
# 1.	ლეპტოპები
# 2.	პერსონალური კომპიუტერები
# 3.	მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.
# პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში. 
# (თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს)
# თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში არ გააჩნია შემოთავაზება.

choice = str(input("აირჩიეთ ერთ-ერთი კატეგორია : ლეპტოპი, პერსონალური კომპიუტერი, მობილური."))
budget = int(input("შეიყვანეთ მაქსიმალური ბიუჯეტი : "))

if choice == "ლეპტოპი":
    if budget >= 1500:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Lenovo Ideapad Slim3")
    elif budget >= 1000 and budget < 1500:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Lenovo 82C600LURU")
    elif budget >= 500 and budget < 1000:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Lenovo Thinkpad")
    else:
        print("სამწუხაროდ ამ თანხაში შემოთავაზება არ გვაქვს.")

elif choice == "პერსონალური კომპიუტერი":
    if budget >= 1500:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- HP Desktop PC Intel Core")
    elif budget >= 1000 and budget < 1500:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- HP 22 All-in-one AMD 3050U")
    elif budget >= 500 and budget < 1000:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Acer 31.5 ED320Q")
    else:
        print("სამწუხაროდ ამ თანხაში შემოთავაზება არ გვაქვს.")

elif choice == "მობილური":
    if budget >= 1500:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Samsung Galaxy s23")
    elif budget >= 1000 and budget < 1500:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Samsung Galaxy Z flip")
    elif budget >= 500 and budget < 1000:
        print("ჩვენ ამ თანხაში შეგვიძლია შემოგთავაზოთ- Samsung Galaxy A50")
    else:
        print("სამწუხაროდ ამ თანხაში შემოთავაზება არ გვაქვს.")
        
else:
    print("არჩევა შესაძლებელია მხოლოდ ამ სამი კატეგორიიდან!")


# მესამე დავალება

# 3. შტორმი 
# პილოტი შტორმში მოხვდა და ვერ შეძლო აეროპორტში დროული დაშვება. საწვავის რაოდენობა შეზღუდულია. პილოტს სჭირდება კომპიუტერის დახმარება. 
# შექმენი პროგრამა, რომელიც მოითხოვს პილოტისგან დარჩენილი საწვავის რაოდენობას (ლიტრებში) და მიაწოდებს ინფორმაციას იმ ქალაქების აეროპორტების შესახებ, რომლამდე მიღწევაც შესაძლებელია. 
# ზემოაღნიშნული თვითმფრინავი ხარჯავს 12 ლიტრ საავიაციო საწვავს 1 კილომეტრის მანძილის დაფარვისას.
# თვითმფრინავის ახლომდებარე სამი ქალაქია: 
# Zaragoza (50km) 
# Valencia (75 km)
# Madrid (100km)

# თუ თვითმფრინავს არ ჰყოფნის საწვავი არცერთ ქალაქამდე, 
# დაბეჭდე მესიჯი: „!ავარიული დაშვება!“

leftFuel = int(input("შეიყვანეთ დარჩენილი საწვავის რაოდენობა : "))


if leftFuel >= 50 * 12 and leftFuel < 75 * 12:
    print("დარჩენილი საწვავი ზარაგოზამდე ჩასასვლელად საკმარისია.(50კმ)")
elif leftFuel >= 75 * 12 and leftFuel < 100 * 12:
    print("დარჩენილი საწვავი ვალენსიამდე და ზარაგოზამდე ჩასასვლელად საკმარისია.(70კმ)")
elif leftFuel >= 100 * 12:
    print("დარჩენილი საწვავი მადრიდამდე, ვალენსიამდე და ზარაგოზამდე მისასვლელად საკმარისია.(100კმ)")
else:
    print("თქვენ არ გაქვთ საკმარისი საწვავი ზემოთხსენებულ ქალაქამდე მისასვლელად. ავარიული დაშვება!!")


# მეოთხე დავალება

# 4. მომხმარებლისთვის კარიერის შერჩევა
# პროგრამა უსვამს მომხმარებელს რამდენიმე კითხვას (თქვენი იმპროვიზაციით) და ურჩევს მისთვის შესაფერის პროფესიას.

print("Career Choosing Test")
print("This test will help you to understand if your career aligns with your interest and skills.")

choice = input("Please Select a career: 1.Software Developer, 2.Graphic Designer, 3.Teacher, 4.Accountant- ")

if choice.lower() == "software developer" or choice == "1":
    print("For each career, you will have to answer 4 questions. Please rate questions from 1 to 5. 1 is for the lowest interest and 5 is for the highest interest.")
    ans1 = int(input("1.How comfortable are you with programming languages (1-5)?"))
    ans2 = int(input("2.Do you enjoy problem-solving and logical thinking (1-5)?"))
    ans3 = int(input("3.Are you interested in staying updated with technology trends (1-5)?"))
    ans4 = int(input("4.How would you rate your attention to detail (1-5)?"))

    result = ans1 + ans2 + ans3 + ans4

    if result <= 6:
        print("This career doesn't seem too suitable for you, you should reconsider your desicion.")
    elif result > 6 and result <= 12:
        print(f"I suggest you should choose career which is close to {choice} or continue with this.")
    elif result > 12 and result <= 20:
        print("You have definitely chosen the right career for you! Don't give up!")

elif choice.lower() == "graphic designer" or choice == "2":
    print("For each career, you will have to answer 4 questions. Please rate questions from 1 to 5. 1 is for the lowest interest and 5 is for the highest interest.")
    ans1 = int(input("1.Do you have a creative mindset (1-5)?"))
    ans2 = int(input("2.Are you skilled in using design software like Adobe Creative Suite (1-5)?"))
    ans3 = int(input("3.Do you enjoy visual aesthetics and design principles (1-5)?"))
    ans4 = int(input("4.How good are you at taking feedback and revisions (1-5)?"))

    result = ans1 + ans2 + ans3 + ans4

    if result <= 6:
        print("This career doesn't seem too suitable for you, you should reconsider your desicion.")
    elif result > 6 and result <= 12:
        print(f"I suggest you should choose career which is close to {choice} or continue with this.")
    elif result > 12 and result <= 20:
        print("You have definitely chosen the right career for you! Don't give up!")

elif choice.lower() == "teacher" or choice == "3":
    print("For each career, you will have to answer 4 questions. Please rate questions from 1 to 5. 1 is for the lowest interest and 5 is for the highest interest.")
    ans1 = int(input("1.Do you enjoy working with children or young adults (1-5)?"))
    ans2 = int(input("2.Are you patient and good at explaining concepts (1-5)?"))
    ans3 = int(input("3.Are you interested in educational theory and methods (1-5)?"))
    ans4 = int(input("4.How comfortable are you with public speaking (1-5)?"))

    result = ans1 + ans2 + ans3 + ans4

    if result <= 6:
        print("This career doesn't seem too suitable for you, you should reconsider your desicion.")
    elif result > 6 and result <= 12:
        print(f"I suggest you should choose career which is close to {choice} or continue with this.")
    elif result > 12 and result <= 20:
        print("You have definitely chosen the right career for you! Don't give up!")

elif choice.lower() == "accountant" or choice == "4":
    print("For each career, you will have to answer 4 questions. Please rate questions from 1 to 5. 1 is for the lowest interest and 5 is for the highest interest.")
    ans1 = int(input("1.Are you detail-oriented and organized (1-5)?"))
    ans2 = int(input("2.Do you enjoy working with numbers and financial data (1-5)?"))
    ans3 = int(input("3.Are you comfortable using accounting software (1-5)?"))
    ans4 = int(input("4.How well can you handle financial regulations and compliance (1-5)?"))

    result = ans1 + ans2 + ans3 + ans4

    if result <= 6:
        print("This career doesn't seem too suitable for you, you should reconsider your desicion.")
    elif result > 6 and result <= 12:
        print(f"I suggest you should choose career which is close to {choice} or continue with this.")
    elif result > 12 and result <= 20:
        print("You have definitely chosen the right career for you! Don't give up!")

else:
    print("You must choose a career from the list")
