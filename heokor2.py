import sqlite3

db = sqlite3.connect('hw.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
name text,
surname text,
year integer,
points integer,
hobby text)
''')

c.execute("INSERT INTO user VALUES ('Иван', 'Иванов', 2066, 8, 'Точно не шпионить')")
c.execute("INSERT INTO user VALUES ('Саят', 'Омаров', 1987, 10, 'Брать и не брать взятки')")
c.execute("INSERT INTO user VALUES ('Рината', 'Калашникова', 2000, 7, 'Программирование')")
c.execute("INSERT INTO user VALUES ('Наташа', 'Смирнова', 1999, 10, 'Красть ручки')")
c.execute("INSERT INTO user VALUES ('Нурбек', 'Омуралиев', 2000, 10, 'Футбол')")
c.execute("INSERT INTO user VALUES ('Александр', 'Тен', 2001, 6, 'Волейбол')")
c.execute("INSERT INTO user VALUES ('Никита', 'Дзю', 2000, 9, 'Бег')")
c.execute("INSERT INTO user VALUES ('Мира', 'Касымбекова', 2010, 10, 'Плавание')")
c.execute("INSERT INTO user VALUES ('Саша', 'Ковалев', 2019, 5, 'Нарды')")
c.execute("INSERT INTO user VALUES ('Роман', 'Фильченков', 1, 1000000000000000000000, 'Майнкрафт')")
c.execute("UPDATE user SET name = 'genius' WHERE points = 10")
c.execute("SELECT rowid, surname, name FROM user ")

c.execute("SELECT rowid FROM user")

c.execute("UPDATE user SET name = 'genius' WHERE points = 10")
c.execute("SELECT rowid, surname, name FROM user ")

items = c.fetchall()

print(items)

for i in items:
    surname = i[1]
    if len(surname) > 10:
        print(f'\nСтуденты со статусом genius: {surname}')
    else:
        ...

c.execute("SELECT rowid, name FROM user WHERE name = 'genius'")
c.execute("DELETE FROM user WHERE rowid % 2 = 0")
print(c.fetchall())

db.commit()
db.close()