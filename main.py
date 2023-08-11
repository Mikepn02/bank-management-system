from bank import Bank, create_table
from register import create_account
from login import validate_user, fetch_user_balance,fetch_user_info

def main():
    create_table()

    print("Welcome to the bank")

    while True:
        try:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = int(input("enter 1/2/3: "))

            if choice == 1:
                name = input("Enter your name: ")
                identity_number = input("Enter your identity number: ")
                pin = input("Enter your PIN: ")
                create_account(name, identity_number, pin)
            elif choice == 2:
                identity_number = input("Enter your identity number: ")
                pin = input("Enter your PIN: ")
                user = validate_user(identity_number, pin)

                if user:
                    user_balance = fetch_user_balance(identity_number)
                    account1 = Bank(user, identity_number, user_balance)

                    user_info = fetch_user_info(identity_number)

                    print(f"Welcome, {user_info['name']}!")
                    print(f"Identity Number: {identity_number}")
                    print(f"Account Balance: {user_balance}")
                    
                    while True:
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. request loan")
                        print("4. Exit")
                        choice = int(input("enter 1/2/3/4: "))
                        if choice == 1:
                            deposited = int(input("Enter the amount to deposit: "))
                            account1.deposit(deposited)
                        elif choice == 2:
                            withdrew = int(input("Enter the amount to withdraw: "))
                            account1.withdraw(withdrew)
                        elif choice == 3:
                            loan_amount = int(input("Enter the loan amouunt: "))
                            account1.request_loan(loan_amount)
                        elif choice == 4:
                            print("Logged out.")
                            break
                        else:
                            print("Invalid choice!")
                else:
                    print("Invalid identity number or PIN")
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
