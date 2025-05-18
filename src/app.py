from database.connection import get_connection

def main():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 1 * FROM NODO")
        print(cursor.fetchone())
        conn.close()

if __name__ == "__main__":
    main()
