from environs import Env
import logging

# Чтение переменных окружения
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', # настраиваем вывод (как и что будем выводить)
    # level = logging.INFO # уровень логов (все или только основные)
    level = logging.DEBUG # уровень логов (все или только основные)
)