from data.DefaultDataBase import DefaultDataBase
from data.constants.access import BANNED_APP_STATUS


class AppRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def ban_app_by_id(self, flow_id):
        query = "UPDATE `apps` SET `status` = %s WHERE `id` = %s;"
        return self._update(query, (BANNED_APP_STATUS, flow_id))

    def get_app_by_id(self, flow_id):
        query = "SELECT * FROM `apps` WHERE `id` = %s;"
        return self._select_one(query, (flow_id,))

