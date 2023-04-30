import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from app.api.retrieval import get_answer

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = "your_bot_token_here"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I am your Retrieval-Augmented Generation Q&A bot. Ask me any question!")


def ask_question(update: Update, context: CallbackContext) -> None:
    user_query = update.message.text
    answer = get_answer(user_query)
    update.message.reply_text(answer)


def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ask_question))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
