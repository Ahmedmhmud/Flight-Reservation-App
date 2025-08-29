import sqlite3

def init_db():
    create_table = """
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        );
    """

    with sqlite3.connect('flights.db') as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(create_table)
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")