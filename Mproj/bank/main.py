import sqlite3 as sql

#function that will be added
# debit card, graph, admin
# added features
# date and time,


class Bank:

    def __init__(self, name, balance, password, email):
        self.name = name
        self.balance = balance
        self.password = password
        self.email = email

    def deposit(self, amount):
        self.balance += amount
        self.update_balance(self.balance)


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient balance')

    def show_balance(self):
        print(f'Balance: {self.balance}')

    def show_details(self):
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')


    def login(self, password, email):
        connection = sql.connect('bank.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM bank WHERE email=? AND password=?', (email, password))
        result = cursor.fetchall()

        if result:
            for row in result:
                self.name = row[0]
                self.balance = row[1]
                self.password = row[2]
                self.email = row[3]
                print('Login successful')
        else:
            print('Invalid email or password')

        connection.commit()
        connection.close()

    def update_balance(self, new_balance):
        connection = sql.connect('bank.db')
        cursor = connection.cursor()
        
        cursor.execute('UPDATE bank SET balance = ? WHERE email = ?', (new_balance, self.email))
        
        connection.commit()
        connection.close()
        print('Balance updated successfully')




    def register(self):
        connection = sql.connect('bank.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS bank (name TEXT, balance REAL, password TEXT, email TEXT)')
        result = cursor.fetchall()

        if result:
            print('Account already exists')
        else:
            cursor.execute('INSERT INTO bank VALUES (?, ?, ?, ?)', (self.name, self.balance, self.password, self.email))
            print('Account created successfully')

        connection.commit()
        connection.close()



    def menuloggedin(self):
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Show balance")
                        print("4. Show details")
                        print("5. Exit")
                        choice = input("Enter your choice: ")
                        if choice == '1':
                            amount = float(input('Enter amount: '))
                            self.deposit(amount)
                            print('Amount deposited successfully')
                            return self.menuloggedin()
               
                        elif choice == '2':
                            amount = float(input('Enter amount: '))
                            self.withdraw(amount)
                            print('Amount withdrawn successfully')
                            return self.menuloggedin()
                            
                        elif choice == '3':
                            self.show_balance()
                            return self.menuloggedin()
                            
                        elif choice == '4':
                            self.show_details()
                            return self.menuloggedin()
                              
                        elif choice == '5':
                            self.menu()



    def menu(self):
        while True:
            print("-----------------------------------------------------")
            print("------------------BANK REGISTRAR---------------------")
            print("----------------Enter your choice--------------------")
            print("-----------------------------------------------------")
            print("---------1. login------------------------------------")
            print("---------2. create account---------------------------")
            print("---------3. Exit-------------------------------------")
            choice = input("Enter your choice: ")

            if choice == '1':
                email = input('Enter your email: ')
                password = input('Enter your password: ')
                self.login(password, email)
                if self.email == email and self.password == password:
                    self.menuloggedin()
                    return self.menuloggedin()

                    
            elif choice == '2':
                self.name = input('Enter your name: ')
                self.email = input('Enter your email: ')
                self.password = input('Enter your password: ')
                self.register()
                return self.menu()

            elif choice == '3':
                break

            else:
                print("Invalid choice")
                return self.menu()
    


if __name__ == '__main__':
    bank = Bank(name= '', balance= 0.0 , password= '', email= '')
    bank.menu()