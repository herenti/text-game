import commands
import time
import json
from text import game_data

if len(game_data) > 0:
    user_dict = json.loads(game_data["user"])
    env_dict = json.loads(game_data["environment"])
    env_dict["resume"] = "yes"
    game_data["environment"] = json.dumps(env_dict)





while commands._local["game"] == "on":

    def resume():
        env_dict = json.loads(game_data["environment"])
        print("Resuming game. Chapter: {}, Location: {}.".format(env_dict["progress"]["chapter"], env_dict["progress"]["location"]))
        env_dict["resume"] = "no"
        game_data["environment"] = json.dumps(env_dict)
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
                    commands.game_save('')
                    commands._local["game"] = "off"
                    ret = 1
                elif hasattr(commands, func):
                    ret = getattr(commands, func)(data)
                    time.sleep(1)
                if ret == 0:
                    print('Not a valid command. Use "help" for more info.')
                    time.sleep(1)

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
        _environment = dict(progress=_progress, combat=_combat, resume="no")

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


    if len(game_data) > 0:
        env_dict = json.loads(game_data["environment"])
        if env_dict["resume"] == "yes":
            resume()
        else:
            if commands._local["r_e_notify"] != 0:
                print("there is a disturbance in {}....".format(commands._local["r_e_notify"]))
                commands._local["r_e_notify"] = 0
                time.sleep(1)

            if env_dict["progress"]["location"] in commands._local["events"]:
                commands.event_start()
                interact()
            interact()


    else:
        register()
