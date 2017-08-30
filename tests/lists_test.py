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
    def test_successful_editing_list(self):

        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Party'}]
        msg = self._list.edit(
            'Birthday', 'Party', "dalton")
        self.assertEqual(msg, [{'user': 'dalton', 'name': 'Birthday'}])

    def test_edit_already_existing_list(self):

        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Party'}, {
            'user': 'dalton', 'name': 'Birthday'}]
        msg = self._list.edit(
            'Birthday', 'Party', "dalton")
        self.assertEqual(msg, "Shopping list name already exists")
    def test_delete_shoppinglist(self):
        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Rave'}, {
            'user': 'dalton', 'name': 'Party'}, {'user': 'dalton', 'name': 'Birthday'}]
        msg = self._list.delete(
            'Rave', "dalton")
        self.assertEqual(msg, [{
            'user': 'dalton', 'name': 'Party'}, {'user': 'dalton', 'name': 'Birthday'}])

if __name__ == '__main__':
    unittest.main()
