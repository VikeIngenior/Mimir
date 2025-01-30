from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Application, ContextTypes, MessageHandler, Updater, filters
from urllib3.response import HAS_ZSTD

from ai_agent.mimir_agent import MyAIAgent

from dotenv import load_dotenv

import os

load_dotenv()

API_TOKEN = os.environ['API_TOKEN']
agent = MyAIAgent()

async def start(update: Update, context: CallbackQueryHandler) -> None:

    await update.message.reply_text("Step forth, seeker—if wisdom is your mead, drink deep, but know its cost.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """I heed these summons:\n/start – The journey begins, the path unwinds.
        \n/help – Seek guidance, and I shall whisper the way.
        """
    )

async def handle_message(update: Update, context) -> None:
    user_message = update.message.text
    bot_response = agent.get_response(user_message)
    await update.message.reply_text(bot_response)


def runner():
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    application.run_polling()