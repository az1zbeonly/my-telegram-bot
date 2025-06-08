from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Assalomu alaykum! Men Telegram botman.")

def help_command(update, context):
    update.message.reply_text("Savolingiz bormi? Menga /start yuboring.")

def main():
    updater = Updater("7973964835:AAFx-ZEPCzisyA-xvpqDnTci37ZaGcdBXvA", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
