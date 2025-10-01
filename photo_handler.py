from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import MANHWA_LIBRARY
from utils import create_manhwa_detail_menu

async def handle_manhwa_with_photo(query, context, manhwa_title):
    """معالجة المانهوا مع الصورة مع الحفاظ على عمل الأزرار"""
    try:
        info = MANHWA_LIBRARY[manhwa_title]
        
        # النص مع معلومات المانهوا
        manhwa_detail = f"🎨 **{manhwa_title}**\n\n"
        manhwa_detail += f"📊 الفصول: {info['chapters']}\n"
        manhwa_detail += f"📈 الحالة: {info['status']}\n\n"
        manhwa_detail += "🎯 **اختر الفصل الذي تريد قراءته:**\n\n➖➖➖➖➖➖➖➖➖"
        
        # إذا كانت هناك صورة، نرسلها في رسالة منفصلة أولاً
        if manhwa_title in MANHWA_LIBRARY and MANHWA_LIBRARY[manhwa_title].get('image_url'):
            image_url = MANHWA_LIBRARY[manhwa_title]['image_url']
            
            # إرسال الصورة في رسالة منفصلة
            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=image_url,
                caption=f"🎨 {manhwa_title} - الصورة التوضيحية",
                parse_mode='Markdown'
            )
        
        # ثم نعدل الرسالة الأصلية بالأزرار (هنا بتكون الأزرار شغالة)
        await query.edit_message_text(
            manhwa_detail,
            reply_markup=create_manhwa_detail_menu(manhwa_title),
            parse_mode='Markdown'
        )
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في معالجة المانهوا مع الصورة: {e}")
        # Fallback إلى الطريقة العادية
        await query.edit_message_text(
            manhwa_detail,
            reply_markup=create_manhwa_detail_menu(manhwa_title),
            parse_mode='Markdown'
        )
        return False