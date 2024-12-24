from flask import Flask
import mysql.connector

app = Flask(__name__)

DB_SETTINGS = {
    'host': 'localhost',
    'user': 'Amr2221',
    'password': '0000',
    'database': 'e_parking'
}

# Define a function to manage users
class User:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_SETTINGS)
        self.cursor = self.connection.cursor()

    def create_user(self, email, username, password):
        try:
            self.cursor.execute(
                "INSERT INTO User (email, username, password) VALUES (%s, %s, %s)",
                (email, username, password)
            )
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error creating user: {e}")

    def get_user(self, email):
        try:
            self.cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Error fetching user: {e}")

# Initialize the User class for operations
user_model = User()

@app.route('/')
def index():
    return "E-Parking Flask Backend is running!"
