""" TESTS FOR USER ACCOUNTS CLASS"""
import unittest
from app.accounts import Accounts

class AccountsTestCases(unittest.TestCase):
    """TESTS FOR LOGIN AND REGISTRATION MODULES"""
    def setUp(self):
        self.user = Accounts()
    
    def tearDown(self):
        del self.user
    
    def test_sucessful_login(self):
        """ TEST FOR SUCESSFUL LOGIN """
        self.user.list_of_accounts= [
            {'username': 'dalton', 'pwd': 'chromelegend', 'email': 'legionless@yahoo.com'}]
        msg = self.user.login( "legionless@yahoo.com", "chromelegend")
        self.assertEqual(msg, "Success!")
    
    def test_non_user_login(self):
        """CHECKING FOR LOGIN BY NON-USER"""
        self.user.list_of_accounts= [
            {'username': 'Parseen', 'pwd': 'mypassword', 'email': 'david.parseen@yahoo.com'}]
        msg = self.user.login( "nonuser@yahoo.com", "idontevenhaveone")
        self.assertEqual(msg, "Account not registered, sign up")
    
    def test_wrong_login_input(self):
        """CHECKING FOR WRONG INPUT"""
        self.user.list_of_accounts= [
            {'username': 'dalton', 'pwd': 'chromelegend', 'email': 'legionless@yahoo.com'}]
        msg = self.user.login( "legionless@yahoo.com", "legendchrome")
        self.assertEqual(msg, "Invalid email, password combination")
    
    
if __name__ == '__main__':
    unittest.main()
