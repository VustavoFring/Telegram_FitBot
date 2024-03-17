import telebot 
from telebot import types
import sqlite3
from PIL import Image
import io

class Exercise:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cur = self.conn.cursor()

# ---------------------------------------------------------------------------------------
        
    def get_legs_exercise_image_by_id(self, exercise_id):
        self.cur.execute("SELECT image FROM exercises_legs WHERE id=?", (exercise_id))
        exercise_image = self.cur.fetchone()
    
        if exercise_image is not None:
            image_data = exercise_image[0]
            image = Image.open(io.BytesIO(image_data))
            return image
        else:
            return None
    
    def get_back_exercise_image_by_id(self, exercise_id):
        self.cur.execute("SELECT image FROM exercises_back WHERE id=?", (exercise_id))
        exercise_image = self.cur.fetchone()
    
        if exercise_image is not None:
            image_data = exercise_image[0]
            image = Image.open(io.BytesIO(image_data))
            return image
        else:
            return None
    
    def get_legs_exercise_description_by_id(self, exercise_id):
        self.cur.execute("SELECT description FROM exercises_legs WHERE id=?", (exercise_id))
        description = self.cur.fetchone()
        return description
    
    def get_back_exercise_description_by_id(self, exercise_id):
        self.cur.execute("SELECT description FROM exercises_back WHERE id=?", (exercise_id))
        description = self.cur.fetchone()
        return description
    
    # -------------------------------------

    # поиск изображений упражнений на ноги по "доступности"
    def get_legs_exercise_image_by_availability(self, exercise_availability):
        self.cur.execute("SELECT image FROM exercises_legs WHERE availability == ?", (exercise_availability))
        exercise_images = self.cur.fetchall()
        if exercise_images is not None:
            return exercise_images
        else:
            return None
    # поиск изображений упражнений на спину по "доступности"    
    def get_back_exercise_image_by_availability(self, exercise_availability):
        self.cur.execute("SELECT image FROM exercises_back WHERE availability == ?", (exercise_availability))
        exercise_images = self.cur.fetchall()
        if exercise_images is not None:
            return exercise_images
        else:
            return None
    # поиск изображений упражнений на пресс по "доступности"    
    def get_core_exercise_image_by_availability(self, exercise_availability):
        self.cur.execute("SELECT image FROM exercises_core WHERE availability == ?", (exercise_availability))
        exercise_images = self.cur.fetchall()
        if exercise_images is not None:
            return exercise_images
        else:
            return None
    # поиск изображений упражнений на грудь по "доступности"   
    def get_chest_exercise_image_by_availability(self, exercise_availability):
        self.cur.execute("SELECT image FROM exercises_chest WHERE availability == ?", (exercise_availability))
        exercise_images = self.cur.fetchall()
        if exercise_images is not None:
            return exercise_images
        else:
            return None
    # поиск изображений упражнений на руки по "доступности"   
    def get_arms_exercise_image_by_availability(self, exercise_availability):
        self.cur.execute("SELECT image FROM exercises_arms WHERE availability == ?", (exercise_availability))
        exercise_images = self.cur.fetchall()
        if exercise_images is not None:
            return exercise_images
        else:
            return None
    # поиск изображений упражнений на плечи по "доступности"    
    def get_shoulders_exercise_image_by_availability(self, exercise_availability):
        self.cur.execute("SELECT image FROM exercises_shoulders WHERE availability == ?", (exercise_availability))
        exercise_images = self.cur.fetchall()
        if exercise_images is not None:
            return exercise_images
        else:
            return None
        
        
    # поиск описаний упражнений на ноги по "доступности"   
    def get_legs_exercise_description_by_availability(self, exercise_availability):
        self.cur.execute("SELECT description FROM exercises_legs WHERE availability == ?", (exercise_availability))
        descriptions = self.cur.fetchall()
        return descriptions
    # поиск описаний упражнений на спину по "доступности"   
    def get_back_exercise_description_by_availability(self, exercise_availability):
        self.cur.execute("SELECT description FROM exercises_back WHERE availability == ?", (exercise_availability))
        descriptions = self.cur.fetchall()
        return descriptions
    # поиск описаний упражнений на пресс по "доступности"
    def get_core_exercise_description_by_availability(self, exercise_availability):
        self.cur.execute("SELECT description FROM exercises_core WHERE availability == ?", (exercise_availability))
        descriptions = self.cur.fetchall()
        return descriptions
    # поиск описаний упражнений на грудь по "доступности"
    def get_chest_exercise_description_by_availability(self, exercise_availability):
        self.cur.execute("SELECT description FROM exercises_chest WHERE availability == ?", (exercise_availability))
        descriptions = self.cur.fetchall()
        return descriptions
    # поиск описаний упражнений на руки по "доступности"
    def get_arms_exercise_description_by_availability(self, exercise_availability):
        self.cur.execute("SELECT description FROM exercises_arms WHERE availability == ?", (exercise_availability))
        descriptions = self.cur.fetchall()
        return descriptions
    # поиск описаний упражнений на плечи по "доступности"
    def get_shoulders_exercise_description_by_availability(self, exercise_availability):
        self.cur.execute("SELECT description FROM exercises_shoulders WHERE availability == ?", (exercise_availability))
        descriptions = self.cur.fetchall()
        return descriptions
    

# ------------------------------------------------------
    
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
# ---------------------------------------------------------------------------


db_path = 'exercises_data.db'
exercise_manager = Exercise(db_path)

token = '7031939959:AAFOYF-nB-3_37yvr0Q7cXT1NnAf3MW-yvw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_menu(message):
    markup =types.ReplyKeyboardMarkup()
    butn1=types.KeyboardButton('Каталог упражнений')
    butn2=types.KeyboardButton('Информация о боте')
    markup.row(butn1, butn2)
    welcome_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений'
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def aft_click1(message):

    if message.text == 'Информация о боте':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад')
        bot_information_text = 'Здравствуйте, этот бот - ваш персональный фитнесс ассистент, он сможет помочь вам в подборе тренировочного плана и упражнений.\n\nЭтот бот создат в качестве итогового проекта, является всего лишь помощником и не гарантирует 100-процентного результата, если у вас имеются проблемы со здоровьем, то перед выполнением технически сложных упражнений рекомендуется проконсультироваться со специалистом.'
        markup.row(butn_back)
        bot.send_message(message.chat.id, bot_information_text, reply_markup=markup)

    elif message.text == 'Каталог упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Выберете желаемый тип упражнений по группам мышц', reply_markup=markup)

    elif message.text == 'Назад':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Каталог упражнений')
        butn2=types.KeyboardButton('Информация о боте')
        markup.row(butn1, butn2)
        bot.send_message(message.chat.id, 'Назад', reply_markup=markup)



    elif message.text == 'Упражнения на ноги':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Нет никакого инвентаря')
        butn2=types.KeyboardButton('Есть гантели или гири')
        butn3=types.KeyboardButton('Хожу в тренажерный зал')
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn1, butn2, butn3)
        markup.row(butn_back)
        bot.send_message(message.chat.id,'Выберите тип вашего инвентаря', reply_markup=markup)
        bot.register_next_step_handler(message, list_of_legs_exercises)

    elif message.text == 'Упражнения на спину':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Нет никакого инвентаря')
        butn2=types.KeyboardButton('Есть гантели или гири')
        butn3=types.KeyboardButton('Хожу в тренажерный зал')
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn1, butn2, butn3)
        markup.row(butn_back)
        bot.send_message(message.chat.id,'Выберите тип вашего инвентаря', reply_markup=markup)
        bot.register_next_step_handler(message, list_of_back_exercises)

    elif message.text == 'Упражнения на пресс':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Нет никакого инвентаря')
        butn2=types.KeyboardButton('Есть гантели или гири')
        butn3=types.KeyboardButton('Хожу в тренажерный зал')
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn1, butn2, butn3)
        markup.row(butn_back)
        bot.send_message(message.chat.id,'Выберите тип вашего инвентаря', reply_markup=markup)
        bot.register_next_step_handler(message, list_of_core_exercises)

    elif message.text == 'Упражнения на грудные мышцы':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Нет никакого инвентаря')
        butn2=types.KeyboardButton('Есть гантели или гири')
        butn3=types.KeyboardButton('Хожу в тренажерный зал')
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn1, butn2, butn3)
        markup.row(butn_back)
        bot.send_message(message.chat.id,'Выберите тип вашего инвентаря', reply_markup=markup)
        bot.register_next_step_handler(message, list_of_chest_exercises)

    elif message.text == 'Упражнения на руки':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Нет никакого инвентаря')
        butn2=types.KeyboardButton('Есть гантели или гири')
        butn3=types.KeyboardButton('Хожу в тренажерный зал')
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn1, butn2, butn3)
        markup.row(butn_back)
        bot.send_message(message.chat.id,'Выберите тип вашего инвентаря', reply_markup=markup)
        bot.register_next_step_handler(message, list_of_arms_exercises)

    elif message.text == 'Упражнения на плечи':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Нет никакого инвентаря')
        butn2=types.KeyboardButton('Есть гантели или гири')
        butn3=types.KeyboardButton('Хожу в тренажерный зал')
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn1, butn2, butn3)
        markup.row(butn_back)
        bot.send_message(message.chat.id,'Выберите тип вашего инвентаря', reply_markup=markup)
        bot.register_next_step_handler(message, list_of_shoulders_exercises)



    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)


def list_of_legs_exercises(message):
    if message.text == 'Нет никакого инвентаря':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images1 = exercise_manager.get_legs_exercise_image_by_availability(('1'))
        exercise_descriptions1 = exercise_manager.get_legs_exercise_description_by_availability(('1'))
        x = 0 
        for i in exercise_images1:
            exercise_image1 = i[0]
            exercise_image1 = Image.open(io.BytesIO(exercise_image1))
            exercise_description1 = exercise_descriptions1[x]
            x+=1
            bot.send_photo(message.chat.id, exercise_image1, exercise_description1, reply_markup=markup)
    elif message.text == 'Есть гантели или гири':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images2 = exercise_manager.get_legs_exercise_image_by_availability(('2'))
        exercise_descriptions2 = exercise_manager.get_legs_exercise_description_by_availability(('2'))
        y = 0 
        for i in exercise_images2:
            exercise_image2 = i[0]
            exercise_image2 = Image.open(io.BytesIO(exercise_image2))
            exercise_description2 = exercise_descriptions2[y]
            y+=1
            bot.send_photo(message.chat.id, exercise_image2, exercise_description2, reply_markup=markup)
    elif message.text == 'Хожу в тренажерный зал':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images3 = exercise_manager.get_legs_exercise_image_by_availability(('3'))
        exercise_descriptions3 = exercise_manager.get_legs_exercise_description_by_availability(('3'))
        z = 0 
        for i in exercise_images3:
            exercise_image3 = i[0]
            exercise_image3 = Image.open(io.BytesIO(exercise_image3))
            exercise_description3 = exercise_descriptions3[z]
            z+=1
            bot.send_photo(message.chat.id, exercise_image3, exercise_description3, reply_markup=markup)

    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)
    

def list_of_back_exercises(message):
    if message.text == 'Нет никакого инвентаря':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images1 = exercise_manager.get_back_exercise_image_by_availability(('1'))
        exercise_descriptions1 = exercise_manager.get_back_exercise_description_by_availability(('1'))
        x = 0 
        for i in exercise_images1:
            exercise_image1 = i[0]
            exercise_image1 = Image.open(io.BytesIO(exercise_image1))
            exercise_description1 = exercise_descriptions1[x]
            x+=1
            bot.send_photo(message.chat.id, exercise_image1, exercise_description1, reply_markup=markup)
    elif message.text == 'Есть гантели или гири':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images2 = exercise_manager.get_back_exercise_image_by_availability(('2'))
        exercise_descriptions2 = exercise_manager.get_back_exercise_description_by_availability(('2'))
        y = 0 
        for i in exercise_images2:
            exercise_image2 = i[0]
            exercise_image2 = Image.open(io.BytesIO(exercise_image2))
            exercise_description2 = exercise_descriptions2[y]
            y+=1
            bot.send_photo(message.chat.id, exercise_image2, exercise_description2, reply_markup=markup)
    elif message.text == 'Хожу в тренажерный зал':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images3 = exercise_manager.get_back_exercise_image_by_availability(('3'))
        exercise_descriptions3 = exercise_manager.get_back_exercise_description_by_availability(('3'))
        z = 0 
        for i in exercise_images3:
            exercise_image3 = i[0]
            exercise_image3 = Image.open(io.BytesIO(exercise_image3))
            exercise_description3 = exercise_descriptions3[z]
            z+=1
            bot.send_photo(message.chat.id, exercise_image3, exercise_description3, reply_markup=markup)

    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)


def list_of_core_exercises(message):
    if message.text == 'Нет никакого инвентаря':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images1 = exercise_manager.get_core_exercise_image_by_availability(('1'))
        exercise_descriptions1 = exercise_manager.get_core_exercise_description_by_availability(('1'))
        x = 0 
        for i in exercise_images1:
            exercise_image1 = i[0]
            exercise_image1 = Image.open(io.BytesIO(exercise_image1))
            exercise_description1 = exercise_descriptions1[x]
            x+=1
            bot.send_photo(message.chat.id, exercise_image1, exercise_description1, reply_markup=markup)
    elif message.text == 'Есть гантели или гири':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images2 = exercise_manager.get_core_exercise_image_by_availability(('2'))
        exercise_descriptions2 = exercise_manager.get_core_exercise_description_by_availability(('2'))
        y = 0 
        for i in exercise_images2:
            exercise_image2 = i[0]
            exercise_image2 = Image.open(io.BytesIO(exercise_image2))
            exercise_description2 = exercise_descriptions2[y]
            y+=1
            bot.send_photo(message.chat.id, exercise_image2, exercise_description2, reply_markup=markup)
    elif message.text == 'Хожу в тренажерный зал':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images3 = exercise_manager.get_core_exercise_image_by_availability(('3'))
        exercise_descriptions3 = exercise_manager.get_core_exercise_description_by_availability(('3'))
        z = 0 
        for i in exercise_images3:
            exercise_image3 = i[0]
            exercise_image3 = Image.open(io.BytesIO(exercise_image3))
            exercise_description3 = exercise_descriptions3[z]
            z+=1
            bot.send_photo(message.chat.id, exercise_image3, exercise_description3, reply_markup=markup)

    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)


def list_of_chest_exercises(message):
    if message.text == 'Нет никакого инвентаря':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images1 = exercise_manager.get_chest_exercise_image_by_availability(('1'))
        exercise_descriptions1 = exercise_manager.get_chest_exercise_description_by_availability(('1'))
        x = 0 
        for i in exercise_images1:
            exercise_image1 = i[0]
            exercise_image1 = Image.open(io.BytesIO(exercise_image1))
            exercise_description1 = exercise_descriptions1[x]
            x+=1
            bot.send_photo(message.chat.id, exercise_image1, exercise_description1, reply_markup=markup)
    elif message.text == 'Есть гантели или гири':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images2 = exercise_manager.get_chest_exercise_image_by_availability(('2'))
        exercise_descriptions2 = exercise_manager.get_chest_exercise_description_by_availability(('2'))
        y = 0 
        for i in exercise_images2:
            exercise_image2 = i[0]
            exercise_image2 = Image.open(io.BytesIO(exercise_image2))
            exercise_description2 = exercise_descriptions2[y]
            y+=1
            bot.send_photo(message.chat.id, exercise_image2, exercise_description2, reply_markup=markup)
    elif message.text == 'Хожу в тренажерный зал':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images3 = exercise_manager.get_chest_exercise_image_by_availability(('3'))
        exercise_descriptions3 = exercise_manager.get_chest_exercise_description_by_availability(('3'))
        z = 0 
        for i in exercise_images3:
            exercise_image3 = i[0]
            exercise_image3 = Image.open(io.BytesIO(exercise_image3))
            exercise_description3 = exercise_descriptions3[z]
            z+=1
            bot.send_photo(message.chat.id, exercise_image3, exercise_description3, reply_markup=markup)

    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)


def list_of_arms_exercises(message):
    if message.text == 'Нет никакого инвентаря':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images1 = exercise_manager.get_arms_exercise_image_by_availability(('1'))
        exercise_descriptions1 = exercise_manager.get_arms_exercise_description_by_availability(('1'))
        x = 0 
        for i in exercise_images1:
            exercise_image1 = i[0]
            exercise_image1 = Image.open(io.BytesIO(exercise_image1))
            exercise_description1 = exercise_descriptions1[x]
            x+=1
            bot.send_photo(message.chat.id, exercise_image1, exercise_description1, reply_markup=markup)
    elif message.text == 'Есть гантели или гири':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images2 = exercise_manager.get_arms_exercise_image_by_availability(('2'))
        exercise_descriptions2 = exercise_manager.get_arms_exercise_description_by_availability(('2'))
        y = 0 
        for i in exercise_images2:
            exercise_image2 = i[0]
            exercise_image2 = Image.open(io.BytesIO(exercise_image2))
            exercise_description2 = exercise_descriptions2[y]
            y+=1
            bot.send_photo(message.chat.id, exercise_image2, exercise_description2, reply_markup=markup)
    elif message.text == 'Хожу в тренажерный зал':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images3 = exercise_manager.get_arms_exercise_image_by_availability(('3'))
        exercise_descriptions3 = exercise_manager.get_arms_exercise_description_by_availability(('3'))
        z = 0 
        for i in exercise_images3:
            exercise_image3 = i[0]
            exercise_image3 = Image.open(io.BytesIO(exercise_image3))
            exercise_description3 = exercise_descriptions3[z]
            z+=1
            bot.send_photo(message.chat.id, exercise_image3, exercise_description3, reply_markup=markup)

    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)


def list_of_shoulders_exercises(message):
    if message.text == 'Нет никакого инвентаря':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images1 = exercise_manager.get_shoulders_exercise_image_by_availability(('1'))
        exercise_descriptions1 = exercise_manager.get_shoulders_exercise_description_by_availability(('1'))
        x = 0 
        for i in exercise_images1:
            exercise_image1 = i[0]
            exercise_image1 = Image.open(io.BytesIO(exercise_image1))
            exercise_description1 = exercise_descriptions1[x]
            x+=1
            bot.send_photo(message.chat.id, exercise_image1, exercise_description1, reply_markup=markup)
    elif message.text == 'Есть гантели или гири':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images2 = exercise_manager.get_shoulders_exercise_image_by_availability(('2'))
        exercise_descriptions2 = exercise_manager.get_shoulders_exercise_description_by_availability(('2'))
        y = 0 
        for i in exercise_images2:
            exercise_image2 = i[0]
            exercise_image2 = Image.open(io.BytesIO(exercise_image2))
            exercise_description2 = exercise_descriptions2[y]
            y+=1
            bot.send_photo(message.chat.id, exercise_image2, exercise_description2, reply_markup=markup)
    elif message.text == 'Хожу в тренажерный зал':
        markup =types.ReplyKeyboardMarkup()
        butn_back=types.KeyboardButton('Назад к типам упражнений')
        markup.row(butn_back)
        exercise_images3 = exercise_manager.get_shoulders_exercise_image_by_availability(('3'))
        exercise_descriptions3 = exercise_manager.get_shoulders_exercise_description_by_availability(('3'))
        z = 0 
        for i in exercise_images3:
            exercise_image3 = i[0]
            exercise_image3 = Image.open(io.BytesIO(exercise_image3))
            exercise_description3 = exercise_descriptions3[z]
            z+=1
            bot.send_photo(message.chat.id, exercise_image3, exercise_description3, reply_markup=markup)

    elif message.text == 'Назад к типам упражнений':
        markup =types.ReplyKeyboardMarkup()
        butn1=types.KeyboardButton('Упражнения на ноги')
        butn2=types.KeyboardButton('Упражнения на спину')
        butn3=types.KeyboardButton('Упражнения на пресс')
        butn4=types.KeyboardButton('Упражнения на грудные мышцы')
        butn5=types.KeyboardButton('Упражнения на руки')
        butn6=types.KeyboardButton('Упражнения на плечи')
        butn7=types.KeyboardButton('Кардио упражнения')
        butn_back=types.KeyboardButton('Назад')
        markup.row(butn1, butn2)
        markup.row(butn3, butn4)
        markup.row(butn5, butn6)
        markup.row(butn7, butn_back)
        bot.send_message(message.chat.id,'Назад к типам упражнений', reply_markup=markup)



bot.polling(none_stop= True)

                   





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

