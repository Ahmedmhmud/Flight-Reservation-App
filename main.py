from tkinter import *
from home import on_home
from database import init_db

root = Tk()

def main():
    # Set up the main window properties
    root.title("FlySky Reservations")
    root.configure(bg="#ffffff")
    root.state('zoomed')
    init_db()
    on_home(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()
