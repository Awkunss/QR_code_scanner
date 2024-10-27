# QR Code Scanning App

This is a Flask-based web application for scanning and managing QR codes, including user login, registration, and an admin panel for QR code management. The app uses an SQLite database to store user credentials and QR codes.

## Features

- **User Authentication**: Users can log in and register with a username and password. Passwords are securely hashed.
- **QR Code Scanning**: Logged-in users can access the QR code scanning page.
- **Admin Panel**: The `admin` user has access to additional features:
  - Generate new QR codes.
  - View and manage existing QR codes.
  - View and manage user account (future).
- **QR Code Generation**: Each QR code generated has an associated unique hash value and is saved as an image file.
  
## Dependencies

The project requires the following Python packages:

- Flask
- sqlite3 (built-in in Python)
- qrcode
- Other modules (`hash_password`, `check_password`, `connect_db`, `get_code`, `add_code`, `remove_code`, `generate_random_code`) are defined in external files (`pw.py` and `create_qr_code.py`).

Install dependencies via `pip`:

```bash
pip install Flask qrcode
