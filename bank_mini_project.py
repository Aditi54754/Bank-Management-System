import random
import string
accounts = []
def create_account():
    name = input("Enter your name:")
    address = input("Enter your address:")
    amount=int(input("Enter Your starting deposite amount:"))
    accn_len = 4
    account_no = ""
    for i in range(accn_len):
        account_no = account_no + random.choice(string.digits)
    print("Your Account no is:",account_no)

    account={
        "name" : name,
        "address" : address,
        "amount" : amount,
        "account_no" : account_no
    }

    accounts.append(account)
    print("Account is created successfully...")


def view_account():
    if not accounts:
        print("No Account found!!")
        return
    for a in accounts:
        print(a)

def search_account():
    account_no = input("Enter your account no:")
    for a in accounts:
        if a["account_no"] == account_no:
            print("The account details is:",a)
            return
    print("Account not Found!!!")

def deposite_amount():
    account_no = input("enter your account no:")
    for a in accounts:
        if a["account_no"] == account_no:
         entered_amount = int(input("Enter a amount You want to deposite:"))
         a["amount"]= a["amount"] + entered_ammount
         print("Amount Deposited successfully....")
         
        

def withdraw_amount():
    account_no = input("enter your account no:")
    for a in accounts:
        if a["account_no"] == account_no:
            your_amount = int(input("Enter a ammount You want to withdraw:"))
            if your_amount > a["amount"]:
                    print("Insufficient balance!\n")
            else: 
                a["amount"] = a["amount"] - your_amount
                print("Amount withdrawing successfully....")
                print("Your Current Balance is:",a["amount"])

while True:
    print("1.Create Account")
    print("2.View All Account")
    print("3.Search Account")
    print("4.Deposite Money")
    print("5.Withdraw Money")
    print("6.Exit")

    choice = input("Enter your Choice:")

    if choice == '1':
        create_account()
    elif choice == '2':
        view_account()
    elif choice == '3':
        search_account()
    elif choice == '4':
        deposite_amount()
    elif choice == '5':
        withdraw_amount()
    elif choice == '6':
        break
    else:
        print("Invalid Choice!!!")


    


    

