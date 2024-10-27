import bcrypt

# Hàm mã hóa mật khẩu
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Hàm kiểm tra mật khẩu
def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
