import json
import time
from text import game_data


def game_test(x):
    user_dict = json.loads(game_data["user"])
    print("Hello {}, this is a test: {}".format(user_dict["info"]["username"],x))


def game_reset(x):
    user_dict = json.loads(game_data["user"])
    _choice = input("Are you sure? the user {} will be erased. Y/N\n".format(user_dict["info"]["username"]))
    _choice = _choice.lower()
    if _choice == "y":
        game_data.clear()
        print('resetting, do not exit.')
        time.sleep(1)
        f = open("game_data.txt", "w")
        f.write("")
        f.close()
        time.sleep(1)
        print('resetting done')
        time.sleep(1)
    else:
        print("canceled")
