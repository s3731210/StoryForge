# StoryForge
As per week 5 Activity 
﻿define e = Character("")
default sawp = False
default oilp = False
default oilpo = False


screen garageimagemap:
    add "garagelights"

    imagebutton idle "garagesaw" hover "garagesaw" xpos 151 ypos 320 clicked Return ("saw")
    imagebutton idle "vcuestar" hover "vcuering" xpos 1017 ypos 320 clicked Return ("generator")
    imagebutton idle "garageoil" hover "garageoil" xpos 500 ypos 401 clicked Return ("go")
    #imagebutton idle "garagescrewdriverlight" hover "garagescrewdriverlight" xpos 546 ypos 200 clicked Return ("go2")

label start:

    call screen garageimagemap

    $ result = _return

    if result == "saw" :
        scene garagelights
        $ sawp = True
        "Picked up saw"
        jump start

    if result == "go" :
        scene garagelights
        $ oilp = True
        "Picked up Oil"
        jump start

    if result == "go2" :
        scene garagelights
        $ oilpo = True
        "Picked up Oil2"
        jump start


    if result == "generator" :

        if sawp == True and oilp == True and oilpo == True :
            scene garagelights
            "turn on"
        if sawp != True or oilp != True or oilpo != True :
                scene garagelights
                e "It does not turn on maybe I need more tools"
                jump start
    e " ello"


    # This ends the game.

    return
