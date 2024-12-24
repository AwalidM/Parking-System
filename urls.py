from flask import Flask
from e_parking_backend_linked import app as backend_app

app = Flask(__name__)

# Mount backend Flask app
app.register_blueprint(backend_app, url_prefix='/api')

@app.route('/')
def index():
    return "Welcome to the E-Parking System!"
