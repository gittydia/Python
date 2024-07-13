import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def calculate_gwa(subject_entries, unit_entries):
    try:
        total_units = 0
        total_weighted_grades = 0
        for i in range(len(subject_entries)):
            grade = float(subject_entries[i].get())
            units = float(unit_entries[i].get())
            total_units += units
            total_weighted_grades += grade * units
        gwa = total_weighted_grades / total_units
        result_label.configure(text=f"GWA: {gwa:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for grades and units.")

root = ctk.CTk()
root.title("GWA Calculator")
root.geometry("600x400")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


subject_entries = []
unit_entries = []

for i in range(5):
    subject_label = ctk.CTkLabel(root, text=f"Subject {i + 1} Grade:")
    subject_label.grid(row=i, column=0, padx=10, pady=5)
    subject_entry = ctk.CTkEntry(root)
    subject_entry.grid(row=i, column=1, padx=10, pady=5)
    subject_entries.append(subject_entry)

    unit_label = ctk.CTkLabel(root, text=f"Subject {i + 1} Units:")
    unit_label.grid(row=i, column=2, padx=10, pady=5)
    unit_entry = ctk.CTkEntry(root)
    unit_entry.grid(row=i, column=3, padx=10, pady=5)
    unit_entries.append(unit_entry)

def add_subject():
    i = len(subject_entries)
    subject_label = ctk.CTkLabel(root, text=f"Subject {i + 1} Grade:")
    subject_label.grid(row=i, column=0, padx=10, pady=5)
    subject_entry = ctk.CTkEntry(root)
    subject_entry.grid(row=i, column=1, padx=10, pady=5)
    subject_entries.append(subject_entry)

    unit_label = ctk.CTkLabel(root, text=f"Subject {i + 1} Units:")
    unit_label.grid(row=i, column=2, padx=10, pady=5)
    unit_entry = ctk.CTkEntry(root)
    unit_entry.grid(row=i, column=3, padx=10, pady=5)
    unit_entries.append(unit_entry)

def remove_subject():
    if subject_entries:
        subject_entry = subject_entries.pop()
        subject_entry.destroy()
    if unit_entries:
        unit_entry = unit_entries.pop()
        unit_entry.destroy()

add_button = ctk.CTkButton(root, text="Add Subject", command=add_subject)
add_button.grid(row=0, column=4, padx=10, pady=5)

remove_button = ctk.CTkButton(root, text="Remove Subject", command=remove_subject)
remove_button.grid(row=1, column=4, padx=10, pady=5)

calculate_button = ctk.CTkButton(root, text="Calculate GWA", command=lambda: calculate_gwa(subject_entries, unit_entries))
calculate_button.grid(row=2, column=4, padx=10, pady=5)

result_label = ctk.CTkLabel(root, text="GWA: ")
result_label.grid(row=3, column=4, padx=10, pady=5)

root.mainloop()
