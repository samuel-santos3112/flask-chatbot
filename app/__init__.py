from flask import Flask, render_template, request
from flask_cors import CORS
from app.chat import chat


app = Flask(__name__)

app.register_blueprint(chat, url_prefix='/chat')
CORS(app)

app.config['SECRET_KEY'] = '05c6e08f1d9fdafa03147fcb8f82f124c76d2f70e3d989dc8aadb5e7d7450bec'