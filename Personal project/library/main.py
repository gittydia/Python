import mysql.connector

connection = mysql.connector.connect(
    host="your_localhost",
    user="yourroot",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

def add_books(cursor, title, author, rates ):#finish debugging
    sql = "INSERT INTO books (title, author, rates) VALUES (%s, %s, %s)"
    val = (title, author, rates)
    cursor.execute(sql, val)
    print("Record inserted.")



def all_books(cursor):
    sql = "SELECT * FROM books"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print("book_number: ", row[0])
        print("author: ", row[1])
        print("title: ", row[2])
        print("rates: ", row[4])
        print("----------------------")


def menu():
    while True:
        print("1. Add Book")
        print("2. View books")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            rates = float(input("Enter rates: "))
            add_books(cursor, title, author, rates)
            connection.commit()
            print("Book added successfully")



        elif choice == '2':
            all_books(cursor)

        elif choice == '3':
            break

        else:
            print("Invalid choice")


if __name__ == '__main__':
    menu()
    cursor.close()
    connection.close()
