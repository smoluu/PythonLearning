# https://docs.python-telegram-bot.org/en/v20.7/index.html
import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import secrets


api_key = secrets.api_key

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
  sender_id = update.effective_chat.id
  if sender_id == 6947312024:
    await context.bot.send_message(chat_id=update._effective_chat.id, text=update.message.text[::-1])

if __name__ == "__main__":
  application = ApplicationBuilder().token(api_key).build()
  start_handler = CommandHandler("start",start)
  echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
  application.add_handler(start_handler)
  application.add_handler(echo_handler)
  application.run_polling()