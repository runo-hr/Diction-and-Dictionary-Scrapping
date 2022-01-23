from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3f454dc7fa16a53f4d9acf3b'
from application import routes