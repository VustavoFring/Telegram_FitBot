import telebot 
from telebot import types
import sqlite3
from PIL import Image
import io

class Exercise:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cur = self.conn.cursor()

    def get_exercise_image_by_id(self, exercise_id):
        self.cur.execute("SELECT image FROM exercises WHERE id=?", (exercise_id,))
        exercise_image = self.cur.fetchone()
    
        if exercise_image is not None:
            image_data = exercise_image[0]
            image = Image.open(io.BytesIO(image_data))
            return image
        else:
            return None
        
    def get_exercise_image_by_id(self, exercise_id):
        self.cur.execute("SELECT image FROM exercises WHERE id=?", (exercise_id,))
        exercise_image = self.cur.fetchone()[0]
        image = Image.open(io.BytesIO(exercise_image))
        return image
    
    def get_exercise_description_by_id(self, exercise_id):
        self.cur.execute("SELECT description FROM exercises WHERE id=?", (exercise_id,))
        description = self.cur.fetchone()
        return description

    def add_exercise(self, title, image, description, group_muscle, difficulty, availability, energy_cost):
        self.cur.execute("INSERT INTO exercises(title, image, description, group_muscle, difficulty, availability,) VALUES (?, ?, ?, ?, ?, ?, ?)", (title, image, description, group_muscle, difficulty, availability, energy_cost))
        self.conn.commit()

    def update_exercise(self, exercise_id, title, image, description, group_muscle, difficulty, availability, energy_cost):
        self.cur.execute("UPDATE exercises SET title=?, image=?, description=?, group_muscle=?, difficulty=?, availability=? WHERE id=?", (title, image, description, group_muscle, difficulty, availability, energy_cost, exercise_id))
        self.conn.commit()

    def delete_exercise(self, exercise_id):
        self.cur.execute("DELETE FROM exercises WHERE id=?", (exercise_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
db_path = 'exercises_data.db'
exercise_manager = Exercise(db_path)


# токен для бота
token = '7031939959:AAFOYF-nB-3_37yvr0Q7cXT1NnAf3MW-yvw'
# обьект бот
bot = telebot.TeleBot(token)

# декоратор для главного меню и приветствия
@bot.message_handler(commands=['start'])
def start_menu(message):
    markup =types.ReplyKeyboardMarkup()
    butn1=types.KeyboardButton('Каталог упражнений')
    butn2=types.KeyboardButton('Информация о боте')
    markup.row(butn1, butn2)
    welcome_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений'
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    bot.register_next_step_handler(message, aft_click)
def aft_click(message):
    if message.text == 'Информация о боте':
        bot_information_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений.\n\nЭтот бот создат в качестве итогового проекта, является всего лишь помощником и не гарантирует 100-процентного результата, если у вас имеются проблемы со здоровьем, то перед выполнением технически сложных упражнений рекомендуется проконсультироваться со специалистом.'
        bot.send_message(message.chat.id, bot_information_text)
    elif message.text == 'Каталог упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7)
        bot.send_message(message.chat.id,'Выберете желаемый тип упражнений по группам мышц', reply_markup=markup)
        bot.register_next_step_handler(message, aft_click_exersize_group)
def aft_click_exersize_group(message):
    if message.text == 'Упражнения на ноги':
        i = 0
        while i < 16:
            i += 1
            exersize_image = exercise_manager.get_exercise_image_by_id(int(i))
            exersize_description = exercise_manager.get_exercise_description_by_id(int(i))
            bot.send_photo(message.chat.id, exersize_image, exersize_description)


                   



@bot.message_handler(commands=['help'])
    # даем справку о боте
def information_message(message):
    bot_information_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений.\n\nЭтот бот создат в качестве итогового проекта, является всего лишь помощником и не гарантирует 100-процентного результата, если у вас имеются проблемы со здоровьем, то перед выполнением технически сложных упражнений рекомендуется проконсультироваться со специалистом.'
    # отправляем справку
    bot.send_message(message.chat.id, bot_information_text)

# поле экспериментов
    
# exercise_image = exercise_manager.get_exercise_image_by_id(1)
# exercise_description = exercise_manager.get_exercise_description_by_id(1)
# @bot.message_handler(commands=['image'])

# def image_message(message):
#     image = exercise_image
#     description = exercise_description
#     bot.send_photo(message.chat.id, image, description)

# поле экспериментов



# циклирование работы бота
bot.polling()