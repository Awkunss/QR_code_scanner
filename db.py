import sqlite3

# Kết nối và khởi tạo database
def connect_db():
    return sqlite3.connect('database.db')

# Hàm tạo bảng users và qr_codes
def init_db():
    con = connect_db()
    cursor = con.cursor()
    
    # Tạo bảng users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            points INTEGER DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qr_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hash TEXT UNIQUE
        )
    ''')

    # Lưu và đóng kết nối
    con.commit()
    con.close()

# Thực hiện khởi tạo database
init_db()