import json
import time
from text import game_data

_commands = {
    "help": "show the list of commands, or a specific commands information.",
    "reset": "erase your save file and start a new game. Cannot be undone",
    "exit": "exit and save the game. Current battle progress will be lost.",
    "test": 'test message. Can be used as such: "test messagehere"'}


def game_test(x):
    user_dict = json.loads(game_data["user"])
    print("Hello {}, this is a test: {}".format(user_dict["info"]["username"],x))


def game_reset(x):
    user_dict = json.loads(game_data["user"])
    _choice = input("Are you sure? the user {} will be erased. Y/N\n".format(user_dict["info"]["username"]))
    _choice = _choice.lower()
    if _choice == "y":
        game_data.clear()
        print('Resetting, do not exit.')
        time.sleep(1)
        f = open("game_data.txt", "w")
        f.write("")
        f.close()
        time.sleep(1)
        print('Resetting done')
    else:
        print("Canceled")


def game_help(x):
    if len(x) >0:
        try:
            print(x + ": " +_commands[x])
        except:
            print("That is not a valid command")
    else:
        print('Commands so far: [help, reset, exit, test]\nUse the help command to check individual commands, like "help reset", to show what reset does.')
