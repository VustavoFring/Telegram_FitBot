import sqlite3
from PIL import Image
import io

class Exercise:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def get_exercise_by_id(self, exercise_id):
        self.cur.execute("SELECT * FROM exercises WHERE id=?", (exercise_id,))
        exercise = self.cur.fetchone()
        if exercise:
            return exercise
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
        self.cur.execute("INSERT INTO exercises(title, image, description, group_muscle, difficulty, availability, energy_cost) VALUES (?, ?, ?, ?, ?, ?, ?)", (title, image, description, group_muscle, difficulty, availability, energy_cost))
        self.conn.commit()

    def update_exercise(self, exercise_id, title, image, description, group_muscle, difficulty, availability, energy_cost):
        self.cur.execute("UPDATE exercises SET title=?, image=?, description=?, group_muscle=?, difficulty=?, availability=?, energy_cost=? WHERE id=?", (title, image, description, group_muscle, difficulty, availability, energy_cost, exercise_id))
        self.conn.commit()

    def delete_exercise(self, exercise_id):
        self.cur.execute("DELETE FROM exercises WHERE id=?", (exercise_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
db_path = 'exercises_data.db'
exercise_manager = Exercise(db_path)


