import random

confirmed_friends = []
friends_dict = {}

try:
    num_friends = int(input("Enter the number of friends joining"
                            " (including you):\n"))
except ValueError:
    print("\nNo one is joining for the party")
else:
    if num_friends >= 1:
        print("\nEnter the name of every friend"
              " (including you), each on a new line:")

        for num in range(num_friends):
            confirmed_friends.append(input())

        bill = int(input("\nEnter the total bill value:\n"))

        if input('\nDo you want to use the "Who is lucky?"'
                 ' feature? Write Yes/No:\n').lower() == "yes":
            lucky_one = random.choice(confirmed_friends)
            print()
            print(lucky_one, "is the lucky one!")
            confirmed_friends.remove(lucky_one)
            total = round(bill / (num_friends - 1), 2)
            friends_dict = dict.fromkeys(confirmed_friends, total)
            friends_dict[lucky_one] = 0
            print()
            print(friends_dict)
        else:
            print("\nNo one is going to be lucky")
            total = round(bill / num_friends, 2)
            friends_dict = dict.fromkeys(confirmed_friends, total)
            print()
            print(friends_dict)
    else:
        print("\nNo one is joining for the party")
