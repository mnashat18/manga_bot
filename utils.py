import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import REQUIRED_CHANNELS

def check_subscription(user_id, bot_token):
    for channel in REQUIRED_CHANNELS:
        url = f"https://api.telegram.org/bot{bot_token}/getChatMember"
        params = {"chat_id": channel["id"], "user_id": user_id}
        resp = requests.get(url, params=params).json()
        try:
            status = resp["result"]["status"]
            if status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True

def subscription_keyboard():
    buttons = [
        [InlineKeyboardButton(ch["name"], url=f"https://t.me/{ch['id'].lstrip('@')}")]
        for ch in REQUIRED_CHANNELS
    ]
    buttons.append([InlineKeyboardButton("✅ اشتركت", callback_data="check_subscription")])
    return InlineKeyboardMarkup(buttons)

def share_keyboard():
    # زر المشاركة باسم البوت الخاص بك
    share_url = (
        "https://t.me/share/url?"
        "url=https://t.me/virus_teambot"
        "&text=🔥 جرب أقوى بوت مانهوات على تليجرام! 😍\n"
        "📚 اكتشف المانهوات الجديدة واستمتع بالمشاهدة مجانًا ❤️"
    )
    buttons = [
        [InlineKeyboardButton("🔗 شارك البوت مع أصدقائك", url=share_url)],
        [InlineKeyboardButton("🏠 العودة للقائمة الرئيسية", callback_data="back_main")]
    ]
    return InlineKeyboardMarkup(buttons)

def like_keyboard(key):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("❤️ أعجبني", callback_data=f"like_{key}")],
        [InlineKeyboardButton("🏠 العودة للقائمة الرئيسية", callback_data="back_main")]
    ])
