# Import Dependency
from flask import Flask

# Reset flask app 
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

