import commands
import time
import json
from text import game_data

if len(game_data) > 0:
    commands._local["resume"] = "yes"


while commands._local["game"] == "on":

    if len(game_data) > 0:
        env_dict = json.loads(game_data["environment"])
        if commands._local["resume"] == "yes":
            commands.resume()
        else:
            if commands._local["r_e_notify"] != 0:
                print("there is a disturbance in {}....".format(commands._local["r_e_notify"]))
                commands._local["r_e_notify"] = 0
                time.sleep(1)

            if env_dict["progress"]["location"] in commands._local["events"]:
                commands.event_start()
                commands.interact()
            commands.interact()


    else:
        commands.register()
