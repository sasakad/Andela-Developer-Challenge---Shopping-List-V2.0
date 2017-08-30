"""TESTS FOR SHOPPING LIST ITEMS"""
import unittest
from app.shopping_lists_items import ShoppingListItems


class TestCasesItems(unittest.TestCase):

    def setUp(self):
        self.item = ShoppingListItems()

    def tearDown(self):
        del self.item

    
if __name__ == '__main__':
    unittest.main()
