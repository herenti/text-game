events_dict = {
    "story": {
        "1.1":{
            "stages":{
                "1":{"game_text":"content"},
                "2":{"input":"content"},
                "3":{"fight":"thingtofight"},
                #return from fight back into stage progression
                "4":{"finish":"content"}

                            }
                    },

        "1.2":{

            "stages":{
                "1":{"etc":"etc"}
                    }

            }

            },
    "random":{ #randomly chosen, monster strength by level and type randomly chosen from a range based on level
        "1":{
            "stages":{
                "1":{"fight":"monsterselection"},
                "2":{"finish":"content"}
                }
            },
        "2":{ #social or comedy event, only have these events happen once
            "stages":{
                "1":{"game-text":"content"},
                "2":{"finish":"content"}
                }
            }

        }
}
