from flask import Flask

app = Flask(__name__)
app.secret_key = "7tt274t34t214t171"
from app import views
