"""TESTS FOR SHOPPING LISTS"""
import unittest
from datetime import date
from app import shopping_lists



class TestCasesShoppingList(unittest.TestCase):
    """TESTS FOR SHOPPING LIST FN BEHAVIOR"""

    def setUp(self):
        self._list = shopping_lists.ShoppingLists()

    def tearDown(self):
        del self._list

    def test_sucessful_create(self):
        """"TEST FOR SUCESSFUL CREATION OF A SHOPPING LIST"""
        msg = self._list.create("dalton", 'Party')
        self.assertEqual(msg, [{'user': 'dalton',
                                'name': 'Party',
                                'date': str(date.today())}])

    def test_for_invalid_characters(self):
        """CHECKS BEHAVIOUR ON INVALID CHARACTERS"""
        msg = self._list.create('kate', "Back.to-School")
        self.assertEqual(msg, "Invalid characters")

    def test_already_existing_list(self):
        """CHECKS BEHAVIOUR ON TRYING TO CREATE AN EXISTING LIST"""

        self._list.list_of_shopping_lists = [{'user': 'dalton',
                                              'name': 'Party'},
                                             {'user': 'dalton',
                                              'name': 'Birthday'}]
        msg = self._list.create("dalton", "Party")
        self.assertEqual(msg, "List already exists.")
    def test_successful_editing_list(self):
        """CHECKS FOR SUCCESSFUL LIST NAME EDITING"""
        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Party'}]
        msg = self._list.edit(
            'Birthday', 'Party', "dalton")
        self.assertEqual(msg, [{'user': 'dalton', 'name': 'Birthday'}])

    def test_edit_already_existing_list(self):
        """CHECKS BEHAVIOUR WHEN TRYING TO CHANGE NAME TO AN ALREADY EXISTING LIST"""
        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Party'}, {
            'user': 'dalton', 'name': 'Birthday'}]
        msg = self._list.edit(
            'Birthday', 'Party', "dalton")
        self.assertEqual(msg, "Name already used on another list")
    def test_delete_shoppinglist(self):
        """CHECKS FOR SUCCESSFUL DELETION"""
        self._list.list_of_shopping_lists = [{'user': 'dalton', 'name': 'Rave'},
                                             {'user': 'dalton', 'name': 'Party'},
                                             {'user': 'dalton', 'name': 'Birthday'}]
        msg = self._list.delete(
            'Rave', "dalton")
        self.assertEqual(msg, 'Rave has been Deleted')


if __name__ == '__main__':
    unittest.main()
