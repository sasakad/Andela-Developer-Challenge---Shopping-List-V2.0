"""""FLASK'S VIEW FILE"""""

from functools import wraps
from flask import render_template, request, session, redirect, url_for, flash
from app import app, usr_account, shopn_list, shopn_items
from app import list_table_creator, item_table_creator

@app.route('/')
def index():
    """LOADS HOME PAGE"""
    return render_template("index.html")

def login_required(f):
    """RESTRICTS ACCESS TO PAGES THAT REQUIRE USER TO BE LOGGED IN"""
    @wraps(f)
    def wrap(*args, **kwargs):
        """WRAPS AROUND THE f FUNCTION"""
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
        if msg == "Your account is now registered please proceed to login"\
        or msg == "Your Account Already Active. Proceed to login":
            return render_template("login.html", response=msg)
        else:
            return render_template("signup.html", response=msg)
    return render_template("signup.html")
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """RENDERS THE DASHBOARD PAGE"""
    user = session['username']
    print(shopn_list.users_list(user))
    table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
    return render_template("dashboard.html", table_out=table_response, user=str.capitalize(user))
@app.route('/details/<list_name>/', methods=['GET', 'POST'])
@login_required
def details(list_name):
    """Loads the details page"""
    specific_list_items = [item
                           for item in shopn_items.list_of_shopping_list_items
                           if item['list'] == list_name]
    table_response = item_table_creator.ItemTable(specific_list_items)
    return render_template("details.html",
                           table_out=table_response,
                           list_name=str.capitalize(list_name))
@app.route('/login', methods=['GET', 'POST'])
def login():
    """HANDLES REQUESTS SENT BY LOGIN PAGE"""
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        msg = usr_account.login(email, pwd)
        if msg == "Success!":
            session['email'] = email
            session['username'] = usr_account.get_uname_by_email(email)
            table_response = list_table_creator.ItemTable(shopn_list.list_of_shopping_lists)
            return render_template('dashboard.html',
                                   response=msg,
                                   table_out=table_response,
                                   user=str.capitalize(session['username']))
        else:
            return render_template('signup.html', response=msg, alert_type="alert-danger")
    return render_template("login.html")
@app.route('/logout')
@login_required
def log_out():
    """LOGS USER OUT"""
    username = str.capitalize(session['username'])
    session.clear()
    flash("Goodbye {}".format(username), 'alert-warning')
    return render_template('index.html', response="You are now logged Out", alert_type="alert-info")

@app.route('/dashboard/add_list', methods=['GET', 'POST'])
@login_required
def add():
    """ADDS A SHOPPING LIST"""
    user = session['username']
    if request.method == 'POST':
        list_name = str.lower(request.form['list_name'])
        add_response = shopn_list.create(user, list_name)
        if isinstance(add_response, list):
            if add_response == shopn_list.list_of_shopping_lists:
                table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
                text_out = "Successfully added"
                return render_template('dashboard.html',
                                       response=text_out,
                                       table_out=table_response,
                                       user=str.capitalize(user))
            else:
                table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
                text_out = "Unable to add the List Please Try again"
                return render_template('dashboard.html',
                                       table_out=table_response,
                                       user=str.capitalize(user),
                                       alert_type="alert-danger")
        else:
            table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
            return render_template('dashboard.html',
                                   response=add_response,
                                   table_out=table_response,
                                   user=str.capitalize(user),
                                   alert_type='alert-danger')
    return redirect(url_for('dashboard'))

@app.route('/dashboard/edit_list', methods=['GET', 'POST'])
@login_required
def edit_list():
    """EDITS THE NAME OF A SHOPPING LIST"""
    user = session['username']
    if request.method == 'POST':
        new_name = str.lower(request.form['new_name'])
        old_name = str.lower(request.form['old_name'])
        edit_response = shopn_list.edit(new_name, old_name, user)
        if isinstance(edit_response, list):
            if edit_response == shopn_list.list_of_shopping_lists:
                table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
                text_out = "Successfully Changed {} to {}".format(old_name, new_name)
                return render_template('dashboard.html',
                                       response=text_out,
                                       table_out=table_response,
                                       user=str.capitalize(user))
            else:
                table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
                text_out = edit_response
                return render_template('dashboard.html',
                                       table_out=table_response,
                                       user=str.capitalize(user),
                                       alert_type='alert-danger')
        else:
            table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
            return render_template('dashboard.html',
                                   response=edit_response,
                                   table_out=table_response,
                                   user=str.capitalize(user),
                                   alert_type='alert-danger')
    return redirect(url_for('dashboard'))

@app.route('/dashboard/del_list/<list_name>', methods=['GET', 'POST'])
@login_required
def del_list(list_name):
    """DELETES A SHOPPING LIST """
    user = session['username']
    if list_name:
        #list_name = request.form['list_name']
        del_response = shopn_list.delete(list_name, user)
        if del_response == shopn_list.list_of_shopping_lists:
            text_out = "{} has been removed".format(list_name)
            table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
            return render_template('dashboard.html',
                                   response=text_out,
                                   table_out=table_response,
                                   user=str.capitalize(user),
                                   alert_type='alert-danger')
        else:
            table_response = list_table_creator.ItemTable(shopn_list.users_list(user))
            return render_template('dashboard.html',
                                   response=del_response,
                                   table_out=table_response,
                                   user=str.capitalize(user),
                                   alert_type='alert-danger')
    return redirect(url_for('dashboard'))
@app.route('/details/<list_name>/add_item', methods=['GET', 'POST'])
@login_required
def add_item(list_name):
    """ADDS AN ITEM TO A SHOPPING LIST"""
    user = session['username']
    if request.method == 'POST':
        item_name = str.lower(request.form['item_name'])
        add_response = shopn_items.add(list_name, item_name, user)
        if add_response == shopn_items.list_of_shopping_list_items \
        or shopn_items.get_user_items(user, list_name):
            flash('Sucessfully added.', 'alert-success')
            return redirect(url_for('details', list_name=list_name))
        else:
            if add_response == str("Added 1 more " + item_name):
                flash(add_response, 'alert-success')
            else:
                flash(add_response, 'alert-danger')
            return redirect(url_for('details', list_name=list_name))
    return redirect(url_for('details', list_name=list_name))

@app.route('/details/<list_name>/edit_item', methods=['GET', 'POST'])
@login_required
def edit_item(list_name):
    """EDITS AN ITEMS NAME"""
    user = session['username']
    list_name = list_name
    if request.method == 'POST':
        new_name = str.lower(request.form['new_name'])
        old_name = str.lower(request.form['old_name'])
        edit_response = shopn_items.edit(new_name, old_name, list_name, user)
        if edit_response == shopn_items.get_user_items(user, list_name):
            text_out = "Successfully changed {} to {}".format(old_name, new_name)
            flash(text_out, 'alert-success')
            return redirect(url_for('details', list_name=list_name))
        else:
            flash(edit_response, 'alert-danger')
            return redirect(url_for('details', list_name=list_name))
    return redirect(url_for('details', list_name=list_name))


@app.route('/del_item/<list_name>/<item_name>', methods=['GET', 'POST'])
@login_required
def del_item(item_name, list_name):
    """DELETES AN ITEM """
    if item_name:
        #item_name = request.form['item_name']
        del_response = shopn_items.delete(item_name, list_name)
        if del_response is None:
            text_out = "Successfully Removed {}.".format(item_name)
            flash(text_out)
            return render_template('details.html',
                                   response=text_out,
                                   list_name=str.capitalize(list_name),
                                   alert_type='alert-success')
        elif isinstance(del_response, list):
            text_out = "Successfully Removed {}.".format(item_name)
            flash(text_out, 'alert-success')
            return redirect(url_for('details', list_name=list_name))
        else:
            table_response = item_table_creator.ItemTable(shopn_items.list_of_shopping_list_items)
            return render_template('details.html',
                                   response=del_response,
                                   table_out=table_response,
                                   list_name=str.capitalize(list_name),
                                   alert_type='alert-dander')
    return redirect(url_for('details'))
