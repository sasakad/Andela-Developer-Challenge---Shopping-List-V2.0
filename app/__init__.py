""" INITIALIZING FLASK APP"""
from flask import Flask
from app import accounts, shopping_lists, shopping_lists_items

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = "theghostofgabratula"

usr_account = accounts.Accounts()
shopn_list = shopping_lists.ShoppingLists()
shopn_items = shopping_lists_items.ShoppingListItems()

from app import views

app.config.from_object('config')
