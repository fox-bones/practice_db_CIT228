import sqlite3

database = sqlite3.connect('practice.db')
cursor = database.cursor()


sql_query = "CREATE TABLE games (game_id INT PRIMARY KEY, title TEXT, num_players TEXT, min_age INT, ranking FLOAT)"
cursor.execute(sql_query)

sql_query = "INSERT INTO games (game_id, title, num_players, min_age, ranking) VALUES (1, 'Qwirkle', '2-4', 6, 4.5)"
cursor.execute(sql_query)

sql_query = "INSERT INTO games (game_id, title, num_players, min_age, ranking) VALUES (2, 'Monopoly', '2-8', 12, 8)"
cursor.execute(sql_query)

sql_query = "INSERT INTO games (game_id, title, num_players, min_age, ranking) VALUES (3, 'Farkle', '2-4', 8, 9)"
cursor.execute(sql_query)

sql_query = "INSERT INTO games (game_id, title, num_players, min_age) VALUES (4, 'Candy Land', '2-4', 3)"
cursor.execute(sql_query)

database.commit()

sql_query = "SELECT * FROM games"
results = list(cursor.execute(sql_query))
results.sort()
print("ID\tTitle\t\tNumber of Players\tMin Age\t\t\tRank")
for result in results:
    row = f"{result[0]}\t{result[1]}\t\t{result[2]}\t\t\t{result[3]}\t\t\t{result[4]}"
    print(row)

print() # break line for readability

sql_query = "SELECT * FROM games WHERE game_id = 1"
results = list(cursor.execute(sql_query))
results.sort()
print("ID\tTitle\t\tNumber of Players\tMin Age\t\t\tRank")
for result in results:
    row = f"{result[0]}\t{result[1]}\t\t{result[2]}\t\t\t{result[3]}\t\t\t{result[4]}"
    print(row)

print() # break line for readability

sql_query = "SELECT title FROM games WHERE game_id = 1"
results = list(cursor.execute(sql_query))
results.sort()
print("Title")
for result in results:
    row = f"{result[0]}"
    print(row)

print() # break line for readability

sql_query = "SELECT title, min_age FROM games ORDER BY min_age DESC"
results = list(cursor.execute(sql_query))
print("Title\t\tMin Age")
for result in results:
    row = f"{result[0]}\t\t{result[1]}"
    print(row)



sql_query = "UPDATE games SET ranking = 4.2 WHERE game_id = 1"
cursor.execute(sql_query)

sql_query = "UPDATE games SET min_age = 5, ranking = 2 WHERE game_id = 4"
cursor.execute(sql_query)


sql_query = "ALTER TABLE games ADD will_donate BOOLEAN"
cursor.execute(sql_query)

sql_query = "UPDATE games SET will_donate = True WHERE ranking < 3"
cursor.execute(sql_query)


sql_query = "DELETE FROM games WHERE game_id = 1"
cursor.execute(sql_query)

sql_query = "DELETE FROM games WHERE will_donate = True"
cursor.execute(sql_query)

database.commit()
database.close()