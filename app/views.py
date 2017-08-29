# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")
@app.route('/dasboard')
def dasboard():
    return render_template("dashboard.html")
@app.route('/dashboard/details')
def details():
    return render_template("details.html")
@app.route('/login')
def login():
    return render_template("login.html")
