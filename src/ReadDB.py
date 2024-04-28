import sqlite3

class database_manager:
    def __init__(self, db_name='customers.db'):
        # Connect to the database (creates a new database if it doesn't exist)
        self.conn = sqlite3.connect(db_name)

        # Create a cursor object to execute SQL queries
        self.cursor = self.conn.cursor()

        # Create a table for users
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                email TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Commit the changes
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def get_users(self):
        self.cursor.execute("SELECT * FROM Customers")
        users = self.cursor.fetchall()
        return users

    def get_user_by_name(self, email):
        self.cursor.execute("SELECT * FROM Customers WHERE email = ?", (email,))
        users = self.cursor.fetchall()
        return users

    def insert_user(self, email, first_name, last_name, password):
        self.cursor.execute("INSERT INTO Customers VALUES (?, ?, ?, ?)", (email, first_name, last_name, password))
        self.conn.commit()