from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker is a platform for building, shipping, and running distributed applications in containers.'
