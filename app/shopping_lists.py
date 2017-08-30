""" SHOPPING LISTS MANAGEMENT """
from string import ascii_letters

class ShoppingLists(object):
    """ CLASS FOR CREATING, EDITING AND DELETING SHOPPING LISTS """

    def __init__(self):
        self.list_of_shopping_lists = []

    def create(self, user, list_name):
        """ METHOD FOR CREATING SHOPPING LIST """
        # Checking special characters
        if all(c in ascii_letters+'-' for c in list_name):
            users_list_of_shopping_lists = \
            [item for item in self.list_of_shopping_lists if item['user'] == user]
            for item in users_list_of_shopping_lists:
                if list_name == item['name']:
                    return "List already exists."
            shopping_list_item = {
                'name': list_name,
                'user': user,
            }
            self.list_of_shopping_lists.append(shopping_list_item)
        else:
            return "Invalid characters"
        return [item for item in self.list_of_shopping_lists if item['user'] == user]
    