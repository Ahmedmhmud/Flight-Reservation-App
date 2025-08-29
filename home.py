from tkinter import *
from booking import on_booking
from reservations import on_viewing

def on_home(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    lbl_welcome = Label(root, text="Welcome to FlySky Reservations ✈", fg="#841e1e", bg="#ffffff", font=("Arial", 26, "bold"))

    btn_book = Button(root, text="Book Flight", font=('Arial', 12, 'bold'), fg='white', bg="#af3528", activebackground='#c0392b', border=0, width=20, command=lambda: on_booking(root, on_home))

    btn_view = Button(root, text="View Reservations", font=('Arial', 12, 'bold'), fg='white', bg='#af3528', activebackground='#c0392b', border=0, width=20, command=lambda: on_viewing(root, on_home))

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    lbl_welcome.grid(row=0, column=0, columnspan=2, pady=200)
    btn_book.grid(row=1, column=0, padx=20, pady=20)
    btn_view.grid(row=1, column=1, padx=20, pady=20)
