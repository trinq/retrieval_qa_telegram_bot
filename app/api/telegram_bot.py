import os
import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
K = int(os.getenv("K", 5))
BASE_URL = os.getenv("BASE_URL")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")

def handle_message(update, context):
    message_text = update.message.text
    response = requests.get(f"{BASE_URL}/query_vector_store", params={"question": message_text}).json()
    response_text = "Top results:\n\n"
    for result in response:
        response_text += f"{result['text']} ({result['score']:.4f})\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
