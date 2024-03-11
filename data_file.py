import sqlite3

# класс Упражнение
class Exercise:
    def __init__(self, id, title, image, description, complexity, availability, muscle_group, energy):
        self.id = id
        self.title = title
        self.image = image
        self.description = description
        self.complexity = complexity
        self.availability = availability
        self.muscle_group = muscle_group
        self.energy = energy

# функция получения инфы о упржнении
def get_execise(cursor):
    command = '''SELECT *
    FROM exercises'''
    result = cursor.execute(command)
    
        

# подключаем бд
with sqlite3.connect('exercises_data.db') as cursor:
    get_execise(cursor)