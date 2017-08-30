"""""FLASK'S VIEW FILE"""""

from flask import render_template, request, session
from app import app, usr_account, shopn_list
from app import table_creator
@app.route('/')
def index():
    """LOADS HOME PAGE"""
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """SIGNS UP NEW USER"""
    if request.method == 'POST':
        uname = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        pwd_confirmed = request.form['password_confirm']

        msg = usr_account.registration(uname, email, pwd, pwd_confirmed)
        if msg == "Your account is now registered please proceed to login":
            return render_template("login.html", response= msg)
        else:
            return render_template("signup.html", response = msg)
    return render_template("signup.html")
@app.route('/dashboard', methods=['GET', 'POST'])
def dasboard():
    user = session['email']
    user_shopping_lists = shopn_list.users_list(user)
    if request.method == 'POST':
        list_name = request.form['list-name']
        response = shopn_list.create(user, list_name)
        if isinstance(response, list):
            if response == []:
                return render_template('dashboard.html', response='There are no Shopping lists please add some')
            else:
                table = table_creator.ItemTable(response)
                return render_template('dashboard.html', table_out=table)
        else:
            return render_template('dashboard.html', response=response)
    return render_template("dashboard.html")

@app.route('/details')
def details():
    return render_template("details.html")
@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        msg = usr_account.login(email, pwd)
        if msg == "Success!":
            session['email'] = email
            return render_template('dashboard.html', response=msg)
        else:
            return render_template('login.html', response=msg)
    return render_template("login.html")

@app.route('/add', methods=['GET','POST'])
def add():
    user = session['email']
    if request.method == 'POST':
        list_name = request.form['list_name']
        add_response = shopn_list.create(user, list_name)
        if add_response == shopn_list.list_of_shopping_lists:
            text_out = "Successfully added"
            return render_template('dashboard.html', response=text_out, table_out=table_creator.ItemTable(add_response))
        else:
            return render_template('dashboard.html', response=add_response, 
        table_out=table_creator.ItemTable(shopn_list.list_of_shopping_lists))
    return render_template('dashboard.html')
