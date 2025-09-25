import os
from dotenv import load_dotenv
from telegram import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Загружаем .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))  # если нужен, оставляем

# Клавиатура
def main_keyboard():
    kb = [
        [KeyboardButton(
            text="💎 Купить UC",
            web_app=WebAppInfo(url="https://donza-uc.vercel.app")
        )],
        [KeyboardButton(text="📞 Поддержка")]
    ]
    return ReplyKeyboardMarkup(kb, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать 🔥\n\n"
        "Самые лучшие UC по выгодным ценам только в Donza!\n\n"
        "Для покупки UC воспользуйся меню ниже.",
        reply_markup=main_keyboard()
    )

# Обработка кнопки «Поддержка»
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "📞 Поддержка":
        await update.message.reply_text("Напиши нашему саппорту: @Dimon_sopr")

def main():
    # Создаем приложение
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Хэндлеры
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, support))

    print("✅ Бот запущен…")
    application.run_polling()

if __name__ == "__main__":
    main()
