"""Dinner-party"""

import random


def calculate_total_amount(total_amount, user_input, lucky_mode=False):
    """
    Calculate the amount per person

    Parameters:
    total_amount (float): the total amount
    user_input (int): the number of people
    lucky_mode (optional): activate lucky mode

    Returns:
        float: the amount per person
    """
    if lucky_mode:
        return round(total_amount / (user_input - 1), 2)
    else:
        return round(total_amount / user_input, 2)


def find_lucky_one(num_friends):
    """
    Choose a random person to be the lucky one

    Parameters:
    num_friends (dict): contain the names of friends

    Returns:
        str: the name of the lucky person
    """
    lucky_one = random.choice(list(num_friends))
    return lucky_one


user_input = int(input("Enter the number of friends joining (including you):\n"))

num_friends = {}

if user_input <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(user_input):
        friends_name = input()
        num_friends[friends_name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if choice.lower() == "yes":
        lucky_one = find_lucky_one(num_friends)
        print(f"{lucky_one} is the lucky one!")

        per_person = calculate_total_amount(total_amount, user_input, lucky_mode=True)
        num_friends[lucky_one] = 0

        for friend in num_friends:
            if friend != lucky_one:
                num_friends[friend] = per_person

    else:
        print("No one is going to be lucky")
        per_person = calculate_total_amount(total_amount, user_input)

        for friend in num_friends:
            num_friends[friend] = per_person

    print(num_friends)
