import json

game_data = dict()
f = open('game_data.txt', 'r')
for line in f.readlines():
        try:
                if len(line) > 0:
                        user, _dict = json.loads(line.strip())
                        game_data[user] = json.dumps(_dict)
        except Exception as e:
                print("Could not load game_data file: %s" % e)
f.close()
