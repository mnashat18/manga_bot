import os
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from database import init_db
from handlers import setup_handlers

if __name__ == "__main__":
    print("🚀 Starting bot initialization...")

    # إنشاء الجداول في قاعدة PostgreSQL (Neon)
    init_db()

    # تشغيل البوت
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)

    print("✅ Bot is running on Cyclic...")
    app.run_polling()
