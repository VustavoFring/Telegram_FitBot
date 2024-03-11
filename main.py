import data_file
import telebot
# токен для бота
token = '7031939959:AAFOYF-nB-3_37yvr0Q7cXT1NnAf3MW-yvw'
# обьект бот
bot = telebot.TeleBot(token)

# приветствие
@bot.message_handler(commands=['start'])
    # функция ответа
def welcome_message(message):
    welcome_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений'
    # отправить сообщение
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['help'])
    # даем справку о боте
def information_message(message):
    bot_information_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений.\n\nЭтот бот создат в качестве итогового проекта, является всего лишь помощником и не гарантирует 100-процентного результата.'
    # отправляем справку
    bot.send_message(message.chat.id, bot_information_text)




# циклирование работы бота
bot.polling()