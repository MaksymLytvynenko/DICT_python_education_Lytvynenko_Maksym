"""" ChatBot project """

# information about ChatBot
print("Hello! My name is DICT_Bot.")
print("I was created in 2023.")

# input user's name
print("Please, remind me your name.")
your_name = input()
print("What a great name you have,", your_name)

# guess the user's age
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "; that's a good time to start programming!")

# count a number
print("Now I will prove to you that I can count to any number you want.")
user_number = int(input())
for i in range(0, user_number + 1):
    print(i, "!")

# test user's programming knowledge
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# input user's answer
while True:
    user_answer = int(input())
    if user_answer == 2:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again")
