import os
import logging
from telegram.ext import Application, CommandHandler

# توکن از متغیر محیطی می‌آید
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

async def start(update, context):
    await update.message.reply_text("🤖 ربات دمپایی‌یار فعال است!\n\nدستورات:\n/idea - ایده جدید\n/trend - ترندهای روز")

async def idea(update, context):
    ideas = [
        "💡 ایده: دمپایی اسپرت با کفی EVA و رنگ‌های روشن",
        "🎯 ایده: طراحی مینیمال با لوگوی برجسته", 
        "✨ ایده: ترکیب چرم مصنوعی و پارچه مشبک",
        "🚀 ایده: دمپایی راحتی با memory foam",
        "🌈 ایده: رنگ‌های گرادیانت روی کفی EVA"
    ]
    import random
    await update.message.reply_text(random.choice(ideas))

async def trend(update, context):
    trends = """
📊 ترندهای روز:

• رنگ: سبز زیتونی، آبی آسمانی
• متریال: EVA بافت دار، چرم بازیافتی
• طرح: بندهای کلفت، پاشنه قطور
• هشتگ: #SlideSandals2024
"""
    await update.message.reply_text(trends)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("idea", idea))
    app.add_handler(CommandHandler("trend", trend))
    
    print("✅ ربات روی سرور فعال شد!")
    app.run_polling()

if __name__ == '__main__':
    main()