import sqlite3

conn = sqlite3.connect('students.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE students
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 surname TEXT NOT NULL,
#                 birth_year INTEGER NOT NULL,
#                 homework_score INTEGER NOT NULL,
#                 hobby TEXT)''')

# добавляем 10 студентов
students = [('Иван', 'Иванов', 2066, 8, 'Точно не шпионить'),
            ('Саят', 'Омаров', 1987, 10, 'Брать и не брать взятки'),
            ('Рината', 'Калашникова', 2000, 7, 'Программирование'),
            ('Наташа', 'Смирнова', 1999, 10, 'Красть ручки'),
            ('Нурбек', 'Омуралиев', 2000, 10, 'Футбол'),
            ('Александр', 'Тен', 2001, 6, 'Волейбол'),
            ('Никита', 'Дзю', 2000, 9, 'Бег'),
            ('Мира', 'Касымбекова', 2010, 10, 'Плавание'),
            ('Саша', 'Ковалев', 2019, 5, 'Нарды'),
            ('Роман', 'Фильченков', 1, 1000000000000000000000, 'Майнкрафт')]

for student in students:
    cursor.execute("INSERT INTO students (name,surname,birth_year,homework_score,hobby)VALUES(?, ?, ?, ?, ?)", student)

conn.commit()

cursor.execute('''SELECT * FROM  students WHERE length(surname) > 10''')
result = cursor.fetchall()
print('Студенты с фамилией больше 10 символов:')
for row in result:
    print(row)

cursor.execute('''UPDATE students SET name ='genius' WHERE homework_score > 10''')

cursor.execute('''SELECT * FROM students WHERE  name = 'genius' ''')
result = cursor.fetchall()
print('\nСтуденты со статусом genius:')
for row in result:
    print(row)

cursor.execute("DELETE FROM students WHERE id % 2 = 0")

conn.close()
