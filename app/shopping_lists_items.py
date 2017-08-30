""" SHOPPING LISTS ITEMS MANAGEMENT """
from string import ascii_letters

class ShoppingListItems(object):
    """ CLASS FOR ADDING, EDITING AND DELETING SHOPPING LIST ITEMS """


    def __init__(self):
        self.list_of_shopping_list_items = []

    def get_user_items(self, user, list_name):
        """METHOD FOR DETERMINING ITEMS IN A USERS LIST"""
        user_items = \
        [item for item in self.list_of_shopping_list_items if item['user']
         == user and item['list'] == list_name]
        return user_items

    def add(self, list_name, item_name, user):
        """METHOD FOR ADDING ITEMS IN SHOPPING LIST """
        if all(c in ascii_letters+'-' for c in item_name):
            users_items = self.get_user_items(user, list_name)
            for item in users_items:
                if item['name'] == item_name:
                    return "Item already exists"
            self.list_of_shopping_list_items.append({
                'name': item_name,
                'list': list_name,
                'user': user
            })
            return self.get_user_items(user, list_name)
        else:
            return "Invalid characters"

    