"""TESTS FOR SHOPPING LISTS"""
import unittest
from app import shopping_lists
from datetime import date


class TestCasesShoppingList(unittest.TestCase):

    def setUp(self):
        self._list = shopping_lists.ShoppingLists()

    def tearDown(self):
        del self._list
    
    def test_sucessful_create(self):
        msg = self._list.create( "dalton", 'Party')
        self.assertEqual(
            msg, [{'user': 'dalton', 'name': 'Party','date': str(date.today())}])
    
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
        self.assertEqual(msg,'Rave has been Deleted')
         #[{'user': 'dalton', 'name': 'Party'}, {'user': 'dalton', 'name': 'Birthday'}]''')

if __name__ == '__main__':
    unittest.main()