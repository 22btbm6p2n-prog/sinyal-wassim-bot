import telebot
import os

# التوكن الخاص بك الذي أرسلته
TOKEN = "8929649925:AAGl3qoIKKkovo20_8bOdzS6Q5g9dB99ou4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "أهلاً بك في بوت تحليل الإشارات والذهب (XAUUSD)!\n"
        "أرسل لي صورة الشارت (Grafique) لأقوم بتحليلها وإعطائك التوصيات."
    )

# استقبال صور الشارتات وتحليلها
@bot.message_handler(content_types=['photo'])
def handle_chart_image(message):
    bot.reply_to(
        message, 
        "🔍 جاري استلام الشارت وتحليل المؤشرات الفنية (RSI ومناطق الدعم والمقاومة)...\n"
        "يرجى الانتظار قليلاً لإرسال الإشارة."
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "يرجى إرسال صورة الشارت (Grafique) الخاص بالزوج أو الذهب للبدء بالتحليل.")

bot.infinity_polling()
