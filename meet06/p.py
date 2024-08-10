from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/igs')
def igs():
    return render_template("igs.html")

if __name__ == "__main__":
    app.run(debug=True)