import sys

with open('input.txt', 'r') as f:
    data = f.readlines()

allowed = {'red': 12, 'green': 13, 'blue': 14}

possible_games = []
# format {gameID:[{red: #, green: #, blue: #}]]}
games = {}
for game  in data:
    gameID, flushes = game.split(':')
    gameID = gameID.split(' ')[-1].strip()
    flushes = flushes.split(';')
    flushes_list = []
    for flush in flushes:
        this_flush = {}
        colors = flush.split(',')
        for color in colors:
            color = color.strip().split(' ')
            this_flush[color[-1].strip()] = int(color[0].strip())
        flushes_list.append(this_flush)
    games[gameID] = flushes_list


for game in games:
    game_allowed = True
    for flush in games[game]:
        for color in flush:
            if flush[color] > allowed[color]:
                game_allowed = False
                break
    if game_allowed:
        possible_games.append(int(game))

print(sum(possible_games))

least_num_cubes = {}
for game in games:
    least_num_cubes[game] = {'red': 0, 'green': 0, 'blue': 0}
    for flush in games[game]:
        for color in flush:
            if flush[color] > least_num_cubes[game][color]:
                least_num_cubes[game][color] = flush[color]

powers = []
for game in least_num_cubes:
    powers.append(int(least_num_cubes[game]['red'])*int(least_num_cubes[game]['green'])*int(least_num_cubes[game]['blue']))

print(sum(powers))

    