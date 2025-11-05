import os
import random
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv('TOKEN')

async def start(update, context):
    print("🎯 کاربر /start فرستاد")
    await update.message.reply_text("🤖 ربات DampaaAssistant فعال شد!\n\nدستورات:\n/idea - ایده جدید\n/trend - ترندهای روز")

async def idea(update, context):
    print("💡 کاربر /idea فرستاد")
    ideas = [
        "💡 ایده: دمپایی اسپرت با کفی EVA و رنگ آبی",
        "🎯 ایده: طراحی مینیمال با لوگوی برجسته",
        "✨ ایده: ترکیب چرم مصنوعی و پارچه مشبک",
        "🚀 ایده: دمپایی راحتی با memory foam"
    ]
    await update.message.reply_text(random.choice(ideas))

async def trend(update, context):
    print("📊 کاربر /trend فرستاد")
    await update.message.reply_text("📊 ترندهای روز:\n• رنگ: آبی آسمانی\n• متریال: EVA\n• طرح: مینیمال\n• سبک: اسپرت")

def main():
    print("🔑 در حال راه‌اندازی ربات DampaaAssistant...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("idea", idea))
    app.add_handler(CommandHandler("trend", trend))
    
    print("✅ ربات DampaaAssistant فعال شد!")
    app.run_polling()

if __name__ == '__main__':
    main()
