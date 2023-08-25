from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup # для универсальности версий
from constants import MainMenuButtonsText, StoryTypesButtonsText

# Ключи состояний
MAIN_MENU_KEY="1"
VOICE_KEY="2"

'''
Для каждой клавиатуры отдельно создается список кнопок,
после создается объект клавиатуры в котором указываем расположения кнопок(меняем список кнопок по строкам)
и указываем resize_keyboard=True, чтобы клавиатура стала меньше (ее размер адаптируется)
'''

main_menu_buttons = [
    KeyboardButton(MainMenuButtonsText.SELFI),
    KeyboardButton(MainMenuButtonsText.POST),
    KeyboardButton(MainMenuButtonsText.CODE),
    KeyboardButton(MainMenuButtonsText.INFO),
    KeyboardButton(MainMenuButtonsText.HIGH_SCHOOL)
]

# Клавиатура основного меню
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        main_menu_buttons[:3],
        main_menu_buttons[3:]
        ],
    resize_keyboard=True
)

voice_menu_buttons = [
    InlineKeyboardButton(StoryTypesButtonsText.LOVE, callback_data=StoryTypesButtonsText.LOVE),
    InlineKeyboardButton(StoryTypesButtonsText.GPT, callback_data=StoryTypesButtonsText.GPT),
    InlineKeyboardButton(StoryTypesButtonsText.SQL_NOSQL, callback_data=StoryTypesButtonsText.SQL_NOSQL),
    InlineKeyboardButton(StoryTypesButtonsText.BACK_BUTTON_TEXT, callback_data=StoryTypesButtonsText.BACK_BUTTON_TEXT)
]

# Встроенная клавиатура меню голосовых сообщений(войсов)
voice_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        voice_menu_buttons[:2],
        voice_menu_buttons[2:]
    ]
)