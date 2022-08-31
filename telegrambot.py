from flask import Flask, request, Response
from functions import *

app = Flask(__name__)

# Reading the respomnse from the user and responding to it accordingly
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        try:
            parsed_data = tel_parse_data(msg)
            parsed_massage = parsed_data['message']['text']
            parsed_massage = format_parsed_message(parsed_massage)
            print("PARSED MESS", parsed_massage)
            chat_id = parsed_data['message']['chat']['id']

            if parsed_massage in ["hi", "hello", "good morning", "good afternoon", "good evening"]:
                tel_send_message(chat_id, "Hello " + parsed_data['message']['from']['first_name'] + "!")
            elif parsed_massage in ["message count", "how many message in this chat", "message_count"]:
                tel_send_message(chat_id, "There are " + str(parsed_data['message']['message_id']) + " messages in this chat")
            elif parsed_massage in ["my id", "what is my id", "guess my id", 'id']:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + "'s ID is " + str(parsed_data['message']['from']['id']))
            elif parsed_massage in ["my first name", "what is my first name", "guess my first name"]:
                tel_send_message(chat_id, "Your first name is " + parsed_data['message']['from']['first_name'])
            elif parsed_massage in ["my last name", "what is my last name", "guess my last name"]:
                tel_send_message(chat_id, "Your last name is " + parsed_data['message']['from']['last_name'])
            elif parsed_massage in ["my full name", "what is my full name", "guess my full name", "name", "what is my name", "guess my name", 'name']:
                tel_send_message(chat_id, "Your full name is " + parsed_data['message']['from']['first_name'] + " " + parsed_data['message']['from']['last_name'])

            elif parsed_massage in ["image", "photo", "picture"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + ", here is a random image:")
                tel_send_image(chat_id)
            elif parsed_massage in ["meme"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + ", here is a random meme:")
                tel_send_meme(chat_id)
            elif parsed_massage in ["gif"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + ", here is a random gif:")
                tel_send_gif(chat_id)
            elif parsed_massage in ["dice"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + " start rolling dice:")
                tel_send_dice(chat_id, "🎲")
            elif parsed_massage in ["slot machine", "slot_machine"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + " start using slot machine :")
                tel_send_dice(chat_id, "🎰")
            elif parsed_massage in ["dart", "darts"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + " start playing darts:")
                tel_send_dice(chat_id, "🎯")
            elif parsed_massage in ["basketball"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + " start playing basketball:")
                tel_send_dice(chat_id, "🏀")
            elif parsed_massage in ["football", "soccer"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + " start playing football:")
                tel_send_dice(chat_id, "⚽")
            elif parsed_massage in ["bowling"]:
                tel_send_message(chat_id, parsed_data['message']['from']['first_name'] + " start playing bowling:")
                tel_send_dice(chat_id, "🎳")

            elif parsed_massage == "poll":
                tel_send_poll(chat_id)
            elif parsed_massage == "button":
                tel_send_button(chat_id)
            elif parsed_massage == "audio":
                tel_send_audio(chat_id)
            elif parsed_massage == "file":
                tel_send_document(chat_id)
            elif parsed_massage == "video":
                tel_send_video(chat_id)
            elif parsed_massage == "inline":
                tel_send_inlinebutton(chat_id)
            elif parsed_massage == "inlineurl":
                tel_send_inlineurl(chat_id)
            elif parsed_massage == "ic_A":
                tel_send_message(chat_id, "You have clicked A")
            elif parsed_massage == "ic_B":
                tel_send_message(chat_id, "You have clicked B")

            else:
                tel_send_message(chat_id, 'Sorry, I cannot understand your message :(')
        except Exception as ex:
            print("ERROR IN API: ", ex)

        # try:
        #     file_id = tel_parse_get_message(msg)
        #     tel_upload_file(file_id)
        # except:
        #     print("No file from index-->")

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
