import sqlite3

def edit_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
    update_command = """
        UPDATE flights
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?;
    """
    try:
        with sqlite3.connect('flights.db') as conn:
            cursor = conn.cursor()
            cursor.execute(update_command, (name, flight_number, departure, destination, date, seat_number, reservation_id))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    
def delete_reservation(reservation_id):
    delete_command = "DELETE FROM flights WHERE id = ?;"
    try:
        with sqlite3.connect('flights.db') as conn:
            cursor = conn.cursor()
            cursor.execute(delete_command, (reservation_id,))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False