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
		"Hey! I am Ruby your stress buster companion. Please write\
		/help to explore what we've got for you.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/ASMR 
	/SatisfyingVideo 
	/StandUp 
	/Movies 
	/Songs 
	/Podcast
	/AudioBook
	/YogaPoses
	/StressManagement
	/Tetris
	/TicTacToe 
	/DoodleJump 
	/FlappyBird 
	/DotandBoxes 
	/Pacman
	/Surprise """)


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


def Movies_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Movies URL => https://www.netflix.com/in/")


def Song_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Song URL => https://open.spotify.com")


def DoodleJump_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"DoodleJump URL => https://poki.com/en/g/doodle-jump")


def TicTacToe_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"TicTacToe URL => https://playtictactoe.org/")


def FlappyBird_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"FlappyBird URL => https://flappybird.io/")


def DotandBoxes_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"DotandBoxes URL => https://gametable.org/games/dots-and-boxes/")


def Pacman_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Pacman URL => https://pacman.live/")


def Podcast_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Podcast URL => https://manicpod.com/?gclid=Cj0KCQjwpImTBhCmARIsAKr58cwc2DolvwiZDavdYO0o8iXLMBvMjeQEWttw3J5rEdX3D4e2ZjYKkrEaAohZEALw_wcB")


def AudioBook_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"AudioBook URL => https://www.audible.in/?&source_code=IAATM1331130210024&gclid=Cj0KCQjwpImTBhCmARIsAKr58cz-afFDINz-4lIrgiE25lwRA3OD7dWZypDsq2EFW1gdN0X7pMkm4cAaAoJ1EALw_wcB")


def	Tetris_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Tetris URL = https://tetris.com/play-tetris")

def	YogaPoses_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"YogaPose URL = https://www.fountainhead.com.au/7-yoga-poses-for-stress-relief")


def	StressManagement_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"StressManagement URL = https://www.helpguide.org/articles/stress/stress-management.htm")

def sample_responses(input_text):
    user_message = str(input_text).lower()


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
updater.dispatcher.add_handler(CommandHandler('Surprise', Surprise_url))
updater.dispatcher.add_handler(CommandHandler('Movies', Movies_url))
updater.dispatcher.add_handler(CommandHandler('Song', Song_url))
updater.dispatcher.add_handler(CommandHandler('DoodleJump', DoodleJump_url))
updater.dispatcher.add_handler(CommandHandler('TicTacToe', TicTacToe_url))
updater.dispatcher.add_handler(CommandHandler('FlappyBird', FlappyBird_url))
updater.dispatcher.add_handler(CommandHandler('DotandBoxes', DotandBoxes_url))
updater.dispatcher.add_handler(CommandHandler('Pacman', Pacman_url))
updater.dispatcher.add_handler(CommandHandler('Podcast', Podcast_url))
updater.dispatcher.add_handler(CommandHandler('AudioBook', AudioBook_url))
updater.dispatcher.add_handler(CommandHandler('Tetris', Tetris_url))
updater.dispatcher.add_handler(CommandHandler('YogaPoses', YogaPoses_url))
updater.dispatcher.add_handler(CommandHandler('StressMangement', StressManagement_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
