import sqlite3 
conn = sqlite3.connect("rio_olympics.db") 
cur = conn.cursor() 
columns = []
#Columns: id, name, nation..., sex, dob, height, weight, sport, gold, silver, bronze
def show_table():
    cur.execute(f"SELECT * FROM athletes; ")
    for row in cur:
        print(row)
#show_table()
def add(name, country, sport, gold):
    cur.execute(f"INSERT INTO athletes (name, sport, gold) VALUES ('{name}', '{sport}', {gold});")
    for rows in cur:
        print(rows)
add("Qwerty", "AAA", "AAA", "10")
def show_row(name):
    cur.execute("SELECT * FROM athletes WHERE name = ?;", (name,))
    for row in cur:
        print(row)
#show_row("Qwerty")
def count_rows():
    cur.execute("SELECT COUNT(name) FROM athletes;")
    for row in cur:
        print(row)
#count_rows()
def count_golds():
    cur.execute("SELECT sum(gold) FROM athletes;")
    for row in cur:
        print(row)
#count_golds()
def alter_value(column, value, name):
    cur.execute(f"UPDATE athletes SET {column} = {value} WHERE name = '{name}';")
    for row in cur:
        print(row)
alter_value("gold", "100", "Qwerty")
count_golds()