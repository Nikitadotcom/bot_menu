import logging

from telegram.ext import Updater, CommandHandler, MessageHandler


logging.basicConfig(level=logging.INFO)

TOKEN = '6554206451:AAEQ4fQ616BhgrgPOHD0KyMs5jDPIAE8x6s'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет!')

def main():
    updater = Updater(TOKEN, use_context=True)
    
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


import requests

def send_question(chat_id, question):
    url = 'https://api.yourai.com/ask'
    data = {'chat_id': chat_id, 'question': question}
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        return response.json()['answer']
    else:
        return None