import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._establish_connection()
        return cls._instance

    def _establish_connection(self):
        try:
            self.conn = sqlite3.connect("dao/database.db", check_same_thread=False)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Database Connection Error: {str(e)}")
            self.conn = None
            self.cursor = None

    def get_cursor(self):
        return self.cursor

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        DatabaseConnection._instance = None