"""TESTS FOR SHOPPING LIST ITEMS"""
import unittest
from app import shopping_lists_items
from datetime import date


class TestCasesItems(unittest.TestCase):

    def setUp(self):
        self.item = shopping_lists_items.ShoppingListItems()

    def tearDown(self):
        del self.item
    def test_sucessful_add_item(self):  
        msg = self.item.add(
            "Party", "Whisky", "dalton@yahoo.com")
        self.assertEqual(
            msg, [{'user': 'dalton@yahoo.com', 'list': 'Party', 'name': 'Whisky','number': 1,
            'user': 'dalton@yahoo.com', 'date':str(date.today())}])
    
    '''def test_adding_existing_item(self):
        self.item.list_of_shopping_list_items = [{'user': 'dalton@yahoo.com', 'list': 'Party', 'name': 'Whisky'}, {
            'user': 'dalton@yahoo.com', 'list': 'Party', 'name': 'Soda'}]
        msg = self.item.add(
            "Party", "Whisky", "dalton@yahoo.com")
        self.assertEqual(msg, "Item already exists")'''

    def test_invalid_characters(self):
        msg = self.item.add(
            "Party", "Whisky!", "dalton@yahoo.com")
        self.assertEqual(msg, "Invalid characters")

    
    def test_sucess_edit_item(self):
        self.item.list_of_shopping_list_items = [{'user': 'dalton@yahoo.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'user': 'dalton@yahoo.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item.edit(
            'Soda', 'Booze', 'Adventure', "dalton@yahoo.com")
        self.assertEqual(msg, [{'user': 'dalton@yahoo.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'user': 'dalton@yahoo.com', 'list': 'Adventure', 'name': 'Soda'}])

    def test_edit_existing_item(self):
        """Check if edit name provided is similar to an existing item
        """
        self.item.list_of_shopping_list_items = [{'user': 'dalton@yahoo.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'user': 'dalton@yahoo.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item.edit(
            'Snacks', 'Booze', 'Adventure', "dalton@yahoo.com")
        self.assertEqual(msg, "Name already used on another item")

    
if __name__ == '__main__':
    unittest.main()
