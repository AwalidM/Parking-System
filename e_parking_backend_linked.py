import mysql.connector
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Debugging log for templates directory
if os.path.exists(app.template_folder):
    print("Templates folder contents:", os.listdir(app.template_folder))
else:
    print("Templates folder does not exist.")

# Database connection settings
DB_SETTINGS = {
    'host': 'localhost',
    'user': 'Amr2221',
    'password': '0000',
    'database': 'e_parking'
}

# Database connection function
def get_db_connection():
    try:
        return mysql.connector.connect(**DB_SETTINGS)
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        raise

# User model for database interactions
class UserModel:
    def __init__(self):
        self.connection = get_db_connection()

    def get_user(self, email):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id, email, username, password FROM User WHERE email = %s", (email,))
            user = cursor.fetchone()
            print("Fetched user:", user)  # Debugging log
            return user
        finally:
            cursor.close()

    def create_user(self, email, username, password):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO User (email, username, password) VALUES (%s, %s, %s)",
                (email, username, password),
            )
            self.connection.commit()
            print(f"User {username} created successfully.")  # Debugging log
        except mysql.connector.Error as err:
            print(f"Error creating user: {err}")
            raise
        finally:
            cursor.close()

# Instantiate the user model
user_model = UserModel()

# User Login API
@app.route('/api/users/', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Debugging logs
    print("Login request received with email:", email)
    print("Password provided:", password)

    user = user_model.get_user(email)

    # Debugging user fetched from database
    print("User fetched from database:", user)

    if user and user['password'] == password:
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user['id'],
                'email': user['email'],
                'username': user['username']
            }
        })
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Registration API
@app.route('/api/users/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    print("Registration request received with data:", data)  # Debugging log

    try:
        user_model.create_user(email, username, password)
        print(f"User {username} registered successfully.")  # Debugging log
        return jsonify({'message': 'User registered successfully'})
    except Exception as e:
        print(f"Error registering user: {e}")  # Debugging log
        return jsonify({'error': str(e)}), 500

# Parking Slots API
@app.route('/api/parking-slots/', methods=['GET'])
def get_parking_slots():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, name, is_available FROM ParkingSlot;")
        slots = cursor.fetchall()
        return jsonify(slots)
    except mysql.connector.Error as err:
        print("Error fetching parking slots:", err)
        return jsonify({'error': 'Failed to fetch parking slots'}), 500
    finally:
        cursor.close()
        connection.close()

#book slot
@app.route('/api/book-slot/', methods=['POST'])
def book_slot():
    data = request.json
    user_id = data.get('user')
    parking_slot_id = data.get('parking_slot')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check if the parking slot is available
        cursor.execute("SELECT is_available FROM ParkingSlot WHERE id = %s", (parking_slot_id,))
        slot = cursor.fetchone()
        if not slot or not slot[0]:
            return jsonify({'error': 'Parking slot is not available'}), 400

        # Book the parking slot
        cursor.execute("""
            INSERT INTO Reservation (user_id, parking_slot_id, start_time, end_time)
            VALUES (%s, %s, %s, %s)
        """, (user_id, parking_slot_id, start_time, end_time))

        # Mark the slot as unavailable
        cursor.execute("UPDATE ParkingSlot SET is_available = FALSE WHERE id = %s", (parking_slot_id,))
        connection.commit()

        return jsonify({'message': 'Parking slot booked successfully'})
    except mysql.connector.Error as err:
        print("Error booking slot:", err)
        return jsonify({'error': 'Failed to book slot'}), 500
    finally:
        cursor.close()
        connection.close()


# Reservation API
@app.route('/api/reservations/', methods=['GET'])
def get_reservations():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT r.id, r.user_id, r.parking_slot_id, r.start_time, r.end_time, p.name AS parking_slot
            FROM Reservation r
            JOIN ParkingSlot p ON r.parking_slot_id = p.id
        """)
        reservations = cursor.fetchall()
        print("Fetched reservations:", reservations)  # Debugging log
        return jsonify(reservations)
    except mysql.connector.Error as err:
        print("Error fetching reservations:", err)
        return jsonify({'error': 'Failed to fetch reservations'}), 500
    finally:
        cursor.close()
        connection.close()

# Serve the dashboard
@app.route('/dashboard.html')
def dashboard():
    print("Rendering dashboard.html")  # Debugging log
    return render_template('dashboard.html')

# Serve the login page
@app.route('/login.html')
def login_page():
    print("Rendering login.html")  # Debugging log
    return render_template('login.html')

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
