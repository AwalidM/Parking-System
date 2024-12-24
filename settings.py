import os

DB_SETTINGS = {
    'host': 'localhost',
    'user': 'Amr2221',
    'password': '0000',
    'database': 'e_parking'
}

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "your_secret_key")
