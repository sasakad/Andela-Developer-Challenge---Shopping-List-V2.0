"""TESTS FOR SHOPPING LISTS"""
import unittest
from app.shopping_lists import ShoppingLists


class TestCasesShoppingList(unittest.TestCase):

    def setUp(self):
        self._list = ShoppingLists()

    def tearDown(self):
        del self._list

if __name__ == '__main__':
    unittest.main()
