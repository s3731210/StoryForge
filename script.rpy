define e = Character("")

screen foyerimagemap:
    add "foyerlightson"
    add "minimapfoyer" at topright


    imagebutton idle "vcuestar" hover "vcuedoor" xpos 151 ypos 320 clicked Return ("clro")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 501 ypos 337 clicked Return ("bb")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 677 ypos 341 clicked Return ("dralo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1072 ypos 320 clicked Return ("llo")
    #interact with clock

screen livingimagemap:
    add "livinglightson"
    add "minimaplivingroom" at topright

    imagebutton idle "vcuestar" hover "vcuering" xpos 420 ypos 351 clicked Return ("lamp")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 586 ypos 336 clicked Return ("sl")

screen diningroomimagemap:
    add "dininglightson"
    add "minimapdiningroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 28 ypos 545 clicked Return ("bl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 409 ypos 338 clicked Return ("kl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 885 ypos 337 clicked Return ("sl")


screen childsroomimagemap:
    add "childsroomlightson"
    add "minimapchildsroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1017 ypos 338 clicked Return ("bl")

screen bathroomimagemap:
    add "bathroomlights"
    add "minimapbathroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 586 ypos 324 clicked Return ("mblo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 746 ypos 330 clicked Return ("drlo")

screen masterbedroomimagemap:
    add "masterbedroomlights"
    add "minimapmasterbedroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1017 ypos 338 clicked Return ("mblo")

screen kitchenimagemap:
    add "kitchenlights"
    add "minimapkitchen" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1017 ypos 338 clicked Return ("mblo")

screen garageimagemap:
    add "garagelights"
    add "minimapgarage" at topright

label start:

    e "The sun is setting on what you can only envisage as a pleasant evening."

    e "You are out on a stroll with Wick, a Golden Retriever, who has been your
      faithful companion for 8 years."

    show wick

    e "Out of the blue, he appears agitated and begins frantically pacing about.
    Before you can attempt to console him, he dashes off,"
    e "heading straight into a grove."

    hide wick
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

    scene foyerlightsoff

    e "You pull out your handy iPhone and switch on the flashlight app
       for some illumination."

    scene foyerlightson

    e  "You examine your surroundings to discover the interior is as rundown
        as its exterior, and you catch a whiff of the stale air."

    e  "As you turn around, you notice the door is now closed, although you
        are certain you didn't close it, nor did you hear it shut.
        You attempt to open it, only to discover it is now locked."

    e  "Fear starts creeping in again, but you muster your willpower
        to resist it. You decide it doesn't matter, since you will not
        be leaving this house without your dog."

    e  "You hear something familiar yet faint in the dark. You spin around, “WICK!”"

    e  "Your eyes dart around what appears to be a foyer. Your heart is pounding
        as you take your first step forward into the darkness.
        You need to explore this house. You need to find your dog."

label foyer :
    call screen foyerimagemap
    $ result = _return
    if result == "bb" :
         e "ugh it wont budge!"
         jump foyer

    if result == "clro" :
        scene childsroomlightson
        with fade
        jump childsroom

    if result == "dralo" :
          scene dininglightson
          with fade
          jump diningroom

    if result == "llo" :
        scene livinglightson
        with fade
        jump livingroom

label livingroom :
    call screen livingimagemap
    $ result = _return

    if result == "lamp" :
        e "the power is out!"
        jump livingroom

    if result == "sl" :
        e "its locked"
        jump livingroom

label childsroom :
    call screen childsroomimagemap
    $ result = _return

    if result == "bl" :
        scene bathroomlights
        with fade
        jump bathroom

label bathroom :
    call screen bathroomimagemap
    $ result = _return

    if result == "mblo" :
         scene masterbedroomlights
         with fade
         jump masterbedroom

    if result == "drlo" :
        scene dininglightson
        with fade
        jump diningroom

label diningroom :
    call screen diningroomimagemap
    $ result = _return

    if result == "sl" :
        e "its locked"
        jump diningroom

    if result == "kl" :
        scene kitchenlights
        with fade
        jump kitchen

    if result == "bl" :
        scene bathroomlights
        with fade
        jump bathroom

label masterbedroom :
    call screen masterbedroomimagemap
    $ result = _return

    if result == "kl" :
        scene kitchenlights
        with fade
        jump kitchen

label kitchen :
    call screen kitchenimagemap
    $ result = _return

    if result == "gl" :
        scene garagelights
        with fade
        jump garage

label garage :
    call screen garageimagemap
    $ result = _return

    e " Test end of script "

    e "fin"

#label study :


    return
