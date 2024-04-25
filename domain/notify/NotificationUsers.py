import requests

from config import BOT_TOKEN
from data.constants.localization.default_locale import app_ban_message
from data.repository.UserRepository import UserRepository


class NotificationUsers:

    def __init__(self):
        self.__url_send_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    # Розсилка всім про бан додатку
    def ban_application_notify(self, application):
        users = UserRepository().get_all_users()

        counter = 0

        for user in users:
            try:
                message = app_ban_message(app_name=application['name'], lang_key=user['lang'])
                json_data_pass = {
                    "chat_id": user['telegram_id'],
                    "caption": message,
                    "photo": application['image'],
                    "parse_mode": "HTML"}
                requests.request(method='POST', url=self.__url_send_photo, data=json_data_pass)

                counter += 1
            except Exception as e:
                print(f"ban application: {e}")

        print(f"notification ban application: {counter}/{len(users)}")
