from tkinter import *
from booking import on_booking
from tkinter import ttk, messagebox
import sqlite3
from edit_reservation import edit_reservation, delete_reservation


def on_viewing(root, home_callback):
    for widget in root.winfo_children():
        widget.destroy()
    
    lbl_title = Label(root, text="Your Reservations", font=("Arial", 26, "bold"))
    lbl_title.grid(row=0, column=0, columnspan=3, pady=10)

    btn_book = Button(root, text="Book a new Flight", font=('Arial', 12, 'bold'),
                      fg='white', bg="#af3528", activebackground='#c0392b',
                      border=0, width=20, 
                      command=lambda: on_booking(root, home_callback))
    btn_book.grid(row=3, column=0, padx=20, pady=10, sticky='w')

    btn_back = Button(root, text="Back", font=('Arial', 12, 'bold'),
                      fg='white', bg="#af3528", activebackground='#c0392b',
                      border=0, width=20,
                      command=lambda: home_callback(root))
    btn_back.grid(row=3, column=2, padx=20, pady=10, sticky='e')

    tree = ttk.Treeview(root, columns=("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"), show='headings')
    for col in ("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"):
        tree.heading(col, text=col)
    
    tree.column("ID", width=50)
    tree.column("Name", width=150)
    tree.column("Flight Number", width=100)
    tree.column("Departure", width=100)
    tree.column("Destination", width=100)
    tree.column("Date", width=100)
    tree.column("Seat Number", width=100)
    tree.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky='nsew')

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    try:
        with sqlite3.connect('flights.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights")
            reservations = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        reservations = []

    for res in reservations:
        tree.insert("", "end", values=res)

    def on_edit():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a reservation to edit.")
            return
        res_values = tree.item(selected[0], "values")
        res_id, name, flight, dep, dest, date, seat = res_values

        edit_win = Toplevel(root)
        edit_win.title("Edit Reservation")
        edit_win.geometry("600x600")

        Label(edit_win, text="Name").pack(pady=5)
        entry_name = Entry(edit_win)
        entry_name.insert(0, name)
        entry_name.pack(pady=5)

        Label(edit_win, text="Flight Number").pack(pady=5)
        entry_flight = Entry(edit_win)
        entry_flight.insert(0, flight)
        entry_flight.pack(pady=5)

        Label(edit_win, text="Departure").pack(pady=5)
        entry_dep = Entry(edit_win)
        entry_dep.insert(0, dep)
        entry_dep.pack(pady=5)

        Label(edit_win, text="Destination").pack(pady=5)
        entry_dest = Entry(edit_win)
        entry_dest.insert(0, dest)
        entry_dest.pack(pady=5)

        Label(edit_win, text="Date").pack(pady=5)
        entry_date = Entry(edit_win)
        entry_date.insert(0, date)
        entry_date.pack(pady=5)

        Label(edit_win, text="Seat Number").pack(pady=5)
        entry_seat = Entry(edit_win)
        entry_seat.insert(0, seat)
        entry_seat.pack(pady=5)

        def save_changes():
            new_name = entry_name.get()
            new_flight = entry_flight.get()
            new_dep = entry_dep.get()
            new_dest = entry_dest.get()
            new_date = entry_date.get()
            new_seat = entry_seat.get()
            edit_reservation(res_id, new_name, new_flight, new_dep, new_dest, new_date, new_seat)
            edit_win.destroy()
            on_viewing(root, home_callback)

        Button(edit_win, text="Save Changes", command=save_changes,
               fg='white', bg="#ae2727", width=20).pack(pady=20)

    def on_delete():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a reservation to delete.")
            return
        res_values = tree.item(selected[0], "values")
        res_id = res_values[0]

        confirm = messagebox.askyesno("Delete Reservation", f"Are you sure you want to delete reservation {res_id}?")
        if confirm:
            delete_reservation(res_id)
            on_viewing(root, home_callback)

    btn_edit = Button(root, text="Edit Reservation", font=('Arial', 12, 'bold'),
                      fg='white', bg="#af3528", activebackground='#c0392b',
                      border=0, width=20, command=on_edit)
    btn_edit.grid(row=2, column=0, padx=20, pady=10, sticky='w')

    btn_delete = Button(root, text="Delete Reservation", font=('Arial', 12, 'bold'),
                        fg='white', bg="#af3528", activebackground='#c0392b',
                        border=0, width=20, command=on_delete)
    btn_delete.grid(row=2, column=2, padx=20, pady=10, sticky='e')
