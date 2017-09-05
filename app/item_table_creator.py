"""THE CREATION OF ITEMS TABLE TO BE SERVED TO DETAILS PAGE"""
from flask_table import Table, Col, ButtonCol

# Declare your table
class ItemTable(Table):
    """TAKES IN COLUMNS SETTINGS"""
    iname = 'name'
    lname = 'list'
    name = Col('List\'s Name', th_html_attrs={'style':'width: 30%;'})
    date = Col('Date Created', th_html_attrs={'style':'width: 30%;'})
    number = Col('Number of Items', th_html_attrs={'style':'width: 20%;'})
    del_button = ButtonCol('Delete', 'del_item',
                           button_attrs={'class':"btn btn-sm btn-outline-danger"},
                           url_kwargs={'item_name' : iname, 'list_name': lname})

# Get some objects
class Item(object):
    """ SETS DATA ENTRY TO COLUMN CREATED"""
    def __init__(self, name, date, number, edit_button, del_button):
        self.lname = name
        self.date = date
        self.number = number
        self.edit_button = edit_button
        self.del_button = del_button
