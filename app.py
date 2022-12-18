import sqlite3

connection = sqlite3.connect("tutorial.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
result = cursor.execute("SELECT name FROM sqlite_master")
print(result.fetchone())

cursor.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
connection.commit()

result = cursor.execute("SELECT score FROM movie")
print(result.fetchall())

data = [
    ("Month Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cursor.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
connection.commit()

for row in cursor.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)