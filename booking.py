from tkinter import *
import sqlite3
from tkinter import messagebox

def on_booking(root, home_callback):
    for widget in root.winfo_children():
        widget.destroy()

    lbl_title = Label(root, text="Book a Flight", font=("Arial", 26, "bold"))

    lbl_fname = Label(root, text="Full Name", font=('Arial', 12))
    ent_fname = Entry(root, font=('Arial', 12), width=30)

    lbl_flight = Label(root, text="Flight Number", font=('Arial', 12))
    ent_flight = Entry(root, font=('Arial', 12), width=30)

    lbl_departure = Label(root, text="Departure", font=('Arial', 12))
    ent_departure = Entry(root, font=('Arial', 12), width=30)

    lbl_destination = Label(root, text="Destination", font=('Arial', 12))
    ent_destination = Entry(root, font=('Arial', 12), width=30)

    lbl_date = Label(root, text="Booking Date (YYYY-MM-DD)", font=('Arial', 12))
    ent_date = Entry(root, font=('Arial', 12), width=30)

    lbl_seat = Label(root, text="Seat Number", font=('Arial', 12))
    ent_seat = Entry(root, font=('Arial', 12), width=30)

    def on_book():
        # steps: 
        # 0. validate entries
        if not all([ent_fname.get(), ent_flight.get(), ent_departure.get(), ent_destination.get(), ent_date.get(), ent_seat.get()]):
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        # 1. insert data in the entries into database
        insert_command_line = """
            INSERT INTO flights (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?); """
        
        with sqlite3.connect('flights.db') as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(insert_command_line, (
                    ent_fname.get(),
                    ent_flight.get(),
                    ent_departure.get(),
                    ent_destination.get(),
                    ent_date.get(),
                    ent_seat.get()
                ))
                conn.commit()
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
        # 2. back to home screen
        home_callback(root)
        

    btn_book = Button(root, text="Book Now", font=('Arial', 12, 'bold'), fg='white', bg="#af3528", activebackground='#c0392b', border=0, width=20, command=on_book)
    btn_cancel = Button(root, text="Cancel", font=('Arial', 12, 'bold'), fg='white', bg="#af3528", activebackground='#c0392b', border=0, width=20, command=lambda: home_callback(root))

    lbl_title.grid(row=0, column=0, columnspan=2, pady=20)

    lbl_fname.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 0))
    ent_fname.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 10))

    lbl_flight.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 0))
    ent_flight.grid(row=4, column=0, columnspan=2, padx=20, pady=(0, 10))

    lbl_departure.grid(row=5, column=0, padx=20, pady=(10, 0))
    lbl_destination.grid(row=5, column=1, padx=20, pady=(10, 0))
    ent_departure.grid(row=6, column=0, padx=20, pady=(0, 10))
    ent_destination.grid(row=6, column=1, padx=20, pady=(0, 10))

    lbl_date.grid(row=7, column=0, padx=20, pady=(10, 0))
    lbl_seat.grid(row=7, column=1, padx=20, pady=(10, 0))
    ent_date.grid(row=8, column=0, padx=20, pady=(0, 10))
    ent_seat.grid(row=8, column=1, padx=20, pady=(0, 10))

    btn_book.grid(row=9, column=0, padx=20, pady=20)
    btn_cancel.grid(row=9, column=1, padx=20, pady=20)