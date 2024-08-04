import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_descriptipn
import matplotlib.pyplot as plt
import tkinter as tk
from data_entry import get_amount, get_category, get_date, get_descriptipn
from tkinter import messagebox




class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)



    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["category"] == "Income"][
                "amount"
            ].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"][
                "amount"
            ].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_descriptipn()
    CSV.add_entry(date, amount, category, description)


def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

CSV.initialize_csv()

root = tk.Tk()
root.title("Finance Tracker")

# Labels
tk.Label(root, text="Date (dd-mm-yyyy)").grid(row=0, column=0)
tk.Label(root, text="Amount").grid(row=1, column=0)
tk.Label(root, text="Category").grid(row=2, column=0)
tk.Label(root, text="Description").grid(row=3, column=0)

# Entry fields
date_entry = tk.Entry(root)
amount_entry = tk.Entry(root)
category_entry = tk.Entry(root)
description_entry = tk.Entry(root)

date_entry.grid(row=0, column=1)
amount_entry.grid(row=1, column=1)
category_entry.grid(row=2, column=1)
description_entry.grid(row=3, column=1)

def add_entry():
    date = date_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()

    if not date or not amount or not category or not description:
        messagebox.showerror("Input Error", "All fields are required")
        return
    
    if category not in ["I", "E"]:
        messagebox.showerror("Input Error", "Category should be 'I' for Income or 'E' for Expense")
        return

    try:
        datetime.strptime(date, CSV.FORMAT)
    except ValueError:
        messagebox.showerror("Input Error", "Date format should be dd-mm-yyyy")
        return

    new_entry = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    df = pd.read_csv(CSV.CSV_FILE)
    new_entry_df = pd.DataFrame([new_entry])
    df = pd.concat([df, new_entry_df], ignore_index=True)  # Use pd.concat instead of append
    df.to_csv(CSV.CSV_FILE, index=False)
    messagebox.showinfo("Success", "Entry added successfully")

    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Add Button
tk.Button(root, text="Add Entry", command=add_entry).grid(row=4, column=0, columnspan=2)




if __name__ == "__main__":
    main()
    root.mainloop()
