""" ACCOUNTS MANAGEMENT """

class Accounts(object):
    """ CLASS FOR ACCOUNT CREATION AND LOGIN"""
    def __init__(self):

        self.list_of_accounts = []
def login(self, email, pwd):
        """ Handles Login Requests"""
        for account in self.list_of_accounts:
            if email == account['email']:
                if pwd == account['pwd']:
                    return "Success!"
                else:
                    return "Invalid email, password combination"
        return "Account not registered, sign up"
