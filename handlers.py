from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN, main_menu_buttons, MANHWA_LIST
from utils import check_subscription, subscription_keyboard, share_keyboard
from database import DB_NAME, add_user, update_view, update_like, update_share, get_stats
import sqlite3
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

ADMIN_IDS = [6742773194 , 7356473972 , 7554849582]  # حط ID بتاعك

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username, user.first_name)
    welcome = f"👋 أهلاً بيك {user.first_name}!\n🌟 جاهز لمغامرة جديدة مع المانهوا؟"
    if not check_subscription(user.id, BOT_TOKEN):
        await update.message.reply_text(
            "⚠️ قبل ما نبدأ، اشترك في القناة الرسمية عشان تستمتع بكل المميزات 😊",
            reply_markup=subscription_keyboard()
        )
        return
    await update.message.reply_text(welcome, reply_markup=InlineKeyboardMarkup(main_menu_buttons))

async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    if not check_subscription(user.id, BOT_TOKEN):
        await query.message.reply_text("⚠️ لسه مش مشترك 😅", reply_markup=subscription_keyboard())
        return
    await query.message.reply_text("✅ تمام! اختار من القائمة:", reply_markup=InlineKeyboardMarkup(main_menu_buttons))

async def list_manhwa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    buttons = [[InlineKeyboardButton(m["title"], callback_data=f"manhwa_{k}")] for k, m in MANHWA_LIST.items()]
    buttons.append([InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="back_main")])
    await query.message.reply_text("📚 اختر المانهوا:", reply_markup=InlineKeyboardMarkup(buttons))

async def list_manga(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    message = (
        "📚✨ قسم المانجا لسه تحت التحضير 🙈💖\n\n"
        "⏳ قريب جدًا هتلاقي هنا مانجا مترجمة وحاجات جامدة 🔥📖\n"
        "خليك متابع معانا 👀!"
    )

    await query.edit_message_text(
        text=message,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 رجوع للقائمة الرئيسية", callback_data="back_main")]
        ])
    )

async def manhwa_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data.split("_")[1]
    update_view(key)
    manhwa = MANHWA_LIST.get(key)
    if not manhwa:
        await query.message.reply_text("❌ لم يتم العثور على هذه المانهوا.")
        return


    # تحضير أزرار الفصول 5×1
    chapters = manhwa.get("chapters", [])[:10]
    buttons = []
    for i in range(0, len(chapters), 5):
        row = [InlineKeyboardButton(f"الفصل {i+j+1}", url=link) for j, link in enumerate(chapters[i:i+5])]
        buttons.append(row)

    if len(manhwa.get("chapters", []))>10:
        buttons.append([InlineKeyboardButton("📂 المزيد", callback_data=f"more_{key}")])
    buttons.append([InlineKeyboardButton("📖 عرض القصة", callback_data=f"story_{key}")])
    buttons.append([InlineKeyboardButton("❤️ أعجبني", callback_data=f"like_{key}"), InlineKeyboardButton("🔗 شارك", callback_data=f"share_{key}")])
    buttons.append([InlineKeyboardButton("🔙 رجوع", callback_data="list_manhwa"), InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="back_main")])

    try:
        await query.message.delete()
    except: pass

    # إرسال الصورة أو الأنيميشن حسب توفر المفتاح media
    if "media" in manhwa:
        await context.bot.send_animation(
            chat_id=query.message.chat_id,
            animation=manhwa["media"],
            caption=f"📖 {manhwa['title']}\n🌟 {manhwa['genre']}\n📅 {manhwa['year']}",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    else:
        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=manhwa["image"],
            caption=f"📖 {manhwa['title']}\n🌟 {manhwa['genre']}\n📅 {manhwa['year']}",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

async def more_chapters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data.split("_")[1]
    manhwa = MANHWA_LIST.get(key)
    if not manhwa: return

    all_chapters = manhwa.get("chapters", [])
    buttons = []
    for i in range(0, len(all_chapters), 5):
        row = [InlineKeyboardButton(f"الفصل {i+j+1}", url=link) for j, link in enumerate(all_chapters[i:i+5])]
        buttons.append(row)

    buttons.append([InlineKeyboardButton("📖 عرض القصة", callback_data=f"story_{key}")])
    buttons.append([InlineKeyboardButton("🔙 رجوع", callback_data=f"manhwa_{key}"), InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="back_main")])

    try: await query.message.delete()
    except: pass

    if "media" in manhwa:
        await context.bot.send_animation(chat_id=query.message.chat_id, animation=manhwa["media"], caption=f"📚 كل فصول {manhwa['title']}:", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await context.bot.send_photo(chat_id=query.message.chat_id, photo=manhwa["image"], caption=f"📚 كل فصول {manhwa['title']}:", reply_markup=InlineKeyboardMarkup(buttons))

async def show_story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data.split("_")[1]
    manhwa = MANHWA_LIST.get(key)
    if not manhwa: return

    text = f"""⊱━━━━━⊰✾⊱━━━━━⊰
الاسم ~ [ {manhwa['title']} ]

الحالة ~ [ {manhwa.get('status','غير معروف')} ]

سنة الإصدار ~ [ {manhwa.get('year','غير معروف')} ]

القصة:
{manhwa.get('story','لا توجد قصة')}

مشاهدة ممتعة 
⊱━━━━━⊰✾⊱━━━━━⊰"""

    buttons = [[InlineKeyboardButton("🔙 رجوع", callback_data=f"manhwa_{key}")],
               [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="back_main")]]

    try: await query.message.delete()
    except: pass

    if "media" in manhwa:
        await context.bot.send_animation(chat_id=query.message.chat_id, animation=manhwa["media"], caption=text, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await context.bot.send_photo(chat_id=query.message.chat_id, photo=manhwa["image"], caption=text, reply_markup=InlineKeyboardMarkup(buttons))

async def like_manhwa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("❤️ تم تسجيل إعجابك!")
    key = query.data.split("_")[1]
    update_like(key)

async def share_manhwa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data.split("_")[1]
    update_share(key)
    # هنا نرسل رسالة مع رابط المشاركة (زرار موجود في utils.py)
    from utils import share_keyboard
    await query.message.reply_text(
        "شارك هذا البوت مع أصدقائك:👇",
        reply_markup=share_keyboard()
    )
async def back_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("🏠 رجعت للقائمة الرئيسية:", reply_markup=InlineKeyboardMarkup(main_menu_buttons))
async def notify_all(app, message: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    conn.close()

    for (user_id,) in users:
        try:
            await app.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"خطأ في إرسال الرسالة للمستخدم {user_id}: {e}")
async def notify_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ الأمر ده مخصص للأدمن فقط.")
        return

    if not context.args:
        await update.message.reply_text("⚠️ استخدم: /notify [الرسالة]")
        return

    message = " ".join(context.args)
    app = context.application
    await notify_all(app, f"📢 إشعار جديد:\n\n{message}")
    await update.message.reply_text("✅ تم إرسال الإشعار لكل المستخدمين.")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"🎥 File ID:\n{file_id}")
    else:
        await update.message.reply_text("❌ ابعت الفيديو كـ *فيديو* مش كرابط أو ملف.")
# أمر الأدمن لعرض الإحصائيات
# طريقة المشاهدة (فيديو تعليمي)
async def how_to_watch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        await query.message.reply_video(
            video="BAACAgQAAxkBAAICRmjdPSktnrfWGhRRA6IhA_aO4WNdAAIRHgACgjPoUn9NWNTJLOvmNgQ",
            caption="🎥 شرح طريقة المشاهدة خطوة بخطوة\n\nاستمتع ❤️"
        )
    except Exception as e:
        await query.message.reply_text(f"⚠️ حصل خطأ أثناء إرسال الفيديو: {e}")

async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id not in ADMIN_IDS:
        return

    total_users, manhwa_data = get_stats()
    text = f"📊 إحصائيات البوت:\n\n👤 عدد المستخدمين: {total_users}\n\n"
    for key, views, likes, shares in manhwa_data:
        title = MANHWA_LIST.get(key, {"title": key})["title"]
        text += f"📖 {title} - المشاهدات: {views}, الإعجابات: {likes}, المشاركات: {shares}\n"

    await context.bot.send_message(chat_id=user.id, text=text)
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", show_stats))
    app.add_handler(CallbackQueryHandler(check_sub, pattern="^check_subscription$"))
    app.add_handler(CallbackQueryHandler(list_manhwa, pattern="^list_manhwa$"))
    app.add_handler(CallbackQueryHandler(manhwa_details, pattern="^manhwa_"))
    app.add_handler(CallbackQueryHandler(more_chapters, pattern="^more_"))
    app.add_handler(CallbackQueryHandler(show_story, pattern="^story_"))
    app.add_handler(CallbackQueryHandler(like_manhwa, pattern="^like_"))
    app.add_handler(CallbackQueryHandler(share_manhwa, pattern="^share_"))
    app.add_handler(CallbackQueryHandler(back_main, pattern="^back_main$"))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", show_stats))
    app.add_handler(CommandHandler("notify", notify_command)) 
    app.add_handler(MessageHandler(filters.VIDEO, get_file_id))
    app.add_handler(CallbackQueryHandler(how_to_watch, pattern="^how_to_watch$"))
    app.add_handler(CallbackQueryHandler(list_manga, pattern="^list_manga$"))