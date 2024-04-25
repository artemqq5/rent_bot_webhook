from data.constants.localization.uk import ban_app_uk
from data.constants.localization.en import ban_app_en

from data.constants.localization.ru import ban_app_ru


def app_ban_message(app_name, lang_key="en") -> str:
    if lang_key == "uk":
        return ban_app_uk(app_name)
    elif lang_key == "ru":
        return ban_app_ru(app_name)
    else:
        return ban_app_en(app_name)
