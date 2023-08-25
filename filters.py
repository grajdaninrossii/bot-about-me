from telegram.ext import filters
from constants import MainMenuButtonsText


get_selfi_filter = filters.Regex(f'^{MainMenuButtonsText.SELFI}') | filters.Regex(f"^1$")
get_photo_high_school_filter = filters.Regex(f'^{MainMenuButtonsText.HIGH_SCHOOL}') | filters.Regex(f"^2$")
get_bot_git_repo_filter = filters.Regex(f'^{MainMenuButtonsText.CODE}') | filters.Regex(f"^4")
get_info_filter = filters.Regex(f'^{MainMenuButtonsText.INFO}') | filters.Regex(f"^3")
get_hobby_post_filter = filters.Regex(f'^{MainMenuButtonsText.POST}$')

all_text_filter = filters.TEXT & ~filters.COMMAND