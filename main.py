import data_file
from data_file_2 import *
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

# поле экспериментов
exercise_image = exercise_manager.get_exercise_image_by_id(1)
exercise_description = exercise_manager.get_exercise_description_by_id(1)
@bot.message_handler(commands=['image'])

def image_message(message):
    image = exercise_image
    description = exercise_description
    bot.send_photo(message.chat.id, image, description)




# циклирование работы бота
bot.polling()