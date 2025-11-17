import tkinter as tk
import subprocess
import os

def run_c_program():
    date = date_entry.get()
    desc = desc_entry.get()
    payed = payed_entry.get()

    # prepare the input
    input_text = f"{date}\n{desc}\n{payed}\n"

    # send the input to the c program
    subprocess.run(["main.exe"], input=input_text.encode())

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")
root.configure(bg = "black")
icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
root.iconbitmap(icon_path)

tk.Label(root, text="Date of purchase (DD/MM/YYYY):", fg="white", bg="black", font=("Courier New", 12)).grid(row=0, column=0)
date_entry = tk.Entry(root, width=40)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Description:", fg="white", bg="black", font=("Courier New", 12)).grid(row=1, column=0)
desc_entry = tk.Entry(root, width=40)
desc_entry.grid(row=1, column=1)

tk.Label(root, text="Amount paid:", fg="white", bg="black", font=("Courier New", 12)).grid(row=2, column=0)
payed_entry = tk.Entry(root, width=40)
payed_entry.grid(row=2, column=1)

tk.Button(root, text="Save Expense", command=run_c_program).grid(row=3, column=0, columnspan=2)

root.mainloop()