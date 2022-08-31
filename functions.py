import os
import requests
import json
from datetime import datetime

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

# token that we get from the BotFather
TOKEN = "5352912214:AAGrhEjJz0NOeyGY7QHrzk0w9iyfw16nQrw"


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Reading the JSON format when we send the text message and extracting the chat id of the user and the text that user send to the bot
def tel_parse_data(message):
    print("message-->", message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
        return message
    except Exception as ex:
        print("ERROR: NO DATA FOUND ", ex)

    # try:
    #     cha_id = message['callback_query']['from']['id']
    #     i_txt = message['callback_query']['data']
    #     print("cha_id-->", cha_id)
    #     print("i_txt-->", i_txt)

    #     return cha_id, i_txt
    # except:
    #     pass

# remove punctuation and lowercase the message
def format_parsed_message(message):
    punctuation = [',', '.', r'/', ';', "'", '[', ']', '~', '!', '@', '%', '^', '&', '*', '+', '-', '=', 'Ơ', ':', '|', '<', '>', '?']
    for i in punctuation:
        message = message.replace(i,'')
    return message.lower()


# Get the Text message response from the bot
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=payload)
    return r




# Reading the JSON message when the user send any type of file to the bot and extracting the chat id of the user and the file id for the file that user send to the bot
def tel_parse_get_message(message):
    print("message-->", message)

    try:  # if the file is an image
        g_chat_id = message['message']['chat']['id']
        g_file_id = message['message']['photo'][0]['file_id']
        print("g_chat_id-->", g_chat_id)
        print("g_image_id-->", g_file_id)

        return g_file_id
    except:
        try:  # if the file is a video
            g_chat_id = message['message']['chat']['id']
            g_file_id = message['message']['video']['file_id']
            print("g_chat_id-->", g_chat_id)
            print("g_video_id-->", g_file_id)

            return g_file_id
        except:
            try:  # if the file is an audio
                g_chat_id = message['message']['chat']['id']
                g_file_id = message['message']['audio']['file_id']
                print("g_chat_id-->", g_chat_id)
                print("g_audio_id-->", g_file_id)

                return g_file_id
            except:
                try:  # if the file is a document
                    g_chat_id = message['message']['chat']['id']
                    g_file_id = message['message']['document']['file_id']
                    print("g_chat_id-->", g_chat_id)
                    print("g_file_id-->", g_file_id)

                    return g_file_id
                except:
                    print("NO file found found-->>")


# Get the Image response from the bot by providing the image link
def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': 'https://picsum.photos/200/300/?random&rnd' + str(datetime.now())
    }
    r = requests.get(url, json=payload)
    print("DATA: ", r)
    return r

# Get the Image response from the bot by providing the image link
def tel_send_meme(chat_id):
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    photo = response.json()["url"]
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': photo
    }
    r = requests.get(url, json=payload)
    print("DATA: ", r)
    return r

# Get the Image response from the bot by providing the image link
def tel_send_dice(chat_id, dice):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    payload = {
        'chat_id': chat_id,
        'emoji': dice
    }
    r = requests.get(url, json=payload)
    print("DATA: ", r)
    return r

# Get the Image response from the bot by providing the image link
def tel_send_gif(chat_id):
    gif = requests.get('https://api.giphy.com/v1/gifs/random?api_key=tibAOxCdFsSjFU1Jx8NASyofVz42mjwA')
    gif = gif.json()['data']['images']['looping']['mp4']
    url = f'https://api.telegram.org/bot{TOKEN}/sendAnimation'
    payload = {
        'chat_id': chat_id,
        'animation': gif
    }
    r = requests.post(url, json=payload)
    return r


# Get the Poll response from the bot
def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        "question": "In which direction does the sun rise?",
        # options are provided in json format
        "options": json.dumps(["North", "South", "East", "West"]),
        "is_anonymous": False,
        "type": "quiz",
        # Here we are providing the index for the correct option(i.e. indexing starts from 0)
        "correct_option_id": 2
    }
    r = requests.post(url, json=payload)
    return r


# Get the Button response in the keyboard section
def tel_send_button(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "What is this?",    # button should be in the propper format as described
        'reply_markup': {
            'keyboard': [[
                {
                    'text': 'supa'
                },
                {
                    'text': 'mario'
                }
            ]]
        }
    }
    r = requests.post(url, json=payload)
    return r


# Get the Inline button response
def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "What is this?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "A",
                    "callback_data": "ic_A"
                },
                {
                    "text": "B",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r


# Get the Button response from the bot with the redirected URL
def tel_send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Which link would you like to visit?",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "google", "url": "http://www.google.com/"},
                    {"text": "youtube", "url": "http://www.youtube.com/"}
                ]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r


# Get the Audio response from the bot by providing the URL for the audio
def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'

    payload = {
        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp3",
    }
    r = requests.post(url, json=payload)
    return r


# Get the Document response from the bot by providing the URL for the Document
def tel_send_document(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

    payload = {
        'chat_id': chat_id,
        "document": "http://www.africau.edu/images/default/sample.pdf",
    }
    r = requests.post(url, json=payload)
    return r


# Get the Video response from the bot by providing the URL for the Video
def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'

    payload = {
        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4",
    }
    r = requests.post(url, json=payload)
    return r


# Get the url for the file through the file id
def tel_upload_file(file_id):
    # Getting the url for the file
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("json_resp-->", json_resp)
    file_pathh = json_resp['result']['file_path']
    print("file_pathh-->", file_pathh)

    # saving the file to our computer
    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content = b.content
    with open(file_pathh, "wb") as f:
        f.write(file_content)



def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello there. Provide any English word and I will give you a bunch "
                                                   "of information about it.")

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("hi", start))

# invoke the get_word_info function when the user sends a message 
# that is not a command.
# dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))

updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=TOKEN,
                      webhook_url='https://telegram-bot-hiep.herokuapp.com/' + TOKEN
                      )