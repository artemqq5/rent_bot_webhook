from data.DefaultDataBase import DefaultDataBase
from data.constants.access import BANNED_APP_STATUS, ACTIVE_APP_STATUS


class AppRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def ban_app_by_bundle(self, bundle):
        query = "UPDATE `apps` SET `status` = %s WHERE `bundle` = %s;"
        return self._update(query, (BANNED_APP_STATUS, bundle))

    def get_app_by_bundle(self, bundle):
        query = "SELECT * FROM `apps` WHERE `bundle` = %s AND `status` = %s;"
        return self._select_one(query, (bundle, ACTIVE_APP_STATUS))

