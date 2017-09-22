"""THIS CREATES TABLE TO BE SERVED TO DASHBOARD"""
from flask_table import Table, Col, LinkCol, ButtonCol
from flask import session

class ItemTable(Table):
    """THIS CREATES COLUMNS WITH ATTRIBUTES """
    lname = 'name'
    name = Col('Name', th_html_attrs={'style':'width: 27%;'})
    date = Col('Date Created', th_html_attrs={'style':'width: 27%;'})
    details = LinkCol('List Items', 'details', th_html_attrs={'style':'width: 20%;'},
                      url_kwargs={'list_name' : lname})
    user = Col('Owner', 'user', th_html_attrs={'style':'width: 13%;'})
    edit_button = ButtonCol('Edit Name', 'edit_list',
                        button_attrs={'class':"btn btn-sm btn-primary"},
                        th_html_attrs={'style':'width: 13%;'},
                        url_kwargs={'old_name' : lname})
    del_button = ButtonCol('Delete', 'del_list',
                           button_attrs={'class':"btn btn-sm btn-danger"},
                           th_html_attrs={'style':'width: 13%;'},
                           url_kwargs={'list_name' : lname})


# Get some objects
class Item(object):
    """THIS ENTERS DATA INTO THE CREATED COLUMNS"""
    def __init__(self, name, date, details, user):
        self.lname = name
        self.date = date
        self.details = details
        self.owner = user