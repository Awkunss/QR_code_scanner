from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

from pw import hash_password, check_password
from create_qr_code import connect_db, get_code, add_code, remove_code, generate_random_code
import qrcode

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Kết nối database
def connect_db():
    return sqlite3.connect('database.db')

@app.route('/scan_qr')
def scan_qr_page():
    if 'username' in session:
        return render_template('scan_qr.html')
    return redirect(url_for('login'))

@app.route('/scan_result')
def scan_result():
    if 'username' in session:
        success = request.args.get('success', 'false') == 'true'
        return render_template('scan_result.html', success=success)
    return redirect(url_for('login'))

# Tạo trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        con = connect_db()
        cursor = con.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        con.close()

        if user and check_password(user[0], password):
            session['username'] = username
            if username == 'admin':
                return redirect(url_for('admin'))
            return redirect(url_for('scan_qr_page'))
        else:
            return render_template('index.html', error='Invalid credentials')
    
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)  # Mã hóa mật khẩu

        con = connect_db()
        cursor = con.cursor()

        try:
            # Lưu tài khoản vào cơ sở dữ liệu với mật khẩu đã mã hóa
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            con.commit()
            con.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return 'Username already exists.'

    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'username' not in session or session['username'] != 'admin':
        return redirect(url_for('login'))

    if request.method == 'POST':
        action = request.form['action']
        if action == 'add':
            new_hash = generate_random_code()
            add_code(new_hash)
            # Generate QR code image
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(new_hash)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"qr_codes/{new_hash}.png")
        elif action == 'delete':
            hash_to_delete = request.form['hash']
            remove_code(hash_to_delete)
            # You might want to delete the QR code image file here as well

    qr_codes = get_code()
    return render_template('admin.html', qr_codes=qr_codes)

if __name__ == "__main__":
    app.run(debug=True)
