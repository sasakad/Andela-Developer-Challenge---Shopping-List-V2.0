""" TESTS FOR USER ACCOUNTS CLASS"""
import unittest
from app import accounts

class AccountsTestCases(unittest.TestCase):
    """TESTS FOR LOGIN AND REGISTRATION MODULES"""
    def setUp(self):
        self.user = accounts.Accounts()
    
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
    
    def test_sucess(self):
        """CHECKING FOR SUCESSFUL REGISTRATION"""
        msg = self.user.registration( 
            "MrShort", "MrShort@yahoo.com", "notshort", "notshort")
        self.assertEqual(msg, "Your account is now registered please proceed to login")
    
    def test_if_pwd_equals_confirmed(self):
        """ CHECKING IF BOTH PASSWORD AND CONFIRMED PASSWORD ARE THE SAME"""
        msg = self.user.registration( 
        "Githeri", "githeri.man@yahoo.com", "iwantgitheri", "iwantsgitheri")
        self.assertEqual(msg, "Your passwords should match")

    def test_already_existing_user(self):
        """CHECKING IF USER DETAILS ALREADY EXIST"""
        self.user.registration(
            "Githeri", "githeri.man@yahoo.com", "iwantgitheri", "iwantgitheri")
        msg = self.user.registration( 
        "Githeri", "githeri.man@yahoo.com", "iwantgitheri", "iwantgitheri")
        self.assertEqual(msg, "Your Account Already Active. Proceed to login")

    def test_short_pwd(self):
        """CHECKING FOR LESS THAN 6 CHARACTERS IN PASSWORD"""
        msg = self.user.registration(
            "MrShort", "MrShort@yahoo.com", "short", "short")
        self.assertEqual(
            msg, "Password is too short")


if __name__ == '__main__':
    unittest.main()
