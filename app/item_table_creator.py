# import things
from flask_table import Table, Col, LinkCol

# Declare your table
class ItemTable(Table):
    #user = Col('Name')
    name = Col('Item\'s Name')
    date = Col('Date Created')
# Get some objects
class Item(object):
    def __init__(self, name, date):
        self.name = name
        self.date = date

