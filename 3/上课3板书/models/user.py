from models import Model
from utils import log

class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def validate_login(self):
        list=self.all()
        for i in list:
            if self.username==i.username and self.password==i.password:
                return True
        return False

        # return self.username == 'gua' and self.password == '123'

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2
