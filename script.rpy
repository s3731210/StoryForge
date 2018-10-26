# StoryForge
﻿define e = Character("")

screen foyer_imagemap:
    add "foyer_lights_on"

    imagebutton idle "dot" hover "vcue_door" xpos 177 ypos 349 clicked Return ("clro")
    imagebutton idle "dot" hover "vcue_door" xpos 678 ypos 346 clicked Return ("dralo")
    imagebutton idle "dot" hover "vcue_door" xpos 508 ypos 352 clicked Return ("bb")

label start:

    e "The sun is setting on what you can only envisage as a pleasant evening."

    e "You are out on a stroll with Wick, a Golden Retriever, who has been your
      faithful companion for 8 years."
      
    #show wick
    
    e "Out of the blue, he appears agitated and begins frantically pacing about.
    Before you can attempt to console him, he dashes off,"
    e "heading straight into a grove."
    
    #hide wick
    #show you

    e "You give chase, desperately trying to keep up,
       but it's not long before you lose sight of him."

    e  "Still, you are determined to bring him back, and you
     decide to pursue in the same general direction. You run
     for what feels like an eternity."

    e "Just as you are about to collapse from exhaustion, you catch
     a glimpse of something beyond a cluster of trees."

    e "Amidst the scarce lighting you can barely discern what appears
       to be a house - a very old and dilapidated house."

       #show house

    e "There seems to be no sign of any occupants, but you approach the house,
       still gasping for breath. As you close in on the front door, you notice
       a faint glint on the floor."

    e  "Upon closer inspection, you recognise the small metal plate - a dog tag
        engraved, Wick. In a moment you are assaulted by a flurry of questions,
        and panic sets in."

    e  "As you are haunted by the thought of your poor friend suffering,
        fear soon turns to fury and everything is drowned out by one
        overriding sentiment: NO ONE... MESSES... WITH... MY DOG!"

    e  "Without hesitation, you decide to barge in, not even giving a
       thought to knocking on the door. Surprisingly, the door offers no
       resistance, as it swings wide open."

    e "You enter the house, unfazed by the total darkness. You shout out his
       name at the top of your lungs, but you are met with an eerie silence.
       It finally registers that you can't even see your own feet."

    scene foyer_lights_off

    e "You pull out your handy iPhone and switch on the flashlight app
       for some illumination."

    scene foyer_lights_on

    e  "You examine your surroundings to discover the interior is as rundown
        as its exterior, and you catch a whiff of the stale air."

    e  "As you turn around, you notice the door is now closed, although you
        are certain you didn't close it, nor did you hear it shut.
        You attempt to open it, only to discover it is now locked."

    e  "Fear starts creeping in again, but you muster your willpower
        to resist it. You decide it doesn't matter, since you will not
        be leaving this house without your dog."


label foyer :
    call screen foyer_imagemap

    $ result = _return
    if result == "bb" :
         e "ugh it wont budge!"
         jump foyer

    if result == "clro" :
     scene childs_room_lights_on
     e "test"

    if result == "dralo" :
     scene dining_room_all_lights_on
     e "test"




    e "test"

    return
