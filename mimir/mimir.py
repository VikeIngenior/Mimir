from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Application, ContextTypes, MessageHandler, Updater, filters

async def start(update: Update, context: CallbackQueryHandler) -> None:

    await update.message.reply_text("Step forth, seeker—if wisdom is your mead, drink deep, but know its cost.")