from telegram.ext import PicklePersistence, Application
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram import Update
import logging

from setting import BOT_TOKEN
from handlers import (
    start,
    get_selfi,
    get_photo_high_school,
    get_bot_git_repo,
    get_info,
    get_voice_story,
    back_main_menu,
    error_voice_menu,
    get_hobby_post
)
from keyboards import MAIN_MENU_KEY, VOICE_KEY
from constants import StoryTypesButtonsText
from filters import (
    get_selfi_filter,
    get_photo_high_school_filter,
    get_bot_git_repo_filter,
    get_info_filter,
    all_text_filter,
    get_hobby_post_filter
)


def main() -> None:
    '''
    Мы создаем объект приложения (он связывает все вместе и следит за обновлениями с помощью Updater), закидываем туда токен и
    вызываем метод build, чтобы запустить нашего красавчика бота.
    В строке кода ниже автоматически настраиваются:
    - Updater доступный как application.updater (прием данных от ТГ боту)
    - Bot доступный как application.bot/application.updater.bot (более высокий уровень доступа к методам Bot API)
    - BaseRequest объект инициализирутся и готов к использованию под application.bot (отвечает за обработку фактических сетевых данных, т.е. отправку запросов в API бота)
    - различные другие компоненты, значения в которых также устанавливаются по-умолчанию.
    '''

    persistence = PicklePersistence(filepath="bot_about_me")
    application = Application.builder().token(BOT_TOKEN).persistence(persistence).build()

    logger = logging.getLogger(__name__)
    logger.info("Hello, I'm work!")


    conv_handler = ConversationHandler(
        # Вход в разговор
        entry_points=[CommandHandler('start', start)],
        states={
            MAIN_MENU_KEY: [
                    MessageHandler(get_selfi_filter, get_selfi),
                    MessageHandler(get_photo_high_school_filter, get_photo_high_school),
                    MessageHandler(get_bot_git_repo_filter, get_bot_git_repo),
                    MessageHandler(get_info_filter, get_info),
                    MessageHandler(get_hobby_post_filter, get_hobby_post)
                ],
            VOICE_KEY: [
                CallbackQueryHandler(
                    get_voice_story(StoryTypesButtonsText.LOVE),
                    pattern=f"^{StoryTypesButtonsText.LOVE}$"
                    ),
                CallbackQueryHandler(
                    get_voice_story(StoryTypesButtonsText.GPT),
                    pattern=f"^{StoryTypesButtonsText.GPT}$"
                    ),
                CallbackQueryHandler(
                    get_voice_story(StoryTypesButtonsText.SQL_NOSQL),
                    pattern=f"^{StoryTypesButtonsText.SQL_NOSQL}$"
                    ),
                CallbackQueryHandler(
                    back_main_menu,
                    pattern=f"^{StoryTypesButtonsText.BACK_BUTTON_TEXT}$"
                    ),
                MessageHandler(all_text_filter, error_voice_menu)
            ]
            },
        fallbacks=[],
        name="general_conversation",
        persistent = True,
    )

    # Прикрепляем наш обработчик к приложению
    application.add_handler(conv_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()