"""""FLASK'S VIEW FILE"""""

from flask import render_template, request, session, redirect, url_for
from app import app, usr_account, shopn_list, shopn_items
from app import list_table_creator, item_table_creator
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
    """Loads the dashboard page"""
    user = session['username']
    table=list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
    return render_template("dashboard.html", table_out = table)

@app.route('/details', methods=['GET','POST'])
def details():
    """Loads the details page"""
    user = session['username']
    table=item_table_creator.ItemTable(shopn_items.list_of_shopping_list_items)
    return render_template("details.html", table_out = table)

    return render_template("details.html")
@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        msg = usr_account.login(email, pwd)
        if msg == "Success!":
            session['email'] = email
            session['username']= usr_account.get_uname_by_email(email)
            return render_template('dashboard.html', response=msg)
        else:
            return render_template('login.html', response=msg)
    return render_template("login.html")

@app.route('/add_list', methods=['GET','POST'])
def add():
    user = session['username']
    if request.method == 'POST':
        list_name = request.form['list_name']
        add_response = shopn_list.create(user, list_name)
        if add_response == shopn_list.list_of_shopping_lists:
            text_out = "Successfully added"
            return render_template('dashboard.html', response=text_out, table_out=list_table_creator.ItemTable(add_response))
        else:
            return render_template('dashboard.html', response=add_response, 
        table_out=list_table_creator.ItemTable(shopn_list.list_of_shopping_lists))
    return redirect(url_for('dashboard'))
@app.route('/add_item', methods=['GET','POST'])
def add_item():
    user = session['username']
    if request.method == 'POST':
        item_name = request.form['item_name']
        add_response = shopn_items.add('hello',item_name,user)
        if add_response == shopn_items.list_of_shopping_list_items:
            text_out = "Successfully added"
            return render_template('details.html', response=text_out, table_out=item_table_creator.ItemTable(add_response))
        else:
            return render_template('details.html', response=add_response, 
        table_out=item_table_creator.ItemTable(shopn_items.list_of_shopping_list_items))
    return redirect(url_for('details'))
