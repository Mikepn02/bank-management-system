import sqlite3
import bcrypt 
from register import hashed_password

def validate_user(identity_number , plain_pin):
    conn = sqlite3.connect('bank.db')
    cursor=conn.cursor()
    cursor.execute(f'''
            SELECT pin FROM bank_account WHERE identity_number="{identity_number}"''')
    hashed_pin = cursor.fetchone()
    conn.commit()
    conn.close()
    if hashed_pin:
        if bcrypt.checkpw(plain_pin.encode('utf-8'),hashed_pin[0]):
           return True
    return  False
def fetch_user_balance(identity_number):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f'''
            SELECT balance FROM bank_account WHERE identity_number="{identity_number}"''')
    balance = cursor.fetchone()
    conn.close()

    if balance:
        return balance[0]  # Return the balance value
    else:
        return 0  # Return 0 if no balance is found
def fetch_user_info(identity_number):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM bank_account WHERE identity_number = ?", (identity_number,))
    user_info = cursor.fetchone()
    conn.close()

    if user_info:
        return {'name': user_info[0]}  # Assuming the column index of name is 0
    else:
        return None