import bcrypt
import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (username text PRIMARY KEY, password text)')
        hashed_password = self.password  # This is already a string
        cursor.execute('INSERT OR REPLACE INTO users VALUES (?, ?)', (self.username, hashed_password))
        connection.commit()
        connection.close()
        print("Account saved to database successfully!")

    
    def verify_password(self, plain_text_password, hashed_password):
        password_bytes = plain_text_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    #will make the usn unique
    def login(self):
        print("Enter your username: ")
        username = input()
        print("Enter your password: ")
        password = input()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        connection.close()
        if user:
            if self.verify_password(password, user[1]):
                print("Login successful!")
            else: 
                print("Invalid password")
        else:
            print("User does not exist")

    def create_account(self):
        print("Enter your username: ")
        username = input()
        print("Enter your password: ")
        password = input()
        print("Confirm your password: ")
        confirm_password = input()
        if password == confirm_password:
            self.username = username
            self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            print("Account created successfully!")
            return True
        else:
            print("Password does not match")
            return False
            
###
    def main(self):
        print("--------------------------------")
        print("Welcome to the login page")
        print("--------------------------------")
        print("1. Login")
        print("2. Create account")
        print("3. Exit")
        print("--------------------------------")
        option = input("Enter your option: ")
        if option == '1':
            self.login()
            return self.main()
        elif option == '2':
            if self.create_account():
                self.save_to_db()
                return self.main()
        elif option == '3':
            print("Exiting...")
        else:
            print("Invalid option")
            return self.main()


if __name__ == '__main__':
    user = User('', '')
    user.main()