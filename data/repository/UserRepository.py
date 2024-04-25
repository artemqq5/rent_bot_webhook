from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def get_all_users(self):
        query = "SELECT * FROM `users` WHERE `banned` = 0;"
        return self._select(query)
