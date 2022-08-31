from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import json
import requests
from datetime import datetime
import os

TOKEN = "5352912214:AAGrhEjJz0NOeyGY7QHrzk0w9iyfw16nQrw"
updater = Updater(TOKEN, use_context = True)
dispatcher = updater.dispatcher

def format_update_to_dict(update):
    data = str(update).replace("'",'"').replace('False','false').replace('True','true') # convert update type to string type and replace some charactors to suitable with JSON form
    data = json.loads(data) #convert string to dict type
    return data


def help(update, context):
    update.message.reply_text("There are all available commands: hi, message_count, id, name, photo, meme, gif, dice, slot_machine, darts, basketball, football, bowling")

def hi(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text("Hello " + data["message"]["from"]['first_name'] + "!")

def message_count(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text("There are " + str(data['message']['message_id']) + " messages in this chat")

def id(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + "'s ID is " + str(data['message']['from']['id']))

def name(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text("Your full name is " + data['message']['from']['first_name'] + " " + data['message']['from']['last_name'])

def photo(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + ", here is a random photo:")
    update.message.reply_photo('https://picsum.photos/200/300/?random&rnd' + str(datetime.now()))

def meme(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + ", here is a random meme:")
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    photo = response.json()["url"]
    update.message.reply_photo(photo)

def gif(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + ", here is a random gif:")
    gif = requests.get('https://api.giphy.com/v1/gifs/random?api_key=tibAOxCdFsSjFU1Jx8NASyofVz42mjwA')
    gif = gif.json()['data']['images']['looping']['mp4']
    update.message.reply_animation(gif)

def dice(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + " start rolling dice:")
    update.message.reply_dice(emoji="🎲")

def slot_machine(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + " start using slot machine :")
    update.message.reply_dice(emoji="🎰")

def darts(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + " start playing darts:")
    update.message.reply_dice(emoji="🎯")

def basketball(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + " start playing basketball:")
    update.message.reply_dice(emoji="🏀")

def football(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + " start playing football:")
    update.message.reply_dice(emoji="⚽")

def bowling(update, context):
    data = format_update_to_dict(update)
    update.message.reply_text(data['message']['from']['first_name'] + " start playing bowling:")
    update.message.reply_dice(emoji="🎳")


dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("hi", hi))
dispatcher.add_handler(CommandHandler("message_count", message_count))
dispatcher.add_handler(CommandHandler("id", id))
dispatcher.add_handler(CommandHandler("name", name))
dispatcher.add_handler(CommandHandler("photo", photo))
dispatcher.add_handler(CommandHandler("meme", meme))
dispatcher.add_handler(CommandHandler("gif", gif))
dispatcher.add_handler(CommandHandler("dice", dice))
dispatcher.add_handler(CommandHandler("slot_machine", slot_machine))
dispatcher.add_handler(CommandHandler("darts", darts))
dispatcher.add_handler(CommandHandler("basketball", basketball))
dispatcher.add_handler(CommandHandler("football", football))
dispatcher.add_handler(CommandHandler("bowling", bowling))

updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=TOKEN,
                      webhook_url='https://telegram-bot-hiep.herokuapp.com/' + TOKEN
                      )