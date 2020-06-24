# Write your code here
import random


accounts = dict()


def get_checksum(num):
    numbers = list(map(int, num))
    for x in range(0,len(numbers),2):
        numbers[x] *= 2
    total = 0
    for i in range(len(numbers)):
        if numbers[i] > 9:
            total += numbers[i] - 9
        else:
            total += numbers[i]
    return str(10 - (total % 10))


def generate_number():
    while True:
        num = random.randint(0, 1000000000)
        acc = "400000" + str(num).zfill(9)
        checksum = get_checksum(acc)
        if checksum == "10":
            acc = acc + "0"
        else:
            acc = acc + checksum
        if len(accounts) == 0:
            return acc
        if acc not in accounts.keys():
            return acc


def generate_pin():
    num = random.randint(0, 10000)
    return str(num).zfill(4)


def create_account():
    print("Your card has been created")
    print("Your card number:")
    number = generate_number()
    print(number)
    print("Your card PIN:")
    pin = generate_pin()
    print(pin)
    accounts[number] = {}
    accounts[number]["PIN"] = pin
    accounts[number]["balance"] = 0
    return


def login():
    print("Enter your card number:")
    acc = input()
    print("Enter your PIN:")
    pin = input()

    if acc not in accounts.keys():
        print("Wrong card number or PIN!")
        return False
    if accounts[acc]["PIN"] == pin:
        print("You have successfully logged in!")
        return acc
    print("Wrong card number or PIN!")
    return False


def logged_in(acc):
    while True:
        print("1. Balance")
        print("2. Log out")
        print("0. Exit")

        choice = int(input())
        if choice == 1:
            print("Balance: {}".format(accounts[acc]["balance"]))
        elif choice == 2:
            print("You have successfully logged out!")
            return True
        elif choice == 0:
            print("Bye!")
            return False


while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    choice = int(input())
    if choice == 1:
        create_account()
    elif choice == 2:
        acc = login()
        if acc:
            if not logged_in(acc):
                break
    elif choice == 0:
        print("Bye!")
        break
