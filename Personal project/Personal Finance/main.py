import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, simpledialog




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


CSV.initialize_csv()

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Date (dd-mm-yyyy)").grid(row=0, column=0)
        tk.Label(self.root, text="Amount").grid(row=1, column=0)
        tk.Label(self.root, text="Category").grid(row=2, column=0)
        tk.Label(self.root, text="Description").grid(row=3, column=0)

        self.date_entry = tk.Entry(self.root)
        self.amount_entry = tk.Entry(self.root)
        self.category_entry = tk.Entry(self.root)
        self.description_entry = tk.Entry(self.root)

        self.date_entry.grid(row=0, column=1)
        self.amount_entry.grid(row=1, column=1)
        self.category_entry.grid(row=2, column=1)
        self.description_entry.grid(row=3, column=1)

        self.date_entry.config(width=30)
        self.amount_entry.config(width=30)
        self.category_entry.config(width=30)
        self.description_entry.config(width=30)

        self.root.rowconfigure(0, minsize=20)
        self.root.rowconfigure(1, minsize=20)
        self.root.rowconfigure(2, minsize=20)
        self.root.rowconfigure(3, minsize=20)
        self.root.rowconfigure(4, minsize=20)
        self.root.rowconfigure(5, minsize=20)

        tk.Button(self.root, text="Add Entry", command=self.add_entry).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Get Transactions", command=self.prompt_dates).grid(row=5, column=0, columnspan=2)

    def add_entry(self):
        date = self.date_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()

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
        df = pd.concat([df, new_entry_df], ignore_index=True)
        df.to_csv(CSV.CSV_FILE, index=False)
        messagebox.showinfo("Success", "Entry added successfully")

        self.date_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def prompt_dates(self):
        date_started = simpledialog.askstring("Input", "Enter the start date (dd-mm-yyyy):")
        date_finish_booked = simpledialog.askstring("Input", "Enter the end date (dd-mm-yyyy):")
        if date_started and date_finish_booked:
            self.get_transactions(date_started, date_finish_booked)

    def get_transactions(self, date_started, date_finish_booked):
        df = pd.read_csv(CSV.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        date_started = datetime.strptime(date_started, CSV.FORMAT)
        date_finish_booked = datetime.strptime(date_finish_booked, CSV.FORMAT)

        mask = (df["date"] >= date_started) & (df["date"] <= date_finish_booked)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            messagebox.showinfo("No Transactions", "No transactions found in the given date range.")
        else:
            total_income = filtered_df[filtered_df["category"] == "I"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "E"]["amount"].sum()
            net_savings = total_income - total_expense

            messagebox.showinfo("Transactions", filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            messagebox.showinfo("Summary", f"Total Income: ${total_income:.2f}\nTotal Expense: ${total_expense:.2f}\nNet Savings: ${net_savings:.2f}")
    
            

        if messagebox.askyesno("Plot", "Do you want to see a plot?"):
            self.plot_transactions(filtered_df)

            #self.plot_transactions(filtered_df)

        return filtered_df
    
    def plot_transactions(self, df):
        df.set_index("date", inplace=True)

        income_df = df[df["category"] == "I"]
        expense_df = df[df["category"] == "E"]


        plt.figure(figsize=(10, 5))
        plt.plot(income_df.index, income_df["amount"], label="Income", color="g", marker="o")
        plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r", marker="o")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income and Expenses Over Time")
        plt.legend()
        plt.grid(True)
        plt.show()

       

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("400x300")
root.resizable(False, False)

app = FinanceTracker(root)



if __name__ == "__main__":
    root.mainloop()
