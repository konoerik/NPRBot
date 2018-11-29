import sys
from flask import Flask, request
import telepot
from telepot.loop import OrderedWebhook
from MessageHandler import  MessageHandler
from time import sleep

"""
Skeleton code from Telepot API project adapted for SWE6623 Telegram Bot project

How to run from cmd:
    $ python app.py <token> <listening_port> <webhook_url>
"""

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id)
    user_msg = MessageHandler(msg).reply()
    if type(user_msg) == list:
        for msg in user_msg:
            bot.sendMessage(chat_id=chat_id, text=msg)
            sleep(0.1)
    else:
        bot.sendMessage(chat_id=chat_id, text=user_msg)

def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)

# need `/setinline`
def on_inline_query(msg):
    query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
    print('Inline Query:', query_id, from_id, query_string)

    # Compose your own answers
    articles = [{'type': 'article',
                    'id': 'abc', 'title': 'ABC', 'message_text': 'Good morning'}]

    bot.answerInlineQuery(query_id, articles)

# need `/setinlinefeedback`
def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print('Chosen Inline Result:', result_id, from_id, query_string)


TOKEN = sys.argv[1]
PORT = int(sys.argv[2])
URL = sys.argv[3]

app = Flask(__name__)
bot = telepot.Bot(TOKEN)
webhook = OrderedWebhook(bot, {'chat': on_chat_message,
                               'callback_query': on_callback_query,
                               'inline_query': on_inline_query,
                               'chosen_inline_result': on_chosen_inline_result})

@app.route('/webhook', methods=['GET', 'POST'])
def pass_update():
    webhook.feed(request.data)

    return 'OK'

if __name__ == '__main__':
    try:
        bot.setWebhook(URL)
    # Sometimes it would raise this error, but webhook still set successfully.
    except telepot.exception.TooManyRequestsError:
        pass

    webhook.run_as_thread()
app.run(port=PORT, debug=True)
