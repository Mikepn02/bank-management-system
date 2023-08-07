import sqlite3 
import bcrypt

def create_account(name, identity_number, pin):
    hashed_pin = hashed_password(pin)
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bank_account (name, identity_number, pin, balance) VALUES (?, ?, ?, ?)",
                   (name, identity_number, hashed_pin, 0))
    conn.commit()
    conn.close()


def hashed_password(plain_password): 
   salt = bcrypt.gensalt()
   hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'),salt)
   return hashed_password