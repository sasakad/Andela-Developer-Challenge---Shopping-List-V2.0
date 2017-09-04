# import things
from flask_table import Table, Col, LinkCol, ButtonCol

# Declare your table
class ItemTable(Table):
    lname = 'name'
    id = Col('id', show=False)
    name = Col('List\'s Name', allow_sort=False,th_html_attrs={'style':'width: 25%;'} )
    date = Col('Date Created', th_html_attrs={'style':'width: 25%;'})
    details = LinkCol('List Items', 'details', th_html_attrs={'style':'width: 25%;'},
                 url_kwargs={'list_name' : lname})
    edit_button = ButtonCol('Edit', 'edit_list', button_attrs={'class':"btn btn-sm btn-outline-primary"},
                url_kwargs={'list_name' : lname})
    del_button = ButtonCol('Delete', 'del_list', button_attrs={'class':"btn btn-sm btn-outline-danger"}, 
                url_kwargs={'list_name' : lname})


# Get some objects
class Item(object):
    def __init__(self, name, date, details ,edit_button, del_button):
        self.lname = name
        self.date = date
        self.details = details
        self.edit_button = edit_button
        self.del_button = del_button

