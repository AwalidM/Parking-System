from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="your_secret_key",
    )
    return app

if __name__ == "_main_":
    app = create_app()
    app.run(debug=True)