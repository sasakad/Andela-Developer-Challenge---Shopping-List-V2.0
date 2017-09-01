""" ACCOUNTS MANAGEMENT """

class Accounts(object):
    """ CLASS FOR ACCOUNT CREATION AND LOGIN"""
    def __init__(self):

        self.list_of_accounts = []
    def get_uname_by_email(self, email):
        """Returns username when provided with email"""
        for account in self.list_of_accounts:
            if email == account['email']:
                return account['uname']

    def login(self, email, pwd):
            """Method for  Handling Login Requests"""
            for account in self.list_of_accounts:
                if email == account['email']:
                    if pwd == account['pwd']:
                        return "Success!"
                    else:
                        return "Invalid email, password combination"
            return "Account not registered, sign up"

    def registration(self, uname, email, pwd, pwd_confirm):
        """Method for creating new accounts."""
        dict_for_each_account = {}

        for account in self.list_of_accounts:
            if email == account['email']:
                return "Your Account Already Active. Proceed to login"
        else:
            if len(pwd) < 6:
                return "Password is too short"
            elif pwd == pwd_confirm:
                dict_for_each_account['uname'] = uname
                dict_for_each_account['email'] = email
                dict_for_each_account['pwd'] = pwd
                self.list_of_accounts.append(dict_for_each_account)
            else:
                return "Your passwords should match"
        return "Your account is now registered please proceed to login"