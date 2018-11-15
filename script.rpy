define e = Character("")
default fuel = False
default oil = False
default hammer = False
default screwd = False
default studykey = False

screen foyerimagemap:
    add "foyerlightsofflighten"
    add "minimapfoyer" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 151 ypos 320 clicked Return ("clro")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 501 ypos 337 clicked Return ("bb")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 677 ypos 341 clicked Return ("dralo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1072 ypos 320 clicked Return ("llo")
    #interact with clock

screen livingimagemap:
    add "livinglightsoff"
    add "minimaplivingroom" at topright

    imagebutton idle "vcuestar" hover "vcuering" xpos 420 ypos 351 clicked Return ("lamp")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 586 ypos 336 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 75 ypos 525 clicked Return ("flo")

screen diningroomimagemap:
    add "dininglightsoff"
    add "minimapdiningroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 28 ypos 545 clicked Return ("bl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 409 ypos 338 clicked Return ("kl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 885 ypos 337 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 734 ypos 683 clicked Return ("flo")

screen childsroomimagemap:
    add "childlightsoff"
    add "minimapchildsroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1017 ypos 338 clicked Return ("bl")

screen bathroomimagemap:
    add "bathroomnolights"
    add "minimapbathroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 586 ypos 324 clicked Return ("mblo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 746 ypos 330 clicked Return ("drlo")

screen masterbedroomimagemap:
    add "masterbedroomnolights"
    add "minimapmasterbedroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 704 ypos 344 clicked Return ("mblo")

screen kitchenimagemap:
    add "kitchennolights"
    add "minimapkitchen" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1051 ypos 342 clicked Return ("gnl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 728 ypos 658 clicked Return ("drlo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 16 ypos 413 clicked Return ("mblo")

screen garageimagemapdark:
    add "garagenolights"
    add "minimapgarage" at topright

    imagebutton idle "garagefueldark" hover "garagefueldark" xpos 318 ypos 481 clicked Return ("fuel")
    imagebutton idle "vcuestar" hover "vcuering" xpos 1069 ypos 407 clicked Return ("generator")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 874 ypos 689 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 34 ypos 390 clicked Return ("kl")

##################################################################################################
#################################################Lights_are_on####################################
##################################################################################################


screen garagelightimagemap:
    add "garagelights"
    add "minimapgarage" at topright

    imagebutton idle "garagetoolboxlight" hover "garagetoolboxlight" xpos 661 ypos 439 clicked Return ("toolbox")
    imagebutton idle "garageoillight" hover "garageoillight" xpos 581 ypos 404 clicked Return ("oil")
    imagebutton idle "garagescrewdriverdark" hover "garagescrewdriverdark" xpos 341 ypos 343 clicked Return ("screwdriver")
    imagebutton idle "garagehammerlight" hover "garagehammerlight" xpos 396 ypos 341 clicked Return ("ham")
    imagebutton idle "vcuestar" hover "vcuering" xpos 874 ypos 689 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 34 ypos 390 clicked Return ("kl")

screen garagelight2imagemap:
    add "garagelights"
    add "minimapgarage" at topright

    imagebutton idle "vcuestar" hover "vcuering" xpos 874 ypos 689 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 34 ypos 390 clicked Return ("kl")


screen studylightimagemap :
    add "studylights"
    add "minimapstudy" at topright

screen foyerlightimagemap:
    add "foyerlightson"
    add "minimapfoyer" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 151 ypos 320 clicked Return ("clro")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 501 ypos 337 clicked Return ("bb")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 677 ypos 341 clicked Return ("dralo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1072 ypos 320 clicked Return ("llo")
    #interact with clock

screen livinglightimagemap:
    add "livinglightson"
    add "minimaplivingroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 586 ypos 336 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 75 ypos 525 clicked Return ("flo")

screen diningroomlightimagemap:
    add "dininglightson"
    add "minimapdiningroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 28 ypos 545 clicked Return ("bl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 409 ypos 338 clicked Return ("kl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 885 ypos 337 clicked Return ("sl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 734 ypos 683 clicked Return ("flo")

screen childsroomlightimagemap:
    add "childlightson"
    add "minimapchildsroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1017 ypos 338 clicked Return ("bl")

screen bathroomlightimagemap:
    add "bathroomlights"
    add "minimapbathroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 586 ypos 324 clicked Return ("mblo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 746 ypos 330 clicked Return ("drlo")

screen masterbedroomlightimagemap:
    add "masterbedroomlights"
    add "minimapmasterbedroom" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 704 ypos 344 clicked Return ("mblo")

screen kitchenlightimagemap:
    add "kitchenlights"
    add "minimapkitchen" at topright

    imagebutton idle "vcuestar" hover "vcuedoor" xpos 1051 ypos 342 clicked Return ("gnl")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 728 ypos 658 clicked Return ("drlo")
    imagebutton idle "vcuestar" hover "vcuedoor" xpos 16 ypos 413 clicked Return ("mblo")

label start:

    e "The sun is setting on what you can only envisage as a pleasant evening."

    show wick

    e "You are out on a stroll with Wick, a Golden Retriever, who has been your
      faithful companion for 8 years."

    e "Out of the blue, he appears agitated and begins frantically pacing about.
    Before you can attempt to console him, he dashes off,"
    e "heading straight into a grove."

    hide wick

    e "You give chase, desperately trying to keep up,
       but it's not long before you lose sight of him."

    e  "Still, you are determined to bring him back, and you
     decide to pursue in the same general direction. You run
     for what feels like an eternity."

    scene woods

    e "Just as you are about to collapse from exhaustion, you catch
     a glimpse of something beyond a cluster of trees."

    e "Amidst the scarce lighting you can barely discern what appears
       to be a house - a very old and dilapidated house."

    scene housedistant

    e "There seems to be no sign of any occupants, but you approach the house,
       still gasping for breath."

    scene houseclose

    "As you close in on the front door, you notice a faint glint on the floor."

    scene handscene

    e  "Upon closer inspection, you recognise the small metal plate - a dog tag
        engraved, Wick. In a moment you are assaulted by a flurry of questions,
        and panic sets in."

    e  "As you are haunted by the thought of your poor friend suffering,
        fear soon turns to fury and everything is drowned out by one
        overriding sentiment: NO ONE... MESSES... WITH... MY DOG!"

    e  "Without hesitation, you decide to barge in, not even giving a
       thought to knocking on the door. Surprisingly, the door offers no
       resistance, as it swings wide open."

    scene foyerlightsoff

    e "You enter the house, unfazed by the total darkness. You shout out his
       name at the top of your lungs, but you are met with an eerie silence.
       It finally registers that you can't even see your own feet."

    e "You pull out your handy iPhone and switch on the flashlight app
       for some illumination."

    scene foyerlightsofflighten

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

label foyerdark :
    call screen foyerimagemap
    $ result = _return
    if result == "bb" :
         e "ugh it wont budge!"
         jump foyerdark

    if result == "clro" :
        scene childlightsoff
        with fade
        "I really need to get some lights on"
        jump childroomdark

    if result == "dralo" :
          scene dininglightsoff
          with fade
          jump diningroomdark

    if result == "llo" :
        scene livinglightsoff
        with fade
        jump livingroomdark

label livingroomdark :
    call screen livingimagemap
    $ result = _return

    if result == "lamp" :
        e "the power is out!"
        jump livingroomdark

    if result == "sl" :
        e "its locked"
        jump livingroomdark

    if result == "flo" :
        scene foyerlightsofflighten
        with fade
        "Must be a generator or something around here"
        jump foyerdark

label childroomdark :
    call screen childsroomimagemap
    $ result = _return

    if result == "bl" :
        scene bathroomnolights
        with fade
        "It's so dark!"
        jump bathroomdark

label bathroomdark :
    call screen bathroomimagemap
    $ result = _return

    if result == "mblo" :
         scene masterbedroomnolights
         with fade
         jump masterbedroomdark

    if result == "drlo" :
        scene dininglightsoff
        with fade
        jump diningroomdark

label diningroomdark :
    call screen diningroomimagemap
    $ result = _return

    if result == "sl" :
        e "its locked"
        jump diningroomdark

    if result == "kl" :
        scene kitchennolights
        with fade
        "The generator has to be near here"
        jump kitchendark

    if result == "bl" :
        scene bathroomnolights
        with fade
        jump bathroomdark
    if result == "flo" :
        scene foyerlightsoff
        with fade
        "Must be a generator or something around here"
        jump foyerdark

label masterbedroomdark :
    call screen masterbedroomimagemap
    $ result = _return

    if result == "kl" :
        scene kitchennolights
        with fade
        jump kitchendark

label kitchendark :
    call screen kitchenimagemap
    $ result = _return

    if result == "gnl" :
        scene garagenolights
        with fade
        e "Yes the generator! Need to get this thing on"
        jump garagedark

    if result == "mblo" :
        scene masterbedroomnolights
        with fade
        jump masterbedroomdark

    if result == "drlo" :
        scene dininglightsoff
        with fade
        jump diningroomdark

label garagedark :
    call screen garageimagemapdark

    $ result = _return

    if result == "kl" :
        scene kitchennolights
        with fade
        jump kitchendark

    if result == "sl" :
        e "It is locked"
        jump garagedark

    if result == "fuel" :
        scene garagenolights
        $ fuel = True
        "Picked up fuel"
        jump garagedark

    if result == "generator" :

        if fuel == True :
            scene garagelights
            e "Thats done it!"
            e "Now I can finally find out what is happening here!"
            jump garagelight
        if fuel != True :
            scene garagenolights
            e "It wont start... Maybe needs some fuel"
            jump garagedark

label garagelight :
    call screen garagelightimagemap
    $ result = _return

    if result == "oil" :
        scene garagelights
        $ oil = True
        e "Picked up oil"
        jump garagelight

    if result == "screwdriver" :
        scene garagelights
        $ screwd = True
        e "Picked up screwdriver"
        jump garagelight

    if result == "ham" :
        scene garagelights
        $ hammer = True
        e "Picked up hammer"
        jump garagelight


    if result == "toolbox" :

        if oil == True and screwd == True and hammer == True :
            scene garagelights
            $ studykey = True
            e "That opened it, Yes!"
            e "Hmm, a old key. Wonder what this is for..."
            jump garagelight

        if oil != True or screwd != True or hammer != True :
            scene garagelights
            e "UGH! Need something else to help me open this Dam Thing!"
            jump garagelight

    if result == "sl" :

        if studykey == True :
            scene studylights
            with fade
            jump study
        if studykey != True :
            scene garagelights
            e "Locked"
            jump garagelight

##########################################################################################
#########################################Lights_labels####################################
##########################################################################################

label studylight :
    call screen studylightimagemap
    e " Test end of script "

    e "fin"

label foyerlight :
    call screen foyerlightimagemap
    $ result = _return
    if result == "bb" :
         e "ugh it wont budge!"
         jump foyerlight

    if result == "clro" :
        scene childlightson
        with fade
        jump childroomlight

    if result == "dralo" :
          scene dininglightson
          with fade
          jump diningroomlight

    if result == "llo" :
        scene livinglightson
        with fade
        jump livingroomlight

label livingroomlight :
    call screen livinglightimagemap
    $ result = _return

    if result == "sl" :
        scene studylights
        with fade
        jump studylight

    if result == "flo" :
        scene foyerlightson
        with fade
        jump foyerlight

label childroomlight :
    call screen childsroomlightimagemap
    $ result = _return

    if result == "bl" :
        scene bathroomlightson
        with fade
        "It's so dark!"
        jump bathroomlight

label bathroomlight :
    call screen bathroomlightimagemap
    $ result = _return

    if result == "mblo" :
         scene masterbedroomlights
         with fade
         jump masterbedroomlight

    if result == "drlo" :
        scene dininglightson
        with fade
        jump diningroomlight

label diningroomlight :
    call screen diningroomlightimagemap
    $ result = _return
   
    if result == "sl" :
        scene studylights
        with fade
        jump studylight

    if result == "kl" :
        scene kitchenlights
        with fade
        jump kitchenlight

    if result == "bl" :
        scene bathroomlights
        with fade
        jump bathroomlight

    if result == "flo" :
        scene foyerlightson
        with fade
        jump foyerlight

label masterbedroomlight :
    call screen masterbedroomlightimagemap
    $ result = _return

    if result == "kl" :
        scene kitchenlights
        with fade
        jump kitchenlight

label kitchenlight :
    call screen kitchenlightimagemap
    $ result = _return

    if result == "gnl" :
        scene garagelights
        with fade
        jump garagelight

    if result == "mblo" :
        scene masterbedroomlights
        with fade
        jump masterbedroomlight

    if result == "drlo" :
        scene dininglightson
        with fade
        jump diningroomlight

label garagelight2 :    ####Garage scene with no items left ot collect

    call screen garagelight2imagemap
    $ result = _return

    


    return
