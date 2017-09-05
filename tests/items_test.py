"""TESTS FOR SHOPPING LIST ITEMS"""
import unittest
from datetime import date
from app import shopping_lists_items



class TestCasesItems(unittest.TestCase):
    """TESTS FOR ITEMS CREATION AND BEHAVIOUR"""

    def setUp(self):
        self.item = shopping_lists_items.ShoppingListItems()

    def tearDown(self):
        del self.item
    def test_sucessful_add_item(self):
        """CHECKS WHETHER AND ITEM CAN BE ADDED SUCESSFULLY"""
        msg = self.item.add(
            "Party", "Whisky", "dalton@yahoo.com")
        self.assertEqual(
            msg, [{'user': 'dalton@yahoo.com',
                   'list': 'Party',
                   'name': 'Whisky',
                   'number': 1,
                   'date':str(date.today())}])
    def test_invalid_characters(self):
        """TESTS IF CODE ACCEPTS INVALID CHARACTERS"""
        msg = self.item.add(
            "Party", "Whisky!", "dalton@yahoo.com")
        self.assertEqual(msg, "Invalid characters")
    def test_sucess_edit_item(self):
        """"CHECKS FOR SUCESSFUL ITEM EDITING"""
        self.item.list_of_shopping_list_items = [{'user': 'dalton@yahoo.com',
                                                  'list': 'Adventure',
                                                  'name': 'Snacks'},
                                                 {'user': 'dalton@yahoo.com',
                                                  'list': 'Adventure',
                                                  'name': 'Booze'}]
        msg = self.item.edit('Soda', 'Booze', 'Adventure', "dalton@yahoo.com")
        self.assertEqual(msg, [{'user': 'dalton@yahoo.com',
                                'list': 'Adventure',
                                'name': 'Snacks'},
                               {'user': 'dalton@yahoo.com',
                                'list': 'Adventure',
                                'name': 'Soda'}])

    def test_edit_existing_item(self):
        """Check if edit name provided is similar to an existing item
        """
        self.item.list_of_shopping_list_items = [{'user': 'dalton@yahoo.com',
                                                  'list': 'Adventure',
                                                  'name': 'Snacks'},
                                                 {'user': 'dalton@yahoo.com',
                                                  'list': 'Adventure',
                                                  'name': 'Booze'}]
        msg = self.item.edit(
            'Snacks', 'Booze', 'Adventure', "dalton@yahoo.com")
        self.assertEqual(msg, "Name already used on another item")

if __name__ == '__main__':
    unittest.main()
