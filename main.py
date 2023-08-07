
from bank import Bank,create_table
from register import create_account 
from login  import validate_user , fetch_user_balance

def main():
    create_table()

    print("Welcome to the bank")

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice =int(input("enter 1/2/3/4: "))
        if choice == 1 :
            name = input("Enter your name: ")
            identity_number = input("Enter your identity number: ")
            pin = input("Enter your PIN: ")
            create_account(name,identity_number,pin)
        elif choice == 2:
            identity_number = input("Enter your identity number: ")
            pin = input("Enter your PIN: ")
            # user=validate_user(identity_number)
            user = validate_user(identity_number,pin)

            print(user)

            if user:
                # print(f"Welcome, {user[0]}!")
                user_balance = fetch_user_balance(identity_number)
                account1 = Bank(user,identity_number,user_balance)
                while True:
                    print("1. Deposit")
                    print("2. withdraw")
                    print("3. Exit")
                    choice =int(input("enter 1/2/3/4: "))
                    if choice == 1 :
                        deposited = int(input("Enter the amount to deposit: "))
                        account1.deposit(deposited)
                    elif choice == 2:
                        withdrew = int(input("Enter the amount to withdraw: "))
                        account1.withdraw(withdrew)

                    elif choice == 3:
                        print("logged out.")
                        break
                    else:
                        print("Invalid choise!!!")
            else: 
                print("Invalid identity_number or PIN")
        elif choice == 3:
            print("Good Bye!!")
            break
            
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()