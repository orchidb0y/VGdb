import csv
from datetime import date

fields = ['Name', 'Release date', 'Rating', 'Genres', 'Platforms']

genres = ['Action', 'Adventure', 'Rpg', 'Shooter', 'Puzzle']
platforms = ['Pc', 'Playstation', 'Xbox', 'Nintendo']
games = []

with open('games.csv') as game_csv:
    reader = csv.DictReader(game_csv, fields)
    for row in reader:
        games.append(row)

for dic in games:
    for i in range(3, 5):
        new_value = dic.get(fields[i]).split()
        dic[fields[i]] = new_value
    
    release_date = dic.get('Release date').split()
    release_date = date(int(release_date[0]), int(release_date[1]), int(release_date[2]))
    dic['Release date'] = release_date