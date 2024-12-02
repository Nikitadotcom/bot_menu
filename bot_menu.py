import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TOKEN
from langchain_community.llms import Ollama

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я ананас-бот с AI. Ты можешь задать мне любой вопрос, '
                                     'но я заточен на рецептики.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Получено сообщение: {update.message.text}")
    try:
        llm = Ollama(model="llama2")
        response = llm(update.message.text, timeout=30)
        logging.info(f"Получен ответ от Ollama: {response}")
        await update.message.reply_text(response)
    except ConnectionError:
        await update.message.reply_text("Ошибка: Сервер Ollama недоступен. Убедитесь, что он запущен.")
    except Exception as e:
        logging.error(f"Ошибка: {str(e)}")
        await update.message.reply_text(f"Произошла ошибка: {str(e)}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()