import sys
from markupsafe import escape
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    msg = f"Python version= {sys.version_info}"
    #msg += f" \nFlask version= {Flask.__version__}"
    return msg

@app.route('/about')
def about():
    msg = " I am a Computer Scientist, Data Scientist and Finance Quant"
    return msg

@app.route('/contact')
def contact():
    msg = "email mailto::jmuller.ics88@gtalumni.org"
    return msg

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))