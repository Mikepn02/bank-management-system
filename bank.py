import sqlite3
class Bank:
    def __init__(self,name,identity_number,amount): 
        self.name = name
        self.amount = amount
        self.identity_number = identity_number
    def deposit(self,deposit_amount):
        self.amount +=  deposit_amount
        print(f"The new balance is {self.amount}")
        self.update_balance()
    def withdraw(self,withdraw_amount):
         self.amount -= withdraw_amount
         print(f"The new balance is {self.amount}")
         self.update_balance()
    
    def update_balance(self):
     with sqlite3.connect('bank.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE bank_account SET balance=? WHERE identity_number=?", (self.amount,self.identity_number))
        conn.commit()
    


def create_table():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bank_account
                      (name TEXT PRIMARY KEY,identity_number TEXT,pin TEXT ,balance REAL)''')
    conn.commit()
    conn.close()