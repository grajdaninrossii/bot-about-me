from telegram import InputFile, ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler
from telegram.constants import ParseMode
import aiofiles
import asyncio

from constants import (
    ERROR_VOICE_MENU_TEXT,
    GREETING_TEXT,
    LINK_BOT_REPOSITORY_TEXT,
    MAIN_MENU_TEXT,
    ABOUT_SELFI_TEXT,
    ABOUT_HIGH_SCHOOL_PHOTO_TEXT
)
from constants import StoryTypesButtonsText
from keyboards import main_menu_keyboard, voice_inline_keyboard
from keyboards import MAIN_MENU_KEY, VOICE_KEY



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Стартовая точка входа в приложение

    Args:
        update (Update): Объект обновления, где в том числе хранится информация о пользователе
        context (ContextTypes.DEFAULT_TYPE): контекст бота
    """

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=GREETING_TEXT,
        parse_mode=ParseMode.HTML
        )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MAIN_MENU_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=main_menu_keyboard
        )
    return MAIN_MENU_KEY


async def get_selfi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=ABOUT_SELFI_TEXT,
        parse_mode=ParseMode.HTML
        )
    async with aiofiles.open("./files/selfi.jpg", "rb") as fl:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=await fl.read(),
            )
    # await asyncio.sleep(1)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MAIN_MENU_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=main_menu_keyboard
        )
    return MAIN_MENU_KEY


async def get_photo_high_school(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=ABOUT_HIGH_SCHOOL_PHOTO_TEXT,
        parse_mode=ParseMode.HTML
        )
    async with aiofiles.open("./files/high_school.jpg", "rb") as fl:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=await fl.read(),
            )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MAIN_MENU_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=main_menu_keyboard
        )
    return MAIN_MENU_KEY


async def get_bot_git_repo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=LINK_BOT_REPOSITORY_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=main_menu_keyboard
        )
    return MAIN_MENU_KEY


async def get_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.message.reply_text("Выберите голосовое сообщение", reply_markup=voice_inline_keyboard)
    return VOICE_KEY


def get_voice_story(type_story: str) -> str:
    async def get_one_voice_story(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
        query = update.callback_query
        await query.answer()

        bot_answer_filename: str = "./files"
        bot_answer_text = ""
        match type_story:
            case StoryTypesButtonsText.LOVE:
                bot_answer_filename += '/about_first_love.ogg'
                bot_answer_text = 'Голосовое сообщение о первой любви:'
            case StoryTypesButtonsText.GPT:
                bot_answer_filename += '/about_gpt.ogg'
                bot_answer_text = 'Голосовое сообщение о том, что такое GPT:'
            case StoryTypesButtonsText.SQL_NOSQL:
                bot_answer_filename += '/about_sql_no_sql.ogg'
                bot_answer_text = 'Голосовое сообщени, в котором в двух словах поясняется разница между Sql и NoSql базами данных:'

        context.user_data['type_voice'] = bot_answer_text # Сохраняем информацию о голосовом сообщении

        # Отправка голосового сообщения
        async with aiofiles.open(bot_answer_filename, 'rb') as voice:
            msg = await context.bot.send_voice(
                chat_id=update.effective_chat.id,
                voice=InputFile(await voice.read(), filename=None)
            )
            if context.user_data.get("voice_menu_msg_id", None) is None:
                context.user_data['voice_menu_msg_id'] = msg.id # Сохраняем id msg. В дальнешйем пригодится для обновления голосвых соощений
            else:
                # Удаляем старое сообщение
                await context.bot.delete_message(
                    chat_id=update.effective_chat.id,
                    message_id=context.user_data['voice_menu_msg_id']
                )
                # Сохраняем новое в user_data
                context.user_data['voice_menu_msg_id'] = msg.id
        return VOICE_KEY
    return get_one_voice_story


async def back_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=context.user_data.get('type_voice', "..."), reply_markup=None)
    await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=MAIN_MENU_TEXT,
                parse_mode=ParseMode.HTML,
                reply_markup=main_menu_keyboard
            )

    # Удаляем меню голосовых сообщений
    context.user_data.pop('voice_menu_msg_id', None)
    context.user_data.pop('type_voice', None)
    return MAIN_MENU_KEY


async def error_voice_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=ERROR_VOICE_MENU_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove()
        )
    return VOICE_KEY