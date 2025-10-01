import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler, MessageHandler, filters
from telegram.ext import CommandHandler

from config import TEXTS, ADMIN_ID, MANHWA_LIBRARY, SUBSCRIPTION_REQUIRED
from database import db
from utils import (
    create_main_menu, create_back_button, create_subscribe_keyboard,
    check_channel_subscription, create_manhwa_list_menu,
    create_manhwa_detail_menu, create_story_menu
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة أمر /start"""
    user = update.effective_user
    user_id = user.id
    
    print(f"🔍 مستخدم جديد: {user.first_name} (ID: {user_id})")
    
    db.add_user(user_id, user.username, user.first_name, user.last_name)
    
    is_subscribed = await check_channel_subscription(context.bot, user_id)
    db.update_subscription(user_id, is_subscribed)
    
    print(f"📊 نتيجة التحقق: {is_subscribed}")
    
    if is_subscribed:
        await update.message.reply_text(
            TEXTS["welcome"],
            reply_markup=create_main_menu(),
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text(
            TEXTS["subscribe_required"],
            reply_markup=create_subscribe_keyboard(),
            parse_mode='Markdown'
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة ضغطات الأزرار"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    data = query.data
    
    print(f"🔘 زر مضغوط: {data} من المستخدم {user_id}")
    
    # التحقق من الاشتراك
    if data != "check_subscription" and SUBSCRIPTION_REQUIRED:
        is_subscribed = await check_channel_subscription(context.bot, user_id)
        db.update_subscription(user_id, is_subscribed)
        
        if not is_subscribed:
            await query.edit_message_text(
                TEXTS["subscribe_required"],
                reply_markup=create_subscribe_keyboard(),
                parse_mode='Markdown'
            )
            return
    
    # معالجة الأزرار
    if data == "main_menu":
        await query.edit_message_text(
            TEXTS["welcome"],
            reply_markup=create_main_menu(),
            parse_mode='Markdown'
        )
    
    elif data == "check_subscription":
        is_subscribed = await check_channel_subscription(context.bot, user_id)
        db.update_subscription(user_id, is_subscribed)
        
        if is_subscribed:
            await query.edit_message_text(
                TEXTS["welcome"],
                reply_markup=create_main_menu(),
                parse_mode='Markdown'
            )
        else:
            await query.edit_message_text(
                "❌ **لم يتم الاشتراك بعد!**\n\nالرجاء الاشتراك في القناة أولاً",
                reply_markup=create_subscribe_keyboard(),
                parse_mode='Markdown'
            )
    
    elif data == "manga":
        await query.edit_message_text(
            "📚 **قسم المانجا**\n\nجاري التطوير...",
            reply_markup=create_back_button(),
            parse_mode='Markdown'
        )
    
    elif data == "manhwa":
        manhwa_text = "🎨 **قسم المانهوا**\n\n**المانهوا المتاحة:**\n\n"
        
        for i, (title, info) in enumerate(MANHWA_LIBRARY.items(), 1):
            manhwa_text += f"{i}. {title} - {info['chapters']} فصل\n"
        
        manhwa_text += "\n➖➖➖➖➖➖➖➖➖"
        
        await query.edit_message_text(
            manhwa_text,
            reply_markup=create_manhwa_list_menu(),
            parse_mode='Markdown'
        )
    
    elif data.startswith("manhwa_"):
        manhwa_key = data.replace("manhwa_", "")
        manhwa_title = manhwa_key.replace("_", " ")
        
        matching_titles = [title for title in MANHWA_LIBRARY.keys() if title.replace(" ", "_") == manhwa_key]
        
        if matching_titles:
            manhwa_title = matching_titles[0]
            info = MANHWA_LIBRARY[manhwa_title]
            
            # النص مع معلومات المانهوا
            manhwa_detail = f"🎨 **{manhwa_title}**\n\n"
            manhwa_detail += f"📊 الفصول: {info['chapters']}\n"
            manhwa_detail += f"📈 الحالة: {info['status']}\n\n"
            manhwa_detail += "🎯 **اختر الفصل الذي تريد قراءته:**\n\n➖➖➖➖➖➖➖➖➖"
            
            await query.edit_message_text(
                manhwa_detail,
                reply_markup=create_manhwa_detail_menu(manhwa_title),
                parse_mode='Markdown'
            )
        else:
            await query.edit_message_text(
                "❌ لم يتم العثور على المانهوا",
                reply_markup=create_back_button()
            )
    
    elif data.startswith("more_chapters_"):
        manhwa_key = data.replace("more_chapters_", "")
        manhwa_title = manhwa_key.replace("_", " ")
        
        matching_titles = [title for title in MANHWA_LIBRARY.keys() if title.replace(" ", "_") == manhwa_key]
        
        if matching_titles:
            manhwa_title = matching_titles[0]
            info = MANHWA_LIBRARY[manhwa_title]
            
            chapters_text = f"📚 **الفصول الإضافية لـ {manhwa_title}**\n\n"
            
            keyboard = []
            chapters_row = []
            
            for i in range(11, info['chapters'] + 1):
                chapters_row.append(InlineKeyboardButton(f"{i}", callback_data=f"chapter_{manhwa_key}_{i}"))
                if len(chapters_row) == 5:
                    keyboard.append(chapters_row)
                    chapters_row = []
            
            if chapters_row:
                keyboard.append(chapters_row)
            
            keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data=f"manhwa_{manhwa_key}")])
            
            await query.edit_message_text(
                chapters_text,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='Markdown'
            )
    
    elif data.startswith("story_"):
        manhwa_key = data.replace("story_", "")
        manhwa_title = manhwa_key.replace("_", " ")
        
        matching_titles = [title for title in MANHWA_LIBRARY.keys() if title.replace(" ", "_") == manhwa_key]
        
        if matching_titles:
            manhwa_title = matching_titles[0]
            info = MANHWA_LIBRARY[manhwa_title]
            
            story_text = f"📖 **قصة {manhwa_title}**\n\n"
            story_text += f"{info['description']}\n\n"
            story_text += f"📚 عدد الفصول: {info['chapters']}\n"
            story_text += f"⏳ الحالة: {info['status']}\n\n"
            story_text += "➖➖➖➖➖➖➖➖➖"
            
            await query.edit_message_text(
                story_text,
                reply_markup=create_story_menu(manhwa_title),
                parse_mode='Markdown'
            )
        else:
            await query.edit_message_text(
                "❌ لم يتم العثور على القصة",
                reply_markup=create_back_button()
            )
    
    elif data.startswith("chapter_"):
        parts = data.split("_")
        if len(parts) >= 3:
            manhwa_key = "_".join(parts[1:-1])
            chapter_num = parts[-1]
            manhwa_title = manhwa_key.replace("_", " ")
            
            await query.edit_message_text(
                f"📖 {manhwa_title} - الفصل {chapter_num}\n\nجاري التحميل...\n\n⚡ سيتم إضافة المحتوى قريباً!\n\n➖➖➖➖➖➖➖➖➖",
                reply_markup=create_back_button(),
                parse_mode='Markdown'
            )
    
    elif data == "request":
        context.user_data['waiting_for_request'] = True
        await query.edit_message_text(
            "📥 **طلب مادة جديدة**\n\nأرسل اسم المادة...",
            reply_markup=create_back_button(),
            parse_mode='Markdown'
        )
    
    elif data == "contact":
        await query.edit_message_text(
            TEXTS["contact_info"],
            reply_markup=create_back_button(),
            parse_mode='Markdown'
        )
    
    elif data == "watch_method":
        await query.edit_message_text(
            TEXTS["watch_method_text"],
            reply_markup=create_back_button(),
            parse_mode='Markdown'
        )
    
    else:
        await query.edit_message_text(
            "⚠️ الزر غير معروف",
            reply_markup=create_main_menu()
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if context.user_data.get('waiting_for_request'):
        request_text = update.message.text
        db.add_request(user_id, "طلب", request_text)
        
        if ADMIN_ID:
            await context.bot.send_message(
                ADMIN_ID,
                f"📥 طلب جديد من: @{update.effective_user.username}\n\n{request_text}"
            )
        
        await update.message.reply_text(
            "✅ تم استلام طلبك بنجاح!",
            reply_markup=create_back_button()
        )
        context.user_data['waiting_for_request'] = False
        return
    
    await update.message.reply_text(
        "استخدم الأزرار في القائمة للتنقل",
        reply_markup=create_main_menu()
    )

async def admin_board(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ ليس لديك صلاحية الوصول لهذا الأمر")
        return
    
    stats = db.get_user_stats()
    admin_text = f"""👑 لوحة الأدمن

📊 الإحصائيات:
👥 المستخدمين: {stats['total_users']}
✅ المشتركين: {stats['subscribed_users']}
📥 الطلبات: {stats['total_requests']}"""
    
    await update.message.reply_text(admin_text, parse_mode='Markdown')

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ ليس لديك صلاحية الوصول لهذا الأمر")
        return
    
    if not context.args:
        await update.message.reply_text("الاستخدام: /broadcast <الرسالة>")
        return
    
    message = " ".join(context.args)
    await update.message.reply_text(f"✅ تم إعداد رسالة البث: {message}")

def setup_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("board", admin_board))
    application.add_handler(CommandHandler("broadcast", broadcast))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))