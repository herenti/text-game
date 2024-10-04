import json
import time
from text import game_data

_commands = {
    "help": "show the list of commands, or a specific commands information.",
    "reset": "erase your save file and start a new game. Cannot be undone",
    "exit": "exit and save the game. Current battle progress will be lost.",
    "test": 'test message. Can be used as such: "test messagehere"'}

_locations = {
    "location a": {"nearby": ["location b", "location f"]},
    "location b": {"nearby": ["location a", "location c", "location e"]},
    "location c": {"nearby": ["location b"]},
    "location e": {"nearby": ["location b"]},
    "location f": {"nearby": ["location a"]}

    }


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

def game_travel(x):
    x = x.lower()
    try:
        env_dict = json.loads(game_data["environment"])
        current_location = env_dict["progress"]["location"]
        if x == current_location:
            print("You are already here.")
            return
        dest_nearby = _locations[x]["nearby"]
        current_nearby = _locations[current_location]["nearby"]
        a = set(dest_nearby)
        b = set(current_nearby)
        if (a & b):
            _link = list(a&b)
            print(_link)
        else:
            _link = "none"
        if current_location in dest_nearby:
            env_dict["progress"]["location"] = x
            game_data["environment"]= json.dumps(env_dict)
            print("You went from {} to {}".format(current_location, x))

        else:
            if _link != "none":
                print("I have to travel to {} first.".format(''.join(_link)))
            else:
                print("I am too far from there, I need to get closer.\n{} is near: [{}]".format (x, ", ".join(dest_nearby)))
    except:
        print("That is not a valid location.")


def game_save(x):
    print("saving")
    f = open("game_data.txt", "w")
    for i in game_data:
        _dict = json.loads(game_data[i])
        f.write(json.dumps([i,_dict])+"\n")
    f.close()
    time.sleep(1)
    print('saving done')

def game_help(x):
    if len(x) >0:
        try:
            print(x + ": " +_commands[x])
        except:
            print("That is not a valid command")
    else:
        print('Commands so far: [help, reset, exit, test, save]\nUse the help command to check individual commands, like "help reset", to show what reset does.')
