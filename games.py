import csv

fields = ['Name', 'Release date', 'Rating', 'Genres', 'Platforms']
games = []
with open('games.csv') as game_csv:
    reader = csv.DictReader(game_csv, fields)
    for row in reader:
        games.append(row)

for dic in games:
    for i in range(3, 5):
        new_value = dic.get(fields[i]).split()
        dic[fields[i]] = new_value