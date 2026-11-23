import os
import telebot
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "AlNoomi Bot is Running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك في بوت النعومي 🤖\nابعت اي رسالة وانا هرد عليك")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000))), daemon=True).start()
    bot.infinity_polling()
