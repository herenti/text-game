import json
import time
import sys
import random
from events_data import events_dict
from text import game_data

_commands = {
    "help": "show the list of commands, or a specific commands information.",
    "reset": "erase your save file and start a new game. Cannot be undone",
    "exit": "exit and save the game. Current battle progress will be lost.",
    "test": 'test message. Can be used as such: "test messagehere"',
    "travel": 'travel to an available location. Further use as:\n"travel info" (show what locations are near by),\n"travel list" (show all available locations),\n"travel location a" (travel to location a)'
        }

_locations = {
    "location a": {
        "nearby": ["location b", "location f"],
        "shops": [""],
        "events": []
        },
    "location b": {
        "nearby": ["location a", "location c", "location e"],
        "shops": [""],
        "events": []
        },
    "location c": {
        "nearby": ["location b"],
        "shops": [""],
        "events": []
        },
    "location e": {
        "nearby": ["location b"],
        "shops": [""],
        "events": []
        },
    "location f": {
        "nearby": ["location a"],
        "shops": [""],
        "events": []
        }

    }

_shops = {}

_local = {"game": "on",
          "r_e_notify": 0,
          "events": {},
          "random_event_number": 0
          }

def register():
    print("Welcome new user, the time has finally come. Let's register for the game.")
    time.sleep(1)

    _username = input("Firstly, What is your name?\n")
    time.sleep(1)

    _gender = input("What is your gender identification? (more genders to come)\nA) Male\nB) Female\nC) Non binary\n")
    _gender = _gender.lower()
    time.sleep(1)

    options = ["a","b","c"]

    while _gender not in options:
        print("That is not a valid gender. Please try again.")
        time.sleep(1)
        _gender = input("What is your gender identification? (more genders to come)\nA) Male\nB) Female\nC) Non binary\n")
        time.sleep(1)
        _gender = _gender.lower()

    _sorientation = input("What is your sexual orientation? (more to come)\nA) Male attracted\nB) Female Attracted\nC) Bisexual\nD) Pansexual\n")
    _sorientation = _sorientation.lower()
    options = ["a","b","c","d"]

    while _sorientation not in options:
        print("That is not a valid orientation. Please try again.")
        time.sleep(1)
        _sorientation = input("What is your sexual orientation? (more to come)\nA) Male attracted\nB) Female Attracted\nC) Bisexual\nD) Pansexual\n")
        time.sleep(1)
        _sorientation = _sorientation.lower()

    _break = "0"
    while _break == "0":
        _age = input("What is your age?\n")
        time.sleep(1)
        try:
            _age = int(_age)
            _break = "1"
        except:
            print("That is not a valid age. Please make it be a number")
            _break = "0"
            time.sleep(1)

    time.sleep(1)
    _info = dict(username=_username, gender=_gender, age=_age, sorientation=_sorientation, relationship="single")
    _status = dict()
    _inventory = dict(money=0, weapon="none")
    _user = dict(info=_info, status=_status, inventory=_inventory)

    _combat = dict(monster="none", fighting="no")
    _progress = dict(chapter="1", location="location a")
    _environment = dict(progress=_progress, combat=_combat)

    game_data["user"] =  json.dumps(_user)
    game_data["environment"] = json.dumps(_environment)
    print("COngradulations, {} you have registered!".format(_username))
    time.sleep(1)
    print('saving, do not exit.')
    f = open("game_data.txt", "w")
    for i in game_data:
        _dict = json.loads(game_data[i])
        f.write(json.dumps([i,_dict])+"\n")
    f.close()
    time.sleep(1)
    print('saving done')
    time.sleep(1)

def resume():
        env_dict = json.loads(game_data["environment"])
        print("Resuming game. Chapter: {}, Location: {}.".format(env_dict["progress"]["chapter"], env_dict["progress"]["location"]))
        _local["resume"] = "no"
        time.sleep(1)

def interact():
    command = input("command: ")
    time.sleep(1)
    if len(command) > 0:
            data = command.split(" ", 1)
            if len(data) > 1:
                func, data = data[0], data[1]
            else:
                func, data = data[0], ""
            func = func.lower()
            func = "game_"+func
            ret = 0
            if func == "game_exit":
                game_save('')
                _local["game"] = "off"
                ret = 1
            elif hasattr(sys.modules[__name__], func):
                ret = getattr(sys.modules[__name__], func)(data)
                time.sleep(1)
            if ret == 0:
                print('Not a valid command. Use "help" for more info.')
                time.sleep(1)

def random_event():
    env_dict = json.loads(game_data["environment"])
    current_location = env_dict["progress"]["location"]
    user_dict = json.loads(game_data["user"])
    a = []
    for i in _locations:
        for x in _locations[i]["events"]: #switch to local dict
            if x == "random":
                a.append(1)
            else:
                a.append(0)
    if 1 not in a:
        _choice = random.choice(list(_locations.keys()))
        __choice = _locations[_choice]
        __choice["events"].append("random")
        _local["r_e_notify"] = _choice

        event_choice = random.choice([i for i in events_dict["random"]]) #check if works

        _local["events"][_choice] = dict(random = event_choice)
        _local["random_event_number"] = "randomlyselectedeventnum"

    else:
        pass

def event_start():
    env_dict = json.loads(game_data["environment"])
    current_location = env_dict["progress"]["location"]

    _type = _locations[current_location]["events"]
    if "random" in _type:
        _type = "random" #fix this
    else:
        _type = "story" #fix this.

    _choice = input("There is a {} event here... do you wish to engage? Y/N\n".format(_type))
    time.sleep(1)
    _choice = _choice.lower()
    options = ["y","n"]
    while _choice not in options:
        print("That is not a choice. Please try again.")
        time.sleep(1)
        _choice = input("There is a {} event here... do you wish to engage? Y/N\n".format(_type))
        time.sleep(1)
        _choice = _choice.lower()

    if _choice == "y":
        print("Starting {} event".format(_type))
        event_id = _local["events"][current_location]["random"]
        load_id = events_dict["random"][event_id]

        #event_run("random", _id)

        time.sleep(1)
        del _local["events"][current_location]
        _locations[current_location]["events"].remove("random")
        print("Event Finished...")
    else:
        print("Canceling")

#def event_run(_type, _id):


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
    _trigger = random.choice(list(range(2)))
    if _trigger == 1:
        random_event()

    try:
        env_dict = json.loads(game_data["environment"])
        current_location = env_dict["progress"]["location"]
        if x == current_location:
            print("You are already here.")
            return

        current_nearby = _locations[current_location]["nearby"]
        if x == "info":
            print("I am near by [{}]".format(", ".join(current_nearby)))
            return
        elif x == "list":
            print("Locations Accessible to you: " + ", ".join(_locations.keys()))
            return
        dest_nearby = _locations[x]["nearby"]
        a = set(dest_nearby)
        b = set(current_nearby)
        if (a & b):
            _link = list(a&b)
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
    print("Saving... do not exit")
    f = open("game_data.txt", "w")
    for i in game_data:
        _dict = json.loads(game_data[i])
        f.write(json.dumps([i,_dict])+"\n")
    f.close()
    time.sleep(1)
    print('Saving done')

def game_help(x):
    if len(x) >0:
        try:
            print(x + ": " +_commands[x])
        except:
            print("That is not a valid command")
    else:
        print('Commands so far: [help, reset, exit, test, save, travel]\nUse the help command to check individual commands, like "help reset", to show what reset does.')
