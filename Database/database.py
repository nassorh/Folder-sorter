import sqlite3

class db():
    @staticmethod
    def get_catergorys() -> list:
        conn = sqlite3.connect('Database/sqlite.db')
        catergorys = conn.execute("SELECT name from catergory")
        catergorys = catergorys.fetchall()
        conn.close()
        return catergorys
    
    @staticmethod
    def get_extensions() -> list:
        conn = sqlite3.connect('Database/sqlite.db')
        extensions = conn.execute("SELECT extensions.name,catergory.name FROM extensions LEFT JOIN catergory ON extensions.catergory_id=catergory.id")
        extensions = extensions.fetchall()
        conn.close()
        return extensions