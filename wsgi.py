from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"
