from enum import StrEnum
GREETING_TEXT = '''
Здравствуй мой друг. Рад видеть Вас здесь.
Меня зовут Мирослав Кузин, мне 22 года. При помощи данного бота Вы можете узнать обо мне чуть больше выше сказанного.
'''

MAIN_MENU_TEXT = '''
Здесь Вы можете:
1. Посмотреть мое последнее селфи
2. Фото из старшей школы
3. Получить информацию из голосового сообщения
4. Получить исходники бота
'''

CONVERSATION_MENU_TEXT = '''
1. Получить рассказ о GPT
2. Разница SQL и NoSQL
3. История первой любви
'''

LINK_BOT_REPOSITORY_TEXT = '''
...
'''

ABOUT_SELFI_TEXT = '''
Селфи из общежития:
'''

ABOUT_HIGH_SCHOOL_PHOTO_TEXT = '''
Фото с поездки в Гуамку:
'''

ERROR_VOICE_MENU_TEXT = '''
На данный момент вы находитесь в меню Inline-клавиатуры.
Просим Вас нажать на кнопки под сообщением выше!
'''


STORY_BUTTONS_TYPES = {
    "first_love": "Первая любовь",
    "about_SQL_NOSQL": "SQL и NOSQL",
    "about_GPT": "о GPT"
}



class MainMenuButtonsText(StrEnum):
    SELFI: str       = "Cелфи 🤳"
    INFO: str        = "Информация 💯"
    CODE: str        = "Код бота 📔"
    HIGH_SCHOOL: str = "Cтаршая школа 📸"


class StoryTypesButtonsText(StrEnum):
    LOVE: str       = "Первая любовь"
    SQL_NOSQL: str        = "SQL и NOSQL"
    GPT: str = "о GPT"
    BACK_BUTTON_TEXT = 'Назад ⬅'