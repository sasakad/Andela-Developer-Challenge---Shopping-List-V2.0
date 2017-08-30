"""TESTS FOR SHOPPING LISTS"""
import unittest
from app.shopping_lists import ShoppingLists


class TestCasesShoppingList(unittest.TestCase):

    def setUp(self):
        self._list = ShoppingLists()

    def tearDown(self):
        del self._list
    
    def test_sucessful_create(self):
        msg = self._list.create( "dalton", 'Party')
        self.assertEqual(
            msg, [{'user': 'dalton', 'name': 'Party'}])
    
    def test_for_invalid_characters(self):

        msg = self._list.create('kate', "Back.to-School")
        self.assertEqual(msg, "Invalid characters")
    
    def test_already_existing_list(self):

        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Party'},{'user': 'dalton', 'name': 'Birthday'}]
        msg = self._list.create( "dalton", "Party")
        self.assertEqual(msg, "List already exists.")

if __name__ == '__main__':
    unittest.main()
