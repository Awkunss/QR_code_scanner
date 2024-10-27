import sqlite3

# Kết nối và khởi tạo database
def connect_db():
    return sqlite3.connect('users.db')

# Hàm tạo bảng users và qr_codes
def add_db():
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
        INSERT INTO users (id, username, password)
        VALUES (1, John, 123456);
    ''')

    # Tạo bảng qr_codes
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
add_db()