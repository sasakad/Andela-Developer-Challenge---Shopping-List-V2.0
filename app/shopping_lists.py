""" SHOPPING LISTS MANAGEMENT """
from string import ascii_letters
from datetime import date
class ShoppingLists(object):
    """ CLASS FOR CREATING, EDITING AND DELETING SHOPPING LISTS """

    def __init__(self):
        self.list_of_shopping_lists = []
    
    def users_list(self, user):
        return [item for item in self.list_of_shopping_lists if item['user'] == user]

    def create(self, user, list_name):
        """ METHOD FOR CREATING SHOPPING LIST """
        if list_name == '':
            return 'Name cannot be blank'
        elif all(c in ascii_letters+'-' for c in list_name):
            users_list_of_shopping_lists = \
            [item for item in self.list_of_shopping_lists if item['user'] == user]
            for item in users_list_of_shopping_lists:
                if list_name == item['name']:
                    return "List already exists."
            shopping_list_item = {
                'name': list_name,
                'user': user,
                'date': str(date.today()),
            }
            self.list_of_shopping_lists.append(shopping_list_item)
        else:
            return "Invalid characters"
        return self.users_list(user)
    def edit(self, new_name, old_name, user):
        """METHOD FOR EDITING NAME OF SHOPPING LIST """
        if all(c in ascii_letters+'-' for c in new_name):
            users_list_of_shopping_lists = \
            [item for item in self.list_of_shopping_lists if item['user'] == user]
            for item in users_list_of_shopping_lists:
                if new_name == item['name']:
                    return "Name already used on another list"
            else:
                for item in users_list_of_shopping_lists:
                    if old_name == item['name']:
                        del item['name']
                        item.update({'name': new_name})
                        return self.users_list(user)
                    elif old_name not in [item['name'] for item in self.list_of_shopping_lists if item['user'] == user]:
                        return "The List you want to change does not exist"
        else:
            return "Invalid characters"
        return self.users_list(user)

    def delete(self, list_name, user):
        """ METHOD FOR DELETING SHOPPING LISTS"""
        if list_name == '':
            return 'Name cannot be blank'
        elif list_name not in [item['name'] for item in self.list_of_shopping_lists]:
            return "Item not found"
        else:
            for item in self.list_of_shopping_lists:
                item_index = self.list_of_shopping_lists.index(item)
                if item['name'] == list_name:
                    del self.list_of_shopping_lists[item_index]
                    return list_name + " has been Deleted"
                    break
            return self.users_list(user)
    