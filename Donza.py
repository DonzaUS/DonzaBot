import os
from dotenv import load_dotenv
from telegram import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

def main_keyboard():
    kb = [
        [KeyboardButton(
            text="💎 Купить UC",
            web_app=WebAppInfo(url="https://donza-uc.vercel.app")
        )],
        [KeyboardButton(text="📞 Поддержка")]
    ]
    return ReplyKeyboardMarkup(kb, resize_keyboard=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Добро пожаловать 🔥\n\n"
        "Самые лучшие UC по выгодным ценам только в Donza!\n\n"
        "Для покупки UC воспользуйся меню ниже.",
        reply_markup=main_keyboard()
    )

def support(update: Update, context: CallbackContext):
    if update.message.text == "📞 Поддержка":
        update.message.reply_text("Напиши нашему саппорту: @Dimon_sopr")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, support))
    print("✅ Бот запущен…")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
 
