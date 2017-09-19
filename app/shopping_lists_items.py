""" SHOPPING LISTS ITEMS MANAGEMENT """
from string import ascii_letters
from datetime import date

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
        if item_name == '':
            return 'Name cannot be blank'
        elif all(c in ascii_letters+'-'+' ' for c in item_name):
            users_items = self.get_user_items(user, list_name)
            for item in users_items:
                if item['name'] == item_name:
                    item['number'] += 1
                    return "Added 1 more " + item_name
            self.list_of_shopping_list_items.append({
                'name': item_name,
                'list': list_name,
                'user': user,
                'date': str(date.today()),
                'number': 1
            })
            return self.get_user_items(user, list_name)
        else:
            return "Invalid characters"

    def delete(self, item_name, list_name):
        """METHOD FOR DELETING ITEM FROM SHOPPING LIST """
        if item_name == '':
            return 'Name cannot be blank'
        elif item_name not in [item['name']
                               for item in self.list_of_shopping_list_items
                               if item['list'] == list_name]:
            return "Item not found"
        else:
            specific_shp_lst = [item
                                for item in self.list_of_shopping_list_items
                                if item['list'] == list_name]
            for item in specific_shp_lst:
                if item['name'] == item_name:
                    self.list_of_shopping_list_items.remove(item)
                    return self.list_of_shopping_list_items
    def edit(self, new_name, old_name, list_name, user):
        """METHOD FOR EDITING ITEM'S NAME IN SHOPPING LIST"""
        # Get users items
        users_list_items = self.get_user_items(user, list_name)
        for item in users_list_items:
            if new_name == item['name']:
                return "Name already used on another item"
        else:
            for item in users_list_items:
                if old_name == item['name']:
                    del item['name']
                    item.update({'name': new_name})
                elif old_name not in [item['name'] for item in users_list_items]:
                    return "The Item you want to change does not exist"
        return users_list_items
    def edit_parent_list(self, old_list_name, new_list_name, user):
        """This method is called to sync change in name when changing list name"""
        users_list_items = self.get_user_items(user, old_list_name)
        for item in users_list_items:
            del item['list']
            item.update({'list': new_list_name})
