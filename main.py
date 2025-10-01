from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from database import init_db
from handlers import setup_handlers

if __name__ == "__main__":
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)

    print("🚀 Bot is running...")
    app.run_polling()
