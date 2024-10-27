import qrcode, sqlite3
import hashlib
import random
import string

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

def connect_db():
    return sqlite3.connect('database.db')

def get_code():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT hash FROM qr_codes")
    qr_codes = cursor.fetchall()
    con.close()
    return qr_codes

def add_code(hash):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("INSERT INTO qr_codes (hash) VALUES (?)", (hash,))
    con.commit()
    con.close()

def remove_code(hash):
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("DELETE FROM qr_codes WHERE hash=?", (hash,))
    con.commit()
    con.close()

def generate_random_code():
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return hashlib.sha256(random_string.encode()).hexdigest()

if "__main__" == __name__:
    codes = get_code()
    for code in codes:
        qr.add_data(code[0])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"qr_codes/{code[0]}.png")
        qr.clear()