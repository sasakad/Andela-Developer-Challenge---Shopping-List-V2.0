# import things
from flask_table import Table, Col, LinkCol

# Declare your table
class ItemTable(Table):
    #user = Col('Name')
    name = Col('List\'s Name')
    date = Col('Date Created')
    details = LinkCol('List Items', 'details')

# Get some objects
class Item(object):
    def __init__(self, name, date, details = None):
        self.name = name
        self.date = date

