from telebot import TeleBot, types
from studygram.settings import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)
bot.remove_webhook()
bot.set_webhook(url=f"https://a4785b96c9b6.ngrok.io/bot/")

print("Вебхук работает")

markup = types.InlineKeyboardMarkup()
