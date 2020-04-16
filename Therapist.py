from nltk.chat.eliza import eliza_chatbot
import  telepot
import time

bot = telepot.Bot('TOKEN')

def therapist(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text']
    if text == "/start":
        bot.sendMessage(chat_id, "Hello, I'm the therapist.  How can I help?")
    else:
        bot.sendMessage(chat_id, eliza_chatbot.respond(text))

bot.message_loop(therapist)
print ('waiting ...')
while 1:
    time.sleep(10)
