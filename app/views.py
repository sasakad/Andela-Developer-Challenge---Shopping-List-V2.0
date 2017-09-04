"""""FLASK'S VIEW FILE"""""

from functools import wraps
from flask import render_template, request, session, redirect, url_for
from app import app, usr_account, shopn_list, shopn_items
from app import list_table_creator, item_table_creator

@app.route('/')
def index():
    """LOADS HOME PAGE"""
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            msg = "Please login"
            return render_template("login.html", response=msg)
    return wrap
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """SIGNS UP NEW USER"""
    if request.method == 'POST':
        uname = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        pwd_confirmed = request.form['password_confirm']

        msg = usr_account.registration(uname, email, pwd, pwd_confirmed)
        if msg == "Your account is now registered please proceed to login" or msg == "Your Account Already Active. Proceed to login":
            return render_template("login.html", response= msg)
        else:
            return render_template("signup.html", response = msg)
    return render_template("signup.html")
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """Loads the dashboard page"""
    user = session['username']
    table_response=list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
    return render_template("dashboard.html", table_out = table_response)
@app.route('/details/<list_name>/', methods=['GET','POST'])
@login_required
def details(list_name):
    """Loads the details page"""
    specific_list_items = [ item for item in 
    shopn_items.list_of_shopping_list_items if item['list'] == list_name]
    table_response=item_table_creator.ItemTable(specific_list_items) 
    return render_template("details.html", table_out = table_response)
@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        msg = usr_account.login(email, pwd)
        if msg == "Success!":
            session['email'] = email
            session['username']= usr_account.get_uname_by_email(email)
            table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
            return render_template('dashboard.html', response=msg , table_out = table_response)
        else:
            return render_template('signup.html', response=msg)
    return render_template("login.html")
@app.route('/logout')
@login_required
def log_out():
    session.clear()
    return render_template('index.html',response="You are now logged Out")

@app.route('/dashboard/add_list', methods=['GET','POST'])
@login_required
def add():
    user = session['username']
    if request.method == 'POST':
        list_name = request.form['list_name']
        add_response = shopn_list.create(user, list_name)
        if isinstance(add_response, list):
            if add_response == shopn_list.list_of_shopping_lists:
                table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
                text_out = "Successfully added"
                return render_template('dashboard.html', response=text_out, table_out= table_response)
            else:
                table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
                text_out = "Unable to add the List Please Try again"
                return render_template('dashboard.html', table_out = table_response)
        else:
            table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
            return render_template('dashboard.html', response = add_response, table_out = table_response)
    return redirect(url_for('dashboard'))

@app.route('/dashboard/edit_list/', methods=['GET', 'POST'])
@login_required
def edit_list():
    pass


@app.route('/dashboard/del_list/<list_name>', methods=['GET', 'POST'])
@login_required
def del_list(list_name):
    user = session['username']
    if list_name:
        #list_name = request.form['list_name']
        del_response = shopn_list.delete(list_name, user)
        if del_response == shopn_list.list_of_shopping_lists:
            text_out = "Successfully Removed"
            table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
            return render_template('dashboard.html', response=text_out, table_out=table_response)
        else:
            table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
            return render_template('dashboard.html', response=del_response, table_out= table_response)
    return redirect(url_for('dashboard'))
@app.route('/details/<list_name>/add_item', methods=['GET','POST'])
@login_required
def add_item(list_name):
    user = session['username']
    if request.method == 'POST':
        item_name = request.form['item_name']
        add_response = shopn_items.add(list_name,item_name,user)
        if add_response == shopn_items.list_of_shopping_list_items:
            text_out = "Successfully added"
            table_response = item_table_creator.ItemTable(add_response)
            return redirect(url_for('details', list_name=list_name))
        else:
            table_response = item_table_creator.ItemTable(shopn_items.list_of_shopping_list_items)
            #render_template('details.html', response=add_response, table_out=table_response)
            return redirect(url_for('details', list_name = list_name))
    return redirect(url_for('details', list_name = list_name))

@app.route('/dashboard/edit_item/', methods=['GET', 'POST'])
@login_required
def edit_item():
    pass


@app.route('/del_item/<list_name>/<item_name>', methods=['GET','POST'])
@login_required
def del_item(item_name, list_name):
    user = session['username']
    if item_name:
        #item_name = request.form['item_name']
        del_response = shopn_items.delete(item_name, list_name)
        if del_response is None:
            text_out = "Successfully Removed"
            return render_template('details.html', response=text_out)
        elif isinstance(del_response, list):
            return redirect(url_for('details', list_name=list_name))
        else:
            table_response = item_table_creator.ItemTable(shopn_items.list_of_shopping_list_items)
            return render_template('details.html', response=del_response, table_out=table_response)
    return redirect(url_for('details'))
