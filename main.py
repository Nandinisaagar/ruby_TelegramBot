from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5353972776:AAGltvcxuaYxnCPjAsGyeo-CFoIzNzbxlfM",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hey! I am Ruby your stressbuster companion.Please write\
		/help to explore what we've got for you.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/ASMR - To get the Youtube link
	/SatisfyingVideo - To get the Youtube link
	/StandUp - To get the Youtube link
	/Surprise - To get the Youtube link""")


def ASMR_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"ASMR Link =>\
		https://youtu.be/yPH2VnnOK9o)")


def Satisfying_url(update: Update, context: CallbackContext):
	update.message.reply_text("Satisfying Video Link =>\
	https://youtu.be/VHB3_W8cTto/")


def StandUp_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"StandUp URL =>\
		https://youtu.be/E16WhXcIghM")


def Surprise_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Surprise URL => https://youtu.be/dQw4w9WgXcQ")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ASMR', ASMR_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('SatisfyingVideo', Satisfying_url))
updater.dispatcher.add_handler(CommandHandler('StandUp', StandUp_url))
updater.dispatcher.add_handler(CommandHandler('Surprise', Surprise_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
