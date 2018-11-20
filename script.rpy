define e = DynamicCharacter("hero", image="hero")
define hero = "Ash"
image side hero = "hero_side.png"

init:
    $renpy.music.register_channel("extraAudio", "sfx", True)
    $renpy.music.register_channel("extraAudio2", "sfx", True)

default debug = True
default skipIntro = False

default MAX_HP = 3
# Begin with 3 health units
default hp = MAX_HP
# Current room occupied by user
default curRoom = 8
# Current room haunted by ghost
default curGhostRoom = 7

default GHOST_MAX_HP = 3
default ghostHp = GHOST_MAX_HP

# ROOMS AND ASSOCIATED NUMBERS
# 1 Master Bedroom
# 2 Kitchen
# 3 Garage
# 4 Bathroom
# 5 Dining Room
# 6 Study
# 7 Childs Room
# 8 Foyer
# 9 Living Room

# Current section of the story user is at
default curSection = 1

default inRoom = True
default beginning = True
default studyUnlocked = False

# Flags for first time dialogues
default firstKitchen = True
default firstGarage = True
default firstBathroom = True
default firstDiningRoom = True
default firstChildsRoom = True
default firstStudy = True

default firstPoweredKitchen = False
default firstS2Kitchen = True
default firstS3Foyer = True
default firstS4Foyer = True

default isFirstEncounter = True
default ghostActive = False
default isTeddyBearMoving = False
default teddyBearLocation = 0
default ghostOldLocation = 0
default hasTeddyBear = False

default hasConcludedInvestigation = False

default saltCount = 0
default isTrapSet = False
default isDoor1Salted = False
default isDoor2Salted = False

default confrontationChoice = 0
# Confrontation Choices #
# 0. Fight the ghost
# 1. Banish the ghost
# 2. Speak with the ghost

default isConfrontingGhost = False

default hasBeenOiled = False

default hasViewedDiary = False
default hasViewedBook = False
default hasViewedPhoto = False

default hasCanvas = False
default hasSoot = False
default hasBanishingCircle = False
default isBanishingCircleCorrect = True

# ROOM LIGHT STATE
default masterBedroomLight = 0
default kitchenLight = 0
default garageLight = 0
default bathroomLight = 0
default diningRoomLight = 0
default studyLight = 0
default childsRoomLight = 0
default foyerLight = -1
default livingRoomLight = 0

default masterBedroomLamp1 = 0
default masterBedroomLamp2 = 0
default bathroomLamp1 = 0
default bathroomLamp2 = 0
default bathroomLamp3 = 0
default diningRoomLamp1 = 0
default studyLamp1 = 0
default studyLamp2 = 0
default childsRoomLamp1 = 0
default childsRoomLamp2 = 0
default livingRoomLamp1 = 0

image sceneMasterBedroom dark = "masterbedroomnolights.png"
image sceneMasterBedroom light = "masterbedroommainlight.png"

image sceneKitchen dark = "kitchennolights.png"
image sceneKitchen light = "kitchenlights.png"

image sceneGarage dark = "garagenolights.png"
image sceneGarage light = "garagelights.png"

image sceneBathroom dark = "bathroomnolights.png"
image sceneBathroom light = "bathroommainlight.png"

image sceneDiningRoom dark = "dininglightsoff.png"
image sceneDiningRoom light = "dininglightone.png"

image sceneStudy dark = "studynolights.png"
image sceneStudy light = "studymainlight.png"

image sceneChildsRoom dark = "childlightsoff.png"
image sceneChildsRoom light = "childmainlight.png"

image sceneFoyer darkest = "foyerlightsoff.png"
image sceneFoyer dark = "foyerlightsofflighten.png"
image sceneFoyer light = "foyerlightson.png"

image sceneLivingRoom dark = "livinglightsoff.png"
image sceneLivingRoom light = "livingmainlight.png"
image sceneLivingRoom darkNoPainting = "livingnopaintingnolight.png"
image sceneLivingRoom lightNoPainting = "livingnopaintinglight.png"

# Master Bedroom Light Overlays
image masterBedroomOverlay1 = "lightoverlay/masterlamp1.png"
image masterBedroomOverlay2 = "lightoverlay/masterlamp2.png"

# Bathroom Light Overlays
image bathroomOverlay1 = "lightoverlay/bathroomlamp1.png"
image bathroomOverlay2 = "lightoverlay/bathroomlamp2.png"
image bathroomOverlay3 = "lightoverlay/bathroomlamp3.png"

# Dining Room Light Overlays
image diningRoomOverlay1 = "lightoverlay/dininglamp1.png"

# Study Light Overlays
image studyOverlay1 = "lightoverlay/studylamp1.png"
image studyOverlay2 = "lightoverlay/studylamp2.png"

# Child's Room Light Overlays
image childsRoomOverlay1 = "lightoverlay/childslamp1.png"
image childsRoomOverlay2 = "lightoverlay/childslamp2.png"

# Living Room Light Overlays
image livingRoomOverlay1 = "lightoverlay/livinglamp1.png"

# Kitchen Scene Elements
image kitchenKnife dark = "interactive/kitchenknifedark.png"
image kitchenKnife light = "interactive/kitchenknifelight.png"
image kitchenSalt dark = "interactive/kitchensaltdark.png"
image kitchenSalt light = "interactive/kitchensaltlight.png"

# Garage Scene Elements
image fuel = "interactive/garagefuellight.png"
image oil dark = "interactive/garageoildark.png"
image oil light = "interactive/garageoillight.png"
image screwdriver dark = "interactive/garagescrewdriverdark.png"
image screwdriver light = "interactive/garagescrewdriverlight.png"
image hammer dark = "interactive/garagehammerdark.png"
image hammer light = "interactive/garagehammerlight.png"
image saw dark = "interactive/garagesawdark.png"
image saw light = "interactive/garagesawlight.png"
image toolbox dark = "interactive/garagetoolboxdark.png"
image toolbox light = "interactive/garagetoolboxlight.png"

# Dining Room Scene Elements
image candleStick dark = "interactive/diningcandlestickdark.png"
image candleStick light = "interactive/diningcandlesticklight.png"
image silverKnife dark = "interactive/diningknifedark.png"
image silverKnife light = "interactive/diningknifelight.png"
image diningRoomSalt dark = "interactive/kitchensaltdark.png"
image diningRoomSalt light = "interactive/kitchensaltlight.png"

# Study Scene Elements
image photo dark = "interactive/studyportraitdark.png"
image photo light = "interactive/studyportraitlight.png"
image letter dark = "interactive/studyletterdark.png"
image letter light = "interactive/studyletterlight.png"

# Foyer Scene Elements
image silverOrnament dark = "interactive/foyersilverornamentdark.png"
image silverOrnament light = "interactive/foyersilverornamentlight.png"

# Living Room Scene Elements
image silverLetterOpener dark = "interactive/livingletteropenerdark.png"
image silverLetterOpener light = "interactive/livingletteropenerlight.png"

# Teddy Bear
image teddyBear dark = "interactive/teddydark.png"
image teddyBear light = "interactive/teddylight.png"

# Animation for ghost attack
image ghost anim = Movie(play="ghost_anim.webm")

# Animation for best ending
image ghostholdingbaby anim = Movie(play="ghostholdingbaby.webm")

# I1. MASTER BEDROOM INTERACTIONS ##############################################

screen masterBedroomInteraction:
    imagebutton idle "minimapmasterbedroom" hover "minimapmasterbedroom" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 717 ycenter 350 clicked Return ("openNavMenu")

    # Music box hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 609 ycenter 375 clicked Return ("hintMasterBedroom")

    # Master Bedroom Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 676 ycenter 378 clicked Return ("lightMasterBedroomMain")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 172 ycenter 452 clicked Return ("lightMasterBedroomLamp1")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 526 ycenter 415 clicked Return ("lightMasterBedroomLamp2")

    if curSection > 1:
        # Silver Hairpin
        if hasSilverHairpin == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 761 ycenter 428 clicked Return ("takeSilverHairpin")

        imagebutton idle "vcuestar" hover "vcuering" xcenter 395 ycenter 530 clicked Return ("readDiary")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 1:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 899 ycenter 586 clicked Return ("wanderingTeddyBear")



# I2. KITCHEN INTERACTIONS #####################################################

screen kitchenInteraction:
    imagebutton idle "minimapkitchen" hover "minimapkitchen" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 1071 ycenter 342 clicked Return ("openNavMenu")

    # Utensils clanking hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 407 ycenter 373 clicked Return ("hintKitchen")

    # Kitchen Light
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 981 ycenter 375 clicked Return ("lightKitchenMain")

    if curSection > 1:
        # Kitchen Knife
        if hasKitchenKnife == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 481 ycenter 440 clicked Return ("takeKitchenKnife")

        # Kitchen Salt
        if hasKitchenSalt == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 724 ycenter 428 clicked Return ("takeKitchenSalt")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 2:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 386 ycenter 604 clicked Return ("wanderingTeddyBear")


# I3. GARAGE INTERACTIONS ######################################################

screen garageInteraction:
    imagebutton idle "minimapgarage" hover "minimapgarage" xpos 1126 ypos 10 clicked Return("openNavMenu")

    # Radio noise hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 349 ycenter 445 clicked Return ("hintGarage")

    # Garage Light
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 699 ycenter 381 clicked Return ("lightGarageMain")

    if curSection == 1:
        # Generator
        imagebutton idle "vcuestar" hover "vcuering" xcenter 1072 ycenter 394 clicked Return ("generator")
        # Fuel
        if hasFuel == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 269 ycenter 550 clicked Return ("takeFuel")

    if curSection == 2:
        if hasOil == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 510 ycenter 397 clicked Return ("takeOil")

        if hasScrewdriver == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 424 ycenter 403 clicked Return ("takeScrewdriver")

        if hasToolbox == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 659 ycenter 454 clicked Return ("takeToolbox")

    if curSection > 1:
        if hasHammer == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 407 ycenter 380 clicked Return ("takeHammer")

        if hasSaw == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 282 ycenter 382 clicked Return ("takeSaw")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 3:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 136 ycenter 635 clicked Return ("wanderingTeddyBear")


# I4. BATHROOM INTERACTIONS ####################################################

screen bathroomInteraction:
    imagebutton idle "minimapbathroom" hover "minimapbathroom" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 603 ycenter 329 clicked Return ("toiletDoor")
    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 758 ycenter 332 clicked Return ("openNavMenu")

    # Tap running hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 887 ycenter 439 clicked Return ("hintBathroom")

    # Bathroom Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 697 ycenter 386 clicked Return ("lightBathroomMain")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 444 ycenter 340 clicked Return ("lightBathroomLamp1")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 688 ycenter 343 clicked Return ("lightBathroomLamp2")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 1012 ycenter 337 clicked Return ("lightBathroomLamp3")

    if curSection > 1:
        if hasBathroomSalt == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 868 ycenter 529 clicked Return ("takeBathroomSalt")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 4:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 473 ycenter 568 clicked Return ("wanderingTeddyBear")


# I5. DINING ROOM INTERACTIONS #################################################

screen diningRoomInteraction:
    imagebutton idle "minimapdiningroom" hover "minimapdiningroom" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 424 ycenter 347 clicked Return ("openNavMenu")
    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 905 ycenter 342 clicked Return ("openNavMenu")

    # Glasses clanking hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 1107 ycenter 440 clicked Return ("hintDiningRoom")

    # Dining Room Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 370 ycenter 380 clicked Return ("lightDiningRoomMain")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 1211 ycenter 401 clicked Return ("lightDiningRoomLamp1")

    if curSection > 1:
        if hasCandleStick == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 531 ycenter 436 clicked Return ("takeCandleStick")
        if hasSilverKnife == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 400 ycenter 454 clicked Return ("takeSilverKnife")
        if hasDiningRoomSalt == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 1051 ycenter 438 clicked Return ("takeDiningRoomSalt")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 5:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 284 ycenter 605 clicked Return ("wanderingTeddyBear")


# I6. STUDY INTERACTIONS #######################################################

screen studyInteraction :
    imagebutton idle "minimapstudy" hover "minimapstudy" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 499 ycenter 336 clicked Return ("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuering" xcenter 127 ycenter 401 clicked Return ("viewPhoto")
    imagebutton idle "vcuestar" hover "vcuering" xcenter 662 ycenter 344 clicked Return ("viewBook")

    if hasLetter == False:
        imagebutton idle "vcuestar" hover "vcuering" xcenter 248 ycenter 484 clicked Return ("takeLetter")
    if hasCheque == False:
        imagebutton idle "vcuestar" hover "vcuering" xcenter 154 ycenter 555 clicked Return ("takeCheque")
    if hasChloroform == False:
        imagebutton idle "vcuestar" hover "vcuering" xcenter 453 ycenter 492 clicked Return ("takeChloroform")

    # Study Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 434 ycenter 391 clicked Return ("lightStudyMain")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 296 ycenter 310 clicked Return ("lightStudyLamp1")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 860 ycenter 419 clicked Return ("lightStudyLamp2")

    # Teddy Bear
    if isTeddyBearMoving == True and teddyBearLocation == 6:
        imagebutton idle "vcuestar" hover "vcuering" xcenter 456 ycenter 606 clicked Return ("wanderingTeddyBear")


# I7. CHILD'S ROOM INTERACTIONS ################################################

screen childsRoomInteraction:
    imagebutton idle "minimapchildsroom" hover "minimapchildsroom" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 1044 ycenter 344 clicked Return ("openNavMenu")

    # Toy squeak hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 884 ycenter 592 clicked Return ("hintChildsRoom")

    # Child's Room Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 951 ycenter 390 clicked Return ("lightChildsRoomMain")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 77 ycenter 514 clicked Return ("lightChildsRoomLamp1")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 1230 ycenter 464 clicked Return ("lightChildsRoomLamp2")

    if curSection > 1:
        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 7:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 414 ycenter 583 clicked Return ("wanderingTeddyBear")

    if curSection > 2:
        # Crime Scene Investigation
        if hasViewedDiary and hasChloroform and hasCheque and hasLetter:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 585 ycenter 565 clicked Return ("clueStain")



# I8. FOYER INTERACTIONS #######################################################

screen foyerInteraction:
    imagebutton idle "minimapfoyer" hover "minimapfoyer" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 170 ycenter 322 clicked Return ("openNavMenu")
    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 513 ycenter 345 clicked Return ("basement")
    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 687 ycenter 349 clicked Return ("openNavMenu")
    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 1084 ycenter 320 clicked Return ("openNavMenu")

    # Clock chime hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 581 ycenter 320 clicked Return ("hintFoyer")

    # Foyer Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 991 ycenter 392 clicked Return ("lightFoyerMain")

    if curSection > 1:
        # Silver Ornament
        if hasSilverOrnament == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 337 ycenter 405 clicked Return ("takeSilverOrnament")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 8:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 636 ycenter 567 clicked Return ("wanderingTeddyBear")

    if curSection > 2:
    # Salting
        if isDoor1Salted == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 182 ycenter 641 clicked Return ("saltDoor1")

        if isDoor2Salted == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 1067 ycenter 630 clicked Return ("saltDoor2")

        if hasTeddyBear and isDoor1Salted and isDoor2Salted and saltCount > 0:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 626 ycenter 557 clicked Return ("setLure")


screen foyerInteractionEnd:
    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 513 ycenter 345 clicked Return ("basement")


# I9. LIVING ROOM INTERACTIONS #################################################

screen livingRoomInteraction:
    imagebutton idle "minimaplivingroom" hover "minimaplivingroom" xpos 1126 ypos 10 clicked Return("openNavMenu")

    imagebutton idle "vcuestar" hover "vcuedoor" xcenter 599 ycenter 346 clicked Return ("openNavMenu")

    # Window whistling hint
    imagebutton idle "vcuestar" hover "vcuering" xcenter 1104 ycenter 422 clicked Return ("hintLivingRoom")

    # Living Room Lights
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 558 ycenter 369 clicked Return ("lightLivingRoomMain")
    imagebutton idle "vcuestar" hover "vcuelight" xcenter 428 ycenter 410 clicked Return ("lightLivingRoomLamp1")

    if curSection > 1:
        # Silver Letter Opener
        if hasSilverLetterOpener == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 1023 ycenter 557 clicked Return ("takeSilverLetterOpener")

        # Teddy Bear
        if isTeddyBearMoving == True and teddyBearLocation == 9:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 405 ycenter 586 clicked Return ("wanderingTeddyBear")

    if curSection > 2:
        # Banishing Circle Construction
        if hasViewedBook and hasCanvas == False and hasBanishingCircle == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 246 ycenter 280 clicked Return ("takeCanvas")

        if hasViewedBook and hasSoot == False and hasBanishingCircle == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 254 ycenter 534 clicked Return ("takeSoot")

        if hasViewedBook and hasBanishingCircle == False:
            imagebutton idle "vcuestar" hover "vcuering" xcenter 666 ycenter 568 clicked Return ("makeBanishingCircle")


default kitchenKnifePos = Position(xpos=483, ypos=450)
default kitchenSaltPos = Position(xpos=724, ypos=430)
default fuelPos = Position(xpos=270, ypos=610)
default toolboxPos = Position(xpos=660, ypos=480)
default oilPos = Position(xpos=515, ypos=423)
default screwdriverPos = Position(xpos=425, ypos=400)
default hammerPos = Position(xpos=407, ypos=410)
default sawPos = Position(xpos=280, ypos=426)
default candleStickPos = Position(xpos=531, ypos=440)
default silverKnifePos = Position(xpos=400, ypos=460)
default diningRoomSaltPos = Position(xpos=1052, ypos=440)
default silverOrnamentPos = Position(xpos=339, ypos=434)
default silverLetterOpenerPos = Position(xpos=1027, ypos=573)

default photoPos = Position(xpos=129, ypos=460)
default letterPos = Position(xpos=257, ypos=505)

default kitchenWindowWritingPos = Position(xpos=614, ypos=370)

default teddyMasterBedroomPos = Position(xpos=899, ypos=636)
default teddyKitchenPos = Position(xpos=386, ypos=654)
default teddyGaragePos = Position(xpos=136, ypos=685)
default teddyBathroomPos = Position(xpos=473, ypos=618)
default teddyDiningRoomPos = Position(xpos=284, ypos=655)
default teddyStudyPos = Position(xpos=456, ypos=656)
default teddyChildsRoomPos = Position(xpos=414, ypos=633)
default teddyFoyerPos = Position(xpos=636, ypos=617)
default teddyLivingRoomPos = Position(xpos=405, ypos=636)

default hasSilverHairpin = False
default hasKitchenKnife = False
default hasKitchenSalt = False
default hasFuel = False
default hasOil = False
default hasScrewdriver = False
default hasHammer = False
default hasSaw = False
default hasToolbox = False
default hasBathroomSalt = False
default hasCandleStick = False
default hasSilverKnife = False
default hasDiningRoomSalt = False
default hasSilverOrnament = False
default hasSilverLetterOpener = False

#default hasPhoto = False
default hasLetter = False
default hasCheque = False
default hasChloroform = False



# HEALTH BAR
# 0 units of health
screen healthBar0:
    zorder 5
    add "health_depleted.png" xpos 0.02 ypos 0.02
    add "health_depleted.png" xpos 0.08 ypos 0.02
    add "health_depleted.png" xpos 0.14 ypos 0.02

# 1 unit of health
screen healthBar1:
    zorder 5
    add "health.png" xpos 0.02 ypos 0.02
    add "health_depleted.png" xpos 0.08 ypos 0.02
    add "health_depleted.png" xpos 0.14 ypos 0.02

# 2 units of health
screen healthBar2:
    zorder 5
    add "health.png" xpos 0.02 ypos 0.02
    add "health.png" xpos 0.08 ypos 0.02
    add "health_depleted.png" xpos 0.14 ypos 0.02

# 3 units of health
screen healthBar3:
    zorder 5
    add "health.png" xpos 0.02 ypos 0.02
    add "health.png" xpos 0.08 ypos 0.02
    add "health.png" xpos 0.14 ypos 0.02

######################################################################################
# BEGINNING ##########################################################################
######################################################################################

label start:
    scene black
    $hero = renpy.input("What is your name?")
    $hero = hero.strip()
    if hero == "":
        $hero = "Ash"

    # PROLOGUE
    if skipIntro == False:
        call prologue from _call_prologue

    # MAIN GAME
    #call playMusic

    if debug == True:
        # Set HP for debugging
        $inputHP = int(renpy.input("How much health do you want to start with?"))
        if inputHP > 3:
            $inputHP = 3
        elif inputHP < 0:
            $inputHP = 0
        $hp = int(inputHP)

        $inputEnd = renpy.input("Would you like me to take you to the end, fully armed and ready to kick ass? 'y' or 'n'")
        $inputEnd = inputEnd.lower().strip()
        if inputEnd == "y" or inputEnd == "yes" or inputEnd == "'y'" or inputEnd == "'yes'":
            $curSection = 4
            $hasConcludedInvestigation = True
            $hasBanishingCircle = True
            $hasSilverKnife = True
            $hasKitchenKnife = True
            $hasSilverLetterOpener = True
            $hasSaw = True
            $hasScrewdriver = True
            $hasHammer = True
            $hasSilverHairpin = True
            $hasSilverOrnament = True
            $hasCandleStick = True

            $inputBC = renpy.input("Is banishing circle correct? 'y' or 'n'")
            $inputBC = inputBC.lower().strip()
            if inputBC == "y" or inputEnd == "yes" or inputEnd == "'y'" or inputEnd == "'yes'":
                $isBanishingCircleCorrect = True
            else:
                $isBanishingCircleCorrect = False


    jump foyer


################################################################################
# MASTER BEDROOM ###############################################################
################################################################################
label masterBedroom:
    $curRoom = 1
    scene
    call doorOpen from _call_doorOpen
    call displayHealth from _call_displayHealth
    call checkTurn from _call_checkTurn
    call setTeddyLocation from _call_setTeddyLocation
    call displaySceneElements from _call_displaySceneElements
    call displayHealth from _call_displayHealth_1
    call ghostTurn from _call_ghostTurn

    if masterBedroomLamp1 == 0:
        hide masterBedroomOverlay1
    elif masterBedroomLamp1 == 1:
        show masterBedroomOverlay1 zorder 9

    if masterBedroomLamp2 == 0:
        hide masterBedroomOverlay2
    elif masterBedroomLamp2 == 1:
        show masterBedroomOverlay2 zorder 9

    if masterBedroomLight == 0:
        show sceneMasterBedroom dark
        with fade
    elif masterBedroomLight == 1:
        show sceneMasterBedroom light
        with fade

    while inRoom == True:
        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:
            call screen masterBedroomInteraction
            $ result = _return

            if result == "hintMasterBedroom":
                call intHintMasterBedroom from _call_intHintMasterBedroom

            if result == "takeSilverHairpin":
                call intSilverHairpin from _call_intSilverHairpin

            if result == "readDiary":
                call intDiary from _call_intDiary

            if result == "lightMasterBedroomMain":
                call intNoLights from _call_intNoLights
            if result == "lightMasterBedroomLamp1":
                call intNoLights from _call_intNoLights_1
            if result == "lightMasterBedroomLamp2":
                call intNoLights from _call_intNoLights_2

            if result == "openNavMenu":
                call navMenu from _call_navMenu

            call displaySceneElements from _call_displaySceneElements_1

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen masterBedroomInteraction
            $ result = _return

            if result == "hintMasterBedroom":
                call intHintMasterBedroom from _call_intHintMasterBedroom_1

            if result == "takeSilverHairpin":
                call intSilverHairpin from _call_intSilverHairpin_1

            if result == "readDiary":
                call intDiary from _call_intDiary_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_1

            if result == "lightMasterBedroomMain":
                call intLightMasterBedroomMain from _call_intLightMasterBedroomMain

            if result == "lightMasterBedroomLamp1":
                call intLightMasterBedroomLamp1 from _call_intLightMasterBedroomLamp1

            if result == "lightMasterBedroomLamp2":
                call intLightMasterBedroomLamp2 from _call_intLightMasterBedroomLamp2

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear

            call displaySceneElements from _call_displaySceneElements_2

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen masterBedroomInteraction
            $ result = _return

            if result == "hintMasterBedroom":
                call intHintMasterBedroom from _call_intHintMasterBedroom_2

            if result == "takeSilverHairpin":
                call intSilverHairpin from _call_intSilverHairpin_2

            if result == "readDiary":
                call intDiary from _call_intDiary_2

            if result == "openNavMenu":
                call navMenu from _call_navMenu_2

            if result == "lightMasterBedroomMain":
                call intLightMasterBedroomMain from _call_intLightMasterBedroomMain_1

            if result == "lightMasterBedroomLamp1":
                call intLightMasterBedroomLamp1 from _call_intLightMasterBedroomLamp1_1

            if result == "lightMasterBedroomLamp2":
                call intLightMasterBedroomLamp2 from _call_intLightMasterBedroomLamp2_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_1

            call displaySceneElements from _call_displaySceneElements_3

    return


################################################################################
# KITCHEN ######################################################################
################################################################################
label kitchen:
    $curRoom = 2
    scene
    call doorOpen from _call_doorOpen_1
    call displayHealth from _call_displayHealth_2
    call checkTurn from _call_checkTurn_1
    call setTeddyLocation from _call_setTeddyLocation_1
    call displaySceneElements from _call_displaySceneElements_4
    call displayHealth from _call_displayHealth_3
    call ghostTurn from _call_ghostTurn_1

    if kitchenLight == 0:
        show sceneKitchen dark
        with fade
    elif kitchenLight == 1:
        show sceneKitchen light
        with fade

    while inRoom == True:
        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:

            if firstKitchen == True:
                e "I can smell fuel. A generator must be near."
                $firstKitchen = False

            if firstPoweredKitchen == True:
                $firstPoweredKitchen = False
                e "Let's turn some lights on."
                $ renpy.pause(1, hard=True)
                call switchLight from _call_switchLight
                $kitchenLight = 1
                show sceneKitchen light
                call displaySceneElements from _call_displaySceneElements_5
                show kitchenwindowwriting at kitchenWindowWritingPos zorder 20
                e "{b}Woah!{/b}{fast} What the hell?!"
                call ghostScream from _call_ghostScream
                $ renpy.pause(0.5, hard=True)
                with vpunch
                "{b}* SCREAM *{/b}"
                $ renpy.pause(0.5, hard=True)
                e "{b}WHO'S THERE?!{/b}"
                "Your knees buckle and you feel you’re about to lose what’s left
                in your stomach. This house is haunted."
                "This thing has trapped me and Wick. You need to find something
                to protect yourself. You need to look around."
                #hide kitchenwindowwriting
                #with dissolve
                $curSection = 2
                jump kitchen


            call screen kitchenInteraction
            $ result = _return

            if result == "hintKitchen":
                call intHintKitchen from _call_intHintKitchen

            if result == "lightKitchenMain":
                call intNoLights from _call_intNoLights_3

            if result == "openNavMenu":
                call navMenu from _call_navMenu_3

            call displaySceneElements from _call_displaySceneElements_6

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen kitchenInteraction

            if firstS2Kitchen == True:
                $ghostActive = True
                $isTeddyBearMoving = True
                $firstS2Kitchen = False

            $ result = _return

            if result == "hintKitchen":
                call intHintKitchen from _call_intHintKitchen_1

            if result == "takeKitchenKnife":
                call intKitchenKnife from _call_intKitchenKnife

            if result == "takeKitchenSalt":
                call intKitchenSalt from _call_intKitchenSalt

            if result == "lightKitchenMain":
                call intLightKitchenMain from _call_intLightKitchenMain

            if result == "openNavMenu":
                call navMenu from _call_navMenu_4

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_2

            call displaySceneElements from _call_displaySceneElements_7

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen kitchenInteraction

            $ result = _return

            if result == "hintKitchen":
                call intHintKitchen from _call_intHintKitchen_2

            if result == "takeKitchenKnife":
                call intKitchenKnife from _call_intKitchenKnife_1

            if result == "takeKitchenSalt":
                call intKitchenSalt from _call_intKitchenSalt_1

            if result == "lightKitchenMain":
                call intLightKitchenMain from _call_intLightKitchenMain_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_5

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_3

            call displaySceneElements from _call_displaySceneElements_8

    return


################################################################################
# GARAGE #######################################################################
################################################################################
label garage:
    $curRoom = 3
    scene
    call doorOpen from _call_doorOpen_2
    call displayHealth from _call_displayHealth_4
    call checkTurn from _call_checkTurn_2
    call setTeddyLocation from _call_setTeddyLocation_2
    call displaySceneElements from _call_displaySceneElements_9
    call displayHealth from _call_displayHealth_5
    call ghostTurn from _call_ghostTurn_2

    if garageLight == 0:
        show sceneGarage dark
        with fade
    elif garageLight == 1:
        show sceneGarage light
        with fade

    while inRoom == True:
        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:

            if firstGarage == True:
                e "Yes, the generator! Let's fire this baby up."
                $firstGarage = False

            call screen garageInteraction

            $ result = _return

            if result == "hintGarage":
                call intHintGarage from _call_intHintGarage

            if result == "takeFuel":
                call intFuel from _call_intFuel

            if result == "generator" :
                call intGenerator from _call_intGenerator

            if result == "lightGarageMain":
                call intNoLights2 from _call_intNoLights2

            if result == "openNavMenu":
                call navMenu from _call_navMenu_6

            call displaySceneElements from _call_displaySceneElements_10

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen garageInteraction

            $ result = _return

            if result == "hintGarage":
                call intHintGarage from _call_intHintGarage_1

            if result == "takeOil":
                call intOil from _call_intOil

            if result == "takeScrewdriver":
                call intScrewdriver from _call_intScrewdriver

            if result == "takeHammer":
                call intHammer from _call_intHammer

            if result == "takeSaw":
                call intSaw from _call_intSaw

            if result == "takeToolbox":
                call intToolbox from _call_intToolbox

            if result == "openNavMenu":
                call navMenu from _call_navMenu_7

            if result == "lightGarageMain":
                call intLightGarageMain from _call_intLightGarageMain

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_4

            call displaySceneElements from _call_displaySceneElements_11

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen garageInteraction

            $ result = _return

            if result == "hintGarage":
                call intHintGarage from _call_intHintGarage_2

            if result == "takeHammer":
                call intHammer from _call_intHammer_1

            if result == "takeSaw":
                call intSaw from _call_intSaw_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_8

            if result == "lightGarageMain":
                call intLightGarageMain from _call_intLightGarageMain_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_5

            call displaySceneElements from _call_displaySceneElements_12

    return


################################################################################
# BATHROOM #####################################################################
################################################################################
label bathroom:
    $curRoom = 4
    scene
    call doorOpen from _call_doorOpen_3
    call displayHealth from _call_displayHealth_6
    call checkTurn from _call_checkTurn_3
    call setTeddyLocation from _call_setTeddyLocation_3
    call displaySceneElements from _call_displaySceneElements_13
    call displayHealth from _call_displayHealth_7
    call ghostTurn from _call_ghostTurn_3

    if bathroomLamp1 == 0:
        hide bathroomOverlay1
    elif bathroomLamp1 == 1:
        show bathroomOverlay1 zorder 9

    if bathroomLamp2 == 0:
        hide bathroomOverlay2
    elif bathroomLamp2 == 1:
        show bathroomOverlay2 zorder 9

    if bathroomLamp3 == 0:
        hide bathroomOverlay3
    elif bathroomLamp3 == 1:
        show bathroomOverlay3 zorder 9

    if bathroomLight == 0:
        show sceneBathroom dark
        with fade
    elif bathroomLight == 1:
        show sceneBathroom light
        with fade

    while inRoom == True:
        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:

            if firstBathroom == True:
                e "It's so dark!"
                $firstBathroom = False

            call screen bathroomInteraction
            $ result = _return

            if result == "toiletDoor":
                call intToilet from _call_intToilet

            if result == "hintBathroom":
                play sound "audio/tap.mp3"

            if result == "takeBathroomSalt":
                call intBathroomSalt from _call_intBathroomSalt

            if result == "lightBathroomMain":
                call intNoLights from _call_intNoLights_4
            if result == "lightBathroomLamp1":
                call intNoLights from _call_intNoLights_5
            if result == "lightBathroomLamp2":
                call intNoLights from _call_intNoLights_6
            if result == "lightBathroomLamp3":
                call intNoLights from _call_intNoLights_7

            if result == "openNavMenu":
                call navMenu from _call_navMenu_9

            call displaySceneElements from _call_displaySceneElements_14

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen bathroomInteraction
            $ result = _return

            if result == "toiletDoor":
                call intToilet from _call_intToilet_1

            if result == "hintBathroom":
                play sound "audio/tap.mp3"

            if result == "takeBathroomSalt":
                call intBathroomSalt from _call_intBathroomSalt_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_10

            if result == "lightBathroomMain":
                call intLightBathroomMain from _call_intLightBathroomMain

            if result == "lightBathroomLamp1":
                call intLightBathroomLamp1 from _call_intLightBathroomLamp1

            if result == "lightBathroomLamp2":
                call intLightBathroomLamp2 from _call_intLightBathroomLamp2

            if result == "lightBathroomLamp3":
                call intLightBathroomLamp3 from _call_intLightBathroomLamp3

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_6

            call displaySceneElements from _call_displaySceneElements_15

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen bathroomInteraction
            $ result = _return

            if result == "toiletDoor":
                call intToilet from _call_intToilet_2

            if result == "hintBathroom":
                call intHintBathroom from _call_intHintBathroom

            if result == "takeBathroomSalt":
                call intBathroomSalt from _call_intBathroomSalt_2
            if result == "openNavMenu":
                call navMenu from _call_navMenu_11

            if result == "lightBathroomMain":
                call intLightBathroomMain from _call_intLightBathroomMain_1

            if result == "lightBathroomLamp1":
                call intLightBathroomLamp1 from _call_intLightBathroomLamp1_1

            if result == "lightBathroomLamp2":
                call intLightBathroomLamp2 from _call_intLightBathroomLamp2_1

            if result == "lightBathroomLamp3":
                call intLightBathroomLamp3 from _call_intLightBathroomLamp3_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_7

            call displaySceneElements from _call_displaySceneElements_16

    return


################################################################################
# DINING ROOM ##################################################################
################################################################################
label diningRoom:
    $curRoom = 5
    scene
    call doorOpen from _call_doorOpen_4
    call displayHealth from _call_displayHealth_8
    call checkTurn from _call_checkTurn_4
    call setTeddyLocation from _call_setTeddyLocation_4
    call displaySceneElements from _call_displaySceneElements_17
    call displayHealth from _call_displayHealth_9
    call ghostTurn from _call_ghostTurn_4

    if diningRoomLamp1 == 0:
        hide diningRoomOverlay1
    elif diningRoomLamp1 == 1:
        show diningRoomOverlay1 zorder 9

    if diningRoomLight == 0:
        show sceneDiningRoom dark
        with fade
    elif diningRoomLight == 1:
        show sceneDiningRoom light
        with fade

    while inRoom == True:
        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:

            if firstDiningRoom == True:
                e "Maybe an old place like this uses a generator. I should look around."
                $firstDiningRoom = False

            call screen diningRoomInteraction
            $ result = _return

            if result == "hintDiningRoom":
                call intHintDiningRoom from _call_intHintDiningRoom

            if result == "lightDiningRoomMain":
                call intNoLights from _call_intNoLights_8

            if result == "lightDiningRoomLamp1":
                call intNoLights from _call_intNoLights_9

            if result == "openNavMenu":
                call navMenu from _call_navMenu_12

            call displaySceneElements from _call_displaySceneElements_18

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen diningRoomInteraction
            $ result = _return

            if result == "hintDiningRoom":
                call intHintDiningRoom from _call_intHintDiningRoom_1

            if result == "takeCandleStick":
                call intCandleStick from _call_intCandleStick

            if result == "takeSilverKnife":
                call intSilverKnife from _call_intSilverKnife

            if result == "takeDiningRoomSalt":
                call intDiningRoomSalt from _call_intDiningRoomSalt

            if result == "openNavMenu":
                call navMenu from _call_navMenu_13

            if result == "lightDiningRoomMain":
                call intLightDiningRoomMain from _call_intLightDiningRoomMain

            if result == "lightDiningRoomLamp1":
                call intLightDiningRoomLamp1 from _call_intLightDiningRoomLamp1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_8

            call displaySceneElements from _call_displaySceneElements_19

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen diningRoomInteraction
            $ result = _return

            if result == "hintDiningRoom":
                call intHintDiningRoom from _call_intHintDiningRoom_2

            if result == "takeCandleStick":
                call intCandleStick from _call_intCandleStick_1

            if result == "takeSilverKnife":
                call intSilverKnife from _call_intSilverKnife_1

            if result == "takeDiningRoomSalt":
                call intDiningRoomSalt from _call_intDiningRoomSalt_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_14

            if result == "lightDiningRoomMain":
                call intLightDiningRoomMain from _call_intLightDiningRoomMain_1

            if result == "lightDiningRoomLamp1":
                call intLightDiningRoomLamp1 from _call_intLightDiningRoomLamp1_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_9

            call displaySceneElements from _call_displaySceneElements_20

    return


################################################################################
# STUDY ########################################################################
################################################################################
label study:
    $curRoom = 6
    scene
    call doorOpen from _call_doorOpen_5
    call displayHealth from _call_displayHealth_10
    call checkTurn from _call_checkTurn_5
    call setTeddyLocation from _call_setTeddyLocation_5
    call displaySceneElements from _call_displaySceneElements_21
    call displayHealth from _call_displayHealth_11
    call ghostTurn from _call_ghostTurn_5

    if studyLamp1 == 0:
        hide studyOverlay1
    elif studyLamp1 == 1:
        show studyOverlay1 zorder 9

    if studyLight == 0:
        show sceneStudy dark
        with fade
    elif studyLight == 1:
        show sceneStudy light
        with fade

    while inRoom == True:
        # SECTION 1 CONTENTS -------------------------------------------------------
        # No section 1 for study

        # SECTION 2 CONTENTS -------------------------------------------------------
        if curSection == 2:

            if firstStudy == True:
                e "Wick, are you in here?!"
                call intLightStudyMain from _call_intLightStudyMain
                $ renpy.pause(1, hard=True)
                e "Damn, he's not in here. Then there's only one place he can
                be. He's got to be behind that door in the foyer."
                e "But then, why was this door locked? Let's have a look
                around."
                "The hairs on the back of your neck stand up. This room has a
                dark presence. Your gut churns and your pupils dilate. There are
                secrets here."
                $firstStudy = False
                $curSection = 3

            call screen studyInteraction
            $ result = _return

            if result == "openNavMenu":
                call navMenu from _call_navMenu_15

            if result == "takeLetter":
                call intLetter from _call_intLetter

            if result == "takeCheque":
                call intCheque from _call_intCheque

            if result == "takeChloroform":
                call intChloroform from _call_intChloroform

            if result == "viewBook":
                call intBook from _call_intBook

            if result == "viewPhoto":
                call intPhoto from _call_intPhoto

            if result == "lightStudyMain":
                call intLightStudyMain from _call_intLightStudyMain_1

            if result == "lightStudyLamp1":
                call intLightStudyLamp1 from _call_intLightStudyLamp1

            if result == "lightStudyLamp2":
                call intLightStudyLamp2 from _call_intLightStudyLamp2

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_10

            call displaySceneElements from _call_displaySceneElements_22

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen studyInteraction
            $ result = _return

            if result == "openNavMenu":
                call navMenu from _call_navMenu_16

            if result == "takeLetter":
                call intLetter from _call_intLetter_1

            if result == "takeCheque":
                call intCheque from _call_intCheque_1

            if result == "takeChloroform":
                call intChloroform from _call_intChloroform_1

            if result == "viewBook":
                call intBook from _call_intBook_1

            if result == "viewPhoto":
                call intPhoto from _call_intPhoto_1

            if result == "lightStudyMain":
                call intLightStudyMain from _call_intLightStudyMain_2

            if result == "lightStudyLamp1":
                call intLightStudyLamp1 from _call_intLightStudyLamp1_1

            if result == "lightStudyLamp2":
                call intLightStudyLamp2 from _call_intLightStudyLamp2_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_11

            call displaySceneElements from _call_displaySceneElements_23

    return


################################################################################
# CHILD'S ROOM #################################################################
################################################################################
label childsRoom:
    $curRoom = 7
    scene
    call doorOpen from _call_doorOpen_6
    call displayHealth from _call_displayHealth_12
    call checkTurn from _call_checkTurn_6
    call setTeddyLocation from _call_setTeddyLocation_6
    call displaySceneElements from _call_displaySceneElements_24
    call displayHealth from _call_displayHealth_13
    call ghostTurn from _call_ghostTurn_6

    if childsRoomLamp1 == 0:
        hide childsRoomOverlay1
    elif childsRoomLamp1 == 1:
        show childsRoomOverlay1 zorder 9

    if childsRoomLamp2 == 0:
        hide childsRoomOverlay2
    elif childsRoomLamp2 == 1:
        show childsRoomOverlay2 zorder 9

    if childsRoomLight == 0:
        show sceneChildsRoom dark
        with fade
    elif childsRoomLight == 1:
        show sceneChildsRoom light
        with fade

    while inRoom == True:

        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:

            if firstChildsRoom == True:
                e "I really need to get some lights on."
                $firstChildsRoom = False

            call screen childsRoomInteraction
            $ result = _return

            if result == "hintChildsRoom":
                call intHintChildsRoom from _call_intHintChildsRoom

            if result == "lightChildsRoomMain":
                call intNoLights from _call_intNoLights_10
            if result == "lightChildsRoomLamp1":
                call intNoLights from _call_intNoLights_11
            if result == "lightChildsRoomLamp2":
                call intNoLights from _call_intNoLights_12

            if result == "openNavMenu":
                call navMenu from _call_navMenu_17

            call displaySceneElements from _call_displaySceneElements_25

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen childsRoomInteraction
            $ result = _return

            if result == "hintChildsRoom":
                call intHintChildsRoom from _call_intHintChildsRoom_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_18

            if result == "lightChildsRoomMain":
                call intLightChildsRoomMain from _call_intLightChildsRoomMain

            if result == "lightChildsRoomLamp1":
                call intLightChildsRoomLamp1 from _call_intLightChildsRoomLamp1

            if result == "lightChildsRoomLamp2":
                call intLightChildsRoomLamp2 from _call_intLightChildsRoomLamp2

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_12

            call displaySceneElements from _call_displaySceneElements_26

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen childsRoomInteraction
            $ result = _return

            if result == "hintChildsRoom":
                call intHintChildsRoom from _call_intHintChildsRoom_2

            if result == "clueStain":
                call intStain from _call_intStain

            if result == "openNavMenu":
                call navMenu from _call_navMenu_19

            if result == "lightChildsRoomMain":
                call intLightChildsRoomMain from _call_intLightChildsRoomMain_1

            if result == "lightChildsRoomLamp1":
                call intLightChildsRoomLamp1 from _call_intLightChildsRoomLamp1_1

            if result == "lightChildsRoomLamp2":
                call intLightChildsRoomLamp2 from _call_intLightChildsRoomLamp2_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_13

            call displaySceneElements from _call_displaySceneElements_27

    return


################################################################################
# FOYER ########################################################################
################################################################################
label foyer:
    $curRoom = 8
    scene
    call doorOpen from _call_doorOpen_7
    call displayHealth from _call_displayHealth_14
    call checkTurn from _call_checkTurn_7
    call setTeddyLocation from _call_setTeddyLocation_7
    call displaySceneElements from _call_displaySceneElements_28
    call displayHealth from _call_displayHealth_15
    call ghostTurn from _call_ghostTurn_7

    #$curSection = 3
    #$isTrapSet = True
    #$hasBanishingCircle = True
    #$hasConcludedInvestigation = True
    #jump finalConfrontation
    #$studyUnlocked = True
    #$ghostActive = True
    #$isTeddyBearMoving = True

    if foyerLight == 0:
        show sceneFoyer dark
        with fade
    elif foyerLight == 1:
        show sceneFoyer light
        with fade
    elif foyerLight == -1:
        show sceneFoyer darkest
        with fade

    while inRoom == True:

        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:

            # First foyer sequence
            if beginning == True:
                "You enter the house, unfazed by the total darkness. You shout
                out his name at the top of your lungs, but you are met with an
                eerie silence. It finally registers that you can't even see your
                own feet."

                "You pull out your handy iPhone and switch on the flashlight app
                for some illumination."

                show sceneFoyer dark
                $foyerLight = 0

                "You examine your surroundings to discover the interior is as
                rundown as its exterior, and you catch a whiff of the stale
                air."

                "As you turn around, you notice the door is now closed,
                although you are certain you didn't close it, nor did you hear
                it shut. You attempt to open it, only to discover it is now
                locked."

                call playHeartbeats from _call_playHeartbeats

                "Fear starts creeping in again, but you muster your willpower
                to resist it. You decide it doesn't matter, since you will not
                be leaving this house without your dog."

                $renpy.music.set_volume(0.1, 0.0, channel='sound')
                call dogBark2 from _call_dogBark2
                e  "You hear something familiar yet faint in the dark. You spin
                around, “WICK!”"
                $renpy.music.set_volume(1.0, 0.0, channel='sound')

                "Your eyes dart around what appears to be a foyer. Your heart
                is pounding as you take your first step forward into the
                darkness. You need to explore this house. You need to find your
                dog."

                call playMusic from _call_playMusic

                $beginning = False

            call screen foyerInteraction
            $ result = _return
            if result == "basement" :
                call intBasement1 from _call_intBasement1

            # Grandfather clock interaction
            if result == "hintFoyer":
                call intHintFoyer from _call_intHintFoyer

            if result == "lightFoyerMain":
                call intNoLights from _call_intNoLights_13

            if result == "openNavMenu":
                call navMenu from _call_navMenu_20

            call displaySceneElements from _call_displaySceneElements_29


        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen foyerInteraction
            $ result = _return
            if result == "basement" :
                call intBasement1 from _call_intBasement1_1

            # Silver ornament interaction
            if result == "takeSilverOrnament":
                call intSilverOrnament from _call_intSilverOrnament

            # Grandfather clock interaction
            if result == "hintFoyer":
                call intHintFoyer from _call_intHintFoyer_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_21

            if result == "lightFoyerMain":
                call intLightFoyerMain from _call_intLightFoyerMain

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_14

            call displaySceneElements from _call_displaySceneElements_30

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:

            if firstS3Foyer == True:
                call pauseMusic from _call_pauseMusic
                e "It's got to be that door!{w=1.0} {b}WICK ARE YOU IN
                THERE!?{/b}"
                play sound "audio/banging_door.mp3"
                $ renpy.pause(2.5, hard=True)
                call dogBark1 from _call_dogBark1
                $ renpy.pause(1.0, hard=True)
                e "That's him!{fast} Hold on boy, I'm getting you out!"
                e "I've got to open this door, but how? There's no lock. I can't
                even turn the door handle. But if he's in there, there must be
                a way..."
                e "I've got to force that damn spirit to open it. But how...?"
                $ renpy.pause(1.0, hard=True)
                e "Hmmm... It may be a long shot, but I remember my grandma used
                to pour out salt on her window sills. She said it was to ward
                away the evil spirits. I thought she was crazy, but let's pray
                she was onto something."
                e "There's bound to be salt in here. If I can cover the three
                doors in this room, I may be able to trap her. I doubt she'll
                want to leave the house, so she'll have only one place to go..."
                e "But how do I get her in here. Maybe there's something here
                I could use to lure her. What would be precious to her? Perhaps
                something related to her child?"
                $firstS3Foyer = False
                call playMusic from _call_playMusic_1

            if isTrapSet:
                call pauseMusic from _call_pauseMusic_1
                scene black
                with fade
                call doorOpen from _call_doorOpen_8
                $ renpy.pause(1, hard=True)
                e "{alpha=*0.5}Now we wait. Let's hope she takes the bait.{/alpha}"
                $ renpy.pause(4, hard=True)
                play audio "audio/ghost_presence.mp3"
                $ renpy.pause(9, hard=True)
                call intHintFoyer from _call_intHintFoyer_2
                $ renpy.pause(3, hard=True)
                e "{alpha=*0.5}That's our cue, time to lay the last batch of
                salt.{/alpha}"
                e "{alpha=*0.5}Hang on Wick!{/alpha}"
                $curSection = 4
                jump foyer


            call screen foyerInteraction
            $ result = _return
            if result == "basement" :
                call intBasement2 from _call_intBasement2

            if result == "saltDoor1":
                call intSaltDoor1 from _call_intSaltDoor1

            if result == "saltDoor2":
                call intSaltDoor2 from _call_intSaltDoor2

            if result == "setLure":
                e "The trap is set. Now I need to leave and find a place to
                hide."
                $isTrapSet = True

            # Silver ornament interaction
            if result == "takeSilverOrnament":
                call intSilverOrnament from _call_intSilverOrnament_1

            # Grandfather clock interaction
            if result == "hintFoyer":
                call intHintFoyer from _call_intHintFoyer_3

            if result == "openNavMenu":
                call navMenu from _call_navMenu_22

            if result == "lightFoyerMain":
                call intLightFoyerMain from _call_intLightFoyerMain_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_15

            call displaySceneElements from _call_displaySceneElements_31

        # SECTION 4 CONTENTS -------------------------------------------------------
        elif curSection == 4:
            if firstS4Foyer:
                call playHeartbeats from _call_playHeartbeats_1
                "You anxiously survey the room, on guard and anticipating an
                attack at any moment."

                "After what felt like an eternity, you realise the ghost is
                nowhere to be seen. This can only mean one thing..."
                $firstS4Foyer = False

            call screen foyerInteractionEnd
            $ result = _return
            if result == "basement" :
                "You approach the sealed door, certain Wick is beyond this
                point."
                "You extend your arm - your hand shaking uncontrollably.{w=2}
                You quickly grip the door handle to gain composure.{w=2}
                Taking in a deep breath, you turn the handle."
                "{w=2}It turns...{w=1} With your breath still held, you gently
                push."
                call doorOpen from _call_doorOpen_9
                "It opens, at last! You finally let go of your breath as you
                swing the door wide open."
                "As light pierces through the doorway, you discern a set of
                stairs leading down into a wall of darkness."
                "This is it, there's no turning back. You need to decide now how
                to approach this."

                menu:
                    "Fight the ghost":
                        e "Can't wait around here any longer. Need to get Wick, and
                        if she stands in my way, I'll just have to put her down!"
                        e "Hopefully I've got something I can use if it comes to
                        that."
                        $confrontationChoice = 0

                    "Banish the ghost" if hasBanishingCircle:
                        e "Well, it looks like this spell is the most promising
                        option. Time to go home, bitch!"
                        $confrontationChoice = 1

                    "Speak with the ghost" if hasConcludedInvestigation:
                        e "Maybe I'm crazy, but she's a victim in all this too.
                        If possible I'd like to reason with her, and hopefully
                        we can all leave here in peace and not in pieces."
                        $confrontationChoice = 2

                jump finalConfrontation
    return


################################################################################
# LIVING ROOM ##################################################################
################################################################################
label livingRoom:
    $curRoom = 9
    scene
    call doorOpen from _call_doorOpen_10
    call displayHealth from _call_displayHealth_16
    call checkTurn from _call_checkTurn_8
    call setTeddyLocation from _call_setTeddyLocation_8
    call displaySceneElements from _call_displaySceneElements_32
    call displayHealth from _call_displayHealth_17
    call ghostTurn from _call_ghostTurn_8

    if livingRoomLamp1 == 0:
        hide livingRoomOverlay1
    elif livingRoomLamp1 == 1:
        show livingRoomOverlay1 zorder 9

    if hasCanvas:
        if livingRoomLight == 0:
            show sceneLivingRoom darkNoPainting
            with fade
        elif livingRoomLight == 1:
            show sceneLivingRoom lightNoPainting
            with fade
    else:
        if livingRoomLight == 0:
            show sceneLivingRoom dark
            with fade
        elif livingRoomLight == 1:
            show sceneLivingRoom light
            with fade

    while inRoom == True:

        # SECTION 1 CONTENTS -------------------------------------------------------
        if curSection == 1:
            call screen livingRoomInteraction
            $ result = _return

            if result == "hintLivingRoom":
                call intHintLivingRoom from _call_intHintLivingRoom

            if result == "lightLivingRoomMain":
                call intNoLights from _call_intNoLights_14

            if result == "lightLivingRoomLamp1":
                call intNoLights from _call_intNoLights_15

            if result == "openNavMenu":
                call navMenu from _call_navMenu_23

            call displaySceneElements from _call_displaySceneElements_33

        # SECTION 2 CONTENTS -------------------------------------------------------
        elif curSection == 2:
            call screen livingRoomInteraction
            $ result = _return

            if result == "hintLivingRoom":
                call intHintLivingRoom from _call_intHintLivingRoom_1

            if result == "takeSilverLetterOpener":
                call intSilverLetterOpener from _call_intSilverLetterOpener

            if result == "openNavMenu":
                call navMenu from _call_navMenu_24

            if result == "lightLivingRoomMain":
                call intLightLivingRoomMain from _call_intLightLivingRoomMain

            if result == "lightLivingRoomLamp1":
                call intLightLivingRoomLamp1 from _call_intLightLivingRoomLamp1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_16

            call displaySceneElements from _call_displaySceneElements_34

        # SECTION 3 CONTENTS -------------------------------------------------------
        elif curSection == 3:
            call screen livingRoomInteraction
            $ result = _return

            if result == "hintLivingRoom":
                call intHintLivingRoom from _call_intHintLivingRoom_2

            if result == "takeSilverLetterOpener":
                call intSilverLetterOpener from _call_intSilverLetterOpener_1

            if result == "openNavMenu":
                call navMenu from _call_navMenu_25

            if result == "lightLivingRoomMain":
                call intLightLivingRoomMain from _call_intLightLivingRoomMain_1

            if result == "lightLivingRoomLamp1":
                call intLightLivingRoomLamp1 from _call_intLightLivingRoomLamp1_1

            if result == "wanderingTeddyBear":
                call intTeddyBear from _call_intTeddyBear_17

            if result == "takeCanvas":
                call intCanvas from _call_intCanvas

            if result == "takeSoot":
                call intSoot from _call_intSoot

            if result == "makeBanishingCircle":
                call intBanishingCircle from _call_intBanishingCircle
                if debug == True:
                    if hasBanishingCircle:
                        if isBanishingCircleCorrect:
                            "BANISHING CIRCLE MADE CORRECTLY. FLAG SET FOR GOOD ENDING."
                        else:
                            "BANISHING CIRCLE MADE INCORRECTLY."

            call displaySceneElements from _call_displaySceneElements_35

    return


################################################################################
# FINAL CONFRONTATION ##########################################################
################################################################################
label finalConfrontation:
    #$test = renpy.call_stack_depth()
    #"[test]"
    if renpy.call_stack_depth() > 0:
        $ renpy.pop_return()
    $isConfrontingGhost = True
    scene black
    with fade
    play sound "audio/stairs.mp3"
    $ renpy.pause(5, hard=True)
    call pauseMusic from _call_pauseMusic_2
    call playWhispers from _call_playWhispers

    "It's hard to make out anything in here even though your eyes have adjusted
    somewhat in this darkness. One thing is for sure, you can feel the presence
    of evil and hatred growing as you approach."


    if confrontationChoice == 0:

        while inRoom:
            call displayHealth from _call_displayHealth_18

            if ghostHp <= 0:
                call ghostStrike from _call_ghostStrike
                "The ghost emerges with rage.{w=1} She grabs you by the
                throat, ready to thrust her claws."
                "But she pauses.{w=1} Suddenly she releases her grip and
                staggers backwards."
                "She begins to shake violently."
                call ghostShriek from _call_ghostShriek
                with vpunch
                call ghostVanish from _call_ghostVanish
                "Then with a piercing shriek, she disspates into thin air."
                call pauseMusic from _call_pauseMusic_3
                jump endGood

            elif hp <= 0:
                call ghostStrike from _call_ghostStrike_1
                "The ghost emerges with rage.{w=1} She grabs you by the
                throat, ready to thrust her claws."
                call smash from _call_smash
                with hpunch
                call redFlash from _call_redFlash
                $hp = 0
                call displayHealth from _call_displayHealth_19
                "Her claws rip into your chest, as she grins with malice."
                call ghostVanish from _call_ghostVanish_1
                call pauseMusic from _call_pauseMusic_4
                jump endBad

            "Better ready something to use when she makes her move."

            menu:

                "Use a bladed item" if hasSilverKnife or hasKitchenKnife or hasSilverLetterOpener:
                    menu:
                        "Silver knife" if hasSilverKnife:
                            call ghostStrike from _call_ghostStrike_2
                            "The ghost suddenly lunges at you!{fast}{w=1} You
                            manage to evade claws while slashing her torso with
                            the silver knife..."
                            call slash from _call_slash
                            with hpunch
                            call ghostShriek from _call_ghostShriek_1
                            call whiteFlash from _call_whiteFlash
                            "A bright light emanates from her wound as she
                            writhes in pain. You notice the blade has vanished,
                            leaving only its handle."
                            call ghostVanish from _call_ghostVanish_2
                            "The ghost retreats."
                            $ghostHp = ghostHp - 1
                            $hasSilverKnife = False

                        "Kitchen knife" if hasKitchenKnife:
                            call ghostStrike from _call_ghostStrike_3
                            "The ghost appears at a distance.{w=1} Without
                            hesitating, you throw the knife at her..."
                            "The aim is surprisingly good, but it simply passes
                            through her ethereal body and disappears into the
                            shadow."
                            call hit from _call_hit
                            with hpunch
                            call redFlash from _call_redFlash_1
                            "Then in a blink of an eye, she closes in and swipes
                            her claws, smashing into your ribcage."
                            call ghostLaugh from _call_ghostLaugh
                            call ghostVanish from _call_ghostVanish_3
                            e "Ugh, that's not fair."
                            $hp = hp - 1
                            $hasKitchenKnife = False

                        "Silver letter opener" if hasSilverLetterOpener:
                            call ghostStrike from _call_ghostStrike_4
                            "The ghost appears behind you!{fast}{w=1} Before she
                            can strike, you plunge the letter opener into her
                            chest..."
                            call stab from _call_stab
                            with hpunch
                            call ghostShriek from _call_ghostShriek_2
                            call whiteFlash from _call_whiteFlash_1
                            "The impact gives off a bright flash as she shrieks
                            in pain. The letter opener disintegrates before your
                            eyes."
                            call ghostVanish from _call_ghostVanish_4
                            "The ghost retreats."
                            $ghostHp = ghostHp - 1
                            $hasSilverLetterOpener = False

                "Use a tool" if hasSaw or hasScrewdriver or hasHammer:
                    menu:
                        "Saw" if hasSaw:
                            call ghostTaunt from _call_ghostTaunt
                            "The ghost appears before you tauntingly.{fast}{w=2}
                            You slash at her with the saw..."
                            call slash from _call_slash_1
                            "But you hit only air."
                            call hit from _call_hit_1
                            with hpunch
                            call redFlash from _call_redFlash_2
                            "With an evil grin, she slaps you across the face
                            with such force it knocks you down."
                            call ghostLaugh from _call_ghostLaugh_1
                            call ghostVanish from _call_ghostVanish_5
                            $hp = hp - 1
                            "The ghost vanishes."
                            e "A saw... {w=1} What the hell was I thinking?"
                            $hasSaw = False

                        "Screwdriver" if hasScrewdriver:
                            $ renpy.pause(1, hard=True)
                            "You sense the ghost nearby and attempt a surprise
                            attack.{w=2} You lunge with the screwdriver..."
                            call hit from _call_hit_2
                            "But you misstep and fall face forward, losing your
                            grip on the weapon."
                            call ghostTaunt from _call_ghostTaunt_1
                            call slash from _call_slash_2
                            with hpunch
                            call redFlash from _call_redFlash_3
                            "The ghost exploits your blunder and slashes you in
                            the back with her claws."
                            call ghostLaugh from _call_ghostLaugh_2
                            call ghostVanish from _call_ghostVanish_6
                            $hp = hp - 1
                            "The ghost vanishes."
                            e "Damn this darkness!"
                            $hasScrewdriver = False

                        "Hammer" if hasHammer:
                            call ghostStrike from _call_ghostStrike_5
                            "The ghost appears by your side! You swing your
                            hammer..."
                            call slash from _call_slash_3
                            call hit from _call_hit_3
                            "But you only manage to hit the wall, breaking the
                            hammer in the process."
                            call hit from _call_hit_4
                            with hpunch
                            call redFlash from _call_redFlash_4
                            "The ghost grabs you and throws you to the ground."
                            call ghostLaugh from _call_ghostLaugh_3
                            call ghostVanish from _call_ghostVanish_7
                            $hp = hp - 1
                            "The ghost vanishes."
                            e "Knew that damn hammer was going to break!"
                            $hasHammer = False

                "Use an accessory" if hasSilverHairpin or hasSilverOrnament or hasCandleStick:
                    menu:
                        "Silver hairpin" if hasSilverHairpin:
                            call ghostStrike from _call_ghostStrike_6
                            "The ghost suddenly appears and grabs you by the
                            throat!{fast}{w=1} With quick reflexes, you jam the
                            hairpin into her left eye..."
                            call stab from _call_stab_1
                            with hpunch
                            call ghostShriek from _call_ghostShriek_3
                            call whiteFlash from _call_whiteFlash_2
                            "Light flares out from her wounded eye as she
                            screeches and looses her grip on you."
                            call ghostVanish from _call_ghostVanish_8
                            "The ghost retreats."
                            $ghostHp = ghostHp - 1
                            $hasSilverHairpin = False

                        "Silver ornament" if hasSilverOrnament:
                            $ renpy.pause(1, hard=True)
                            "You sense the ghost encroaching from a distance.
                            {fast}{w=1} You quickly throw the ornament in her
                            direction..."
                            call burst from _call_burst
                            show ghost anim
                            with hpunch
                            call ghostShriek from _call_ghostShriek_4
                            call whiteFlash from _call_whiteFlash_3
                            "Suddenly, an explosion of light, followed by a
                            hideous scream."
                            call ghostVanish from _call_ghostVanish_9
                            "The ghost retreats."
                            $ghostHp = ghostHp - 1
                            $hasSilverOrnament = False

                        "Candlestick" if hasCandleStick:
                            call ghostStrike from _call_ghostStrike_7
                            "The launches a surprise attack at you!{w=1} You
                            barely manage to raise the candlestick in defence..."
                            call hit from _call_hit_5
                            with hpunch
                            call redFlash from _call_redFlash_5
                            "But to no avail. The sheer force of her strike
                            breaks it apart and hurls you across the room."
                            call ghostLaugh from _call_ghostLaugh_4
                            call ghostVanish from _call_ghostVanish_10
                            e "Candlestick...{w=1} Seemed like a good idea at
                            the time..."
                            $hp = hp - 1
                            $hasCandleStick = False

                "Defend yourself":
                    call ghostStrike from _call_ghostStrike_8
                    "The ghost rushes at you!{fast}{w=1} You take up a
                    defensive stance."
                    call hit from _call_hit_6
                    with hpunch
                    call redFlash from _call_redFlash_6
                    "But you are no match for her brute
                    strength, and you are thrown to the floor."
                    call ghostLaugh from _call_ghostLaugh_5
                    call ghostVanish from _call_ghostVanish_11
                    $hp = hp - 1
                    "The ghost vanishes."



    elif confrontationChoice == 1:
        call displayHealth from _call_displayHealth_20

        "You pull out the canvas with the banishing circle and gently stretch it
        out at your feet.{w=2} You take a step into where the circle was drawn.
        You clench your fist tightly to summon up your courage."

        e "{b}I'M HERE!!!{w=1} COME AND GET ME YOU CRAZY BITCH!{w=2}
        I DARE YOU!{/b}"

        "After a moment of eerie silence, the room begins to shake."
        with hpunch

        call ghostStrike from _call_ghostStrike_9
        "She appears before you, more hateful than ever, and bellowing with
        fury."

        e "You are one ugly mother..."

        "Before you can finish your statement, she charges at you with
        unbelievable speed!{fast}{w=2} But you hold your ground. The timing has
        to be perfect."

        "She lunges head-on with outstretched claws.{w=2} Just as she is about
        to connect with your throat, you launch yourself backwards."

        call hit from _call_hit_7
        with hpunch
        "But with her immense speed she catches you mid-air..."

        if isBanishingCircleCorrect:
            "It's too late...{w=3} for her.{w=1} She stepped into the circle,
            springing the trap."

            call redFlash from _call_redFlash_7
            call vortexOpen from _call_vortexOpen
            "Suddenly a fiery red vortex envelops the circle, pulling her in,
            feet first."

            call scratch from _call_scratch
            "She tries desperately to hold on, savagely clawing at the floor.
            {w=2} But it's futile. Even with her strength, the power of the
            circle is too compelling to put up much of a resistance."

            call redFlash from _call_redFlash_8
            call ghostShriek from _call_ghostShriek_5
            with vpunch
            "She lets out a final cry before being completely swallowed up by
            the vortex."

            call vortexClose from _call_vortexClose
            call redFlash from _call_redFlash_9
            call ghostVanish from _call_ghostVanish_12
            "After a brief moment, the vortex closes and disappears,
            along with all presence of evil and hatred."
            call pauseMusic from _call_pauseMusic_5
            jump endGood

        else:
            "It's too late...{w=3} for you.{w=1} The circle does nothing, and
            you are now perilously in her grip."

            call ghostLaugh2 from _call_ghostLaugh2
            "She stares down at you, her eyes glowing with malevolence."

            call smash from _call_smash_1
            with hpunch
            call redFlash from _call_redFlash_10
            $hp = 0
            call displayHealth from _call_displayHealth_21
            call ghostLaugh from _call_ghostLaugh_6
            "Then with a sinister grin, she thrusts her wicked claws into your
            chest."

            call ghostVanish from _call_ghostVanish_13
            call pauseMusic from _call_pauseMusic_6
            jump endBad

    elif confrontationChoice == 2:
        call displayHealth from _call_displayHealth_22

        "You attempt to motion a gesture of peace, with hands raised, as you
        approach. You are uncertain a ghost can recognise gestures, but you need
        to try. After all, you want to reason with her."

        "With great trembling and beads of sweat running down your face, you
        find yourself searching for your voice."

        e "Uh...{w=1} I....{w=1} I just want to talk for a moment.{w=2} I know
        what happened in this house.{w=2} I also know that it wasn't your fault.
        It was your husband...{w=2} and I have proof."

        call ghostTaunt from _call_ghostTaunt_2
        "You turn around, and there she is, standing right in front of you.
        She's menacing, but you have her attention."

        jump endBest

################################################################################
# ENDINGS ######################################################################
################################################################################
# BAD ENDING
label endBad :
    if renpy.call_stack_depth() > 0:
        $ renpy.pop_return()
    scene black
    with fade

    "Your health has depleted.{w=1.5}
    \nYou gasp your last breath.{w=1.5}
    \nEverything is fading to black..."
    e "I'm sorry,{w=1} Wick..."

    # To be developed further
    #$ renpy.quit()
    #$ renpy.call_stack_depth()
    return


# GOOD ENDING
label endGood:
    scene black
    with fade
    scene lookingathands
    with fade
    call playHeartbeats from _call_playHeartbeats_2
    "You did it.{w=1} You actually did it.{w=1} You defeated the ghost.{w=1} You
    drop to your knees. Your heart is racing and you realise you're shaking all
    over. It takes all your strength and focus to pull yourself together and
    restore a semblance of composure."

    call dogLick from _call_dogLick
    "But you remain stunned... And then something licks your face. It draws you
    out of your state of shock. Wick is staring into your eyes, his tongue
    hanging to the side as he pants and licks you again."

    call dogPanting from _call_dogPanting
    call pauseMusic from _call_pauseMusic_7
    scene wickbasement
    with dissolve
    e "{b}WICK!{fast}{/b}"

    call dogBark2 from _call_dogBark2_1
    queue sound "audio/panting.mp3"
    "You take the dog into your arms and your shaking subsides. It's over. You
    did it. You got your best friend back. Now...{w=1} {b}GET THE HELL OUT OF
    THERE!{/b}"

    stop sound
    scene black
    with dissolve
    return


# BEST ENDING
label endBest:
    "The ghost’s piercing gaze moves from yours to the items in your hand."

    "For a moment, nothing happens.{w=2} You stand there silent and trembling."

    call pauseMusic from _call_pauseMusic_8
    call ghostScream from _call_ghostScream_1
    $ renpy.pause(0.5, hard=True)
    with vpunch
    scene white
    with dissolve

    "And then... it screams!{fast} You’ve never heard such a scream. It’s laced
    with such rage that you drop the items, shield your ears and clench your
    eyes shut."

    scene black
    show ghostholdingbaby anim
    with dissolve

    "As you reopen your eyes, you see it staring at you.{w=2} You see HER
    staring at you.{w=2} The apparition is kneeling on the floor, holding the
    teddy bear to her arms. But it’s not a teddy bear. It’s, it’s a child."

    "She looks down and strokes her little cheek. She’s smiling. They both are.
    She returns to meet your gaze and bows her head in appreciation."

    "Then her eyes widen and her grin extends. But this smile unsettles you.
    She points to the returning address on the mistress’ letter. To where her
    husband currently resides with his new lover."

    call ghostLaugh from _call_ghostLaugh_7
    scene black
    with fade
    "She lets out a cackle before fading to a mist and dissipating."

    scene lookingathands
    with fade
    call playHeartbeats from _call_playHeartbeats_3
    "You drop to your knees. Your heart is racing and you realise you're shaking
    all over. It takes all your strength and focus to pull yourself together and
    restore a semblance of composure."

    call dogLick from _call_dogLick_1
    "But you remain stunned... And then something licks your face. It draws you
    out of your state of shock. Wick is staring into your eyes, his tongue
    hanging to the side as he pants and licks you again."

    call dogPanting from _call_dogPanting_1
    call pauseMusic from _call_pauseMusic_9
    scene wickbasement
    with dissolve
    e "{b}WICK!{fast}{/b}"

    call dogBark2 from _call_dogBark2_2
    queue sound "audio/panting.mp3"
    "You take the dog into your arms and your shaking subsides. It's over. You
    did it. You got your best friend back. Now...{w=1} {b}GET THE HELL OUT OF
    THERE!{/b}"

    stop sound
    scene black
    with dissolve
    return



# FUNCTIONS

label ghostTurn:
    # Only trigger if ghost is meant to be active
    if ghostActive == False:
        return

    $ghostOldLocation = curGhostRoom

    $ ghostRandRoll = 0
    while ghostRandRoll == 0:
        $ ghostRandRoll = renpy.random.randint(1,9)

        # Ghost turn must not generate same room number as current room
        if ghostRandRoll == curRoom:
            # If there is a match, reroll
            $ ghostRandRoll = 0
        elif ghostRandRoll == curGhostRoom:
            # Ghost cannot haunt same room 2 turns in a row
            $ ghostRandRoll = 0
        elif curSection == 2 and curRoom == 3 and ghostRandRoll == 6:
            # Prevent ghost from haunting user first time into study
            $ ghostRandRoll = 0
        elif curSection == 2 and curRoom == 5 and ghostRandRoll == 6:
            # Prevent ghost from haunting user first time into study
            $ ghostRandRoll = 0
        elif curSection == 2 and curRoom == 9 and ghostRandRoll == 6:
            # Prevent ghost from haunting user first time into study
            $ ghostRandRoll = 0

    $ curGhostRoom = ghostRandRoll
    #"[ghostRandRoll]"

    # For testing teddy bear pop up
    #$isTeddyBearMoving = True
    #$teddyBearLocation = curRoom

    if curGhostRoom == 1:
        play sound "audio/music_box.mp3"
        $masterBedroomLight = 0
        $masterBedroomLamp1 = 0
        $masterBedroomLamp2 = 0
    elif curGhostRoom == 2:
        play sound "audio/utensils.mp3"
        $kitchenLight = 0
    elif curGhostRoom == 3:
        play sound "audio/radio.mp3"
        $garageLight = 0
    elif curGhostRoom == 4:
        play sound "audio/tap.mp3"
        $bathroomLight = 0
        $bathroomLamp1 = 0
        $bathroomLamp2 = 0
        $bathroomLamp3 = 0
    elif curGhostRoom == 5:
        play sound "audio/glasses.mp3"
        $diningRoomLight = 0
        $diningRoomLamp1 = 0
    elif curGhostRoom == 6:
        $studyLight = 0
        $studyLamp1 = 0
        $studyLamp2 = 0
    elif curGhostRoom == 7:
        play sound "audio/toy_squeak.mp3"
        $childsRoomLight = 0
        $childsRoomLamp1 = 0
        $childsRoomLamp2 = 0
    elif curGhostRoom == 8:
        play sound "audio/chime.mp3"
        $foyerLight = 0
    elif curGhostRoom == 9:
        play sound "audio/whistling_wind.mp3"
        $livingRoomLight = 0
        $livinglamp1 = 0

    return

label displayHealth:

    if hp == 0:
        show screen healthBar0
        hide screen healthBar1
        hide screen healthBar2
        hide screen healthBar3
        if isConfrontingGhost == False:
            $ renpy.pop_return()
            jump endBad
    elif hp == 1:
        show screen healthBar1
        hide screen healthBar0
        hide screen healthBar2
        hide screen healthBar3
    elif hp == 2:
        show screen healthBar2
        hide screen healthBar1
        hide screen healthBar0
        hide screen healthBar3
    elif hp == 3:
        show screen healthBar3
        hide screen healthBar1
        hide screen healthBar2
        hide screen healthBar0

    return

label checkTurn:

    # Only trigger if ghost is meant to be active
    if ghostActive == False:
        return

    if curRoom == curGhostRoom:
        call ghostAttackSequence from _call_ghostAttackSequence

    return

label ghostAttackSequence:
    scene black
    with fade

    $ renpy.pause(0.5, hard=True)

    call ghostScream from _call_ghostScream_2

    $ renpy.pause(0.5, hard=True)

    show ghost anim
    with vpunch

    $ renpy.pause(2, hard=True)
    $ renpy.pause(8)


    hide ghost anim
    with dissolve

    $hp = hp - 1

    if isFirstEncounter == True and hp > 0:
        call firstEncounter from _call_firstEncounter

    return


label firstEncounter:
    e "{b}WHAT was that!?{/b}{fast}{w=2} That hurt like hell, but it seems that
    \"thing\" didn't get away unscathed either!"
    "You cup your hand around your neck and grab the remains of your now
    disintegrated silver necklace."
    e "It seems you don't like the taste of silver,{w=1.0} interesting..."

    $isFirstEncounter = False
    #$ renpy.pop_return()
    return

label navMenu:
    if curRoom == 1:
        menu:
            "Go to kitchen":
                $ renpy.pop_return()
                jump kitchen

            "Go to bathroom":
                $ renpy.pop_return()
                jump bathroom

            "Stay":
                return
    elif curRoom == 2:
        # From kitchen
        menu:
            "Go to master bedroom":
                $ renpy.pop_return()
                jump masterBedroom

            "Go to garage":
                $ renpy.pop_return()
                jump garage

            "Go to dining room":
                $ renpy.pop_return()
                jump diningRoom

            "Stay":
                return
    elif curRoom == 3:
        # From garage
        menu:
            "Go to kitchen":
                $ renpy.pop_return()
                jump kitchen

            "Go to study":
                if studyUnlocked == True:
                    if firstStudy == True:
                        e "Let's quickly unlock this. Please be behind this
                        door, Wick..."
                    play sound "audio/unlock.mp3"
                    $ renpy.pause(1, hard=True)
                    $ renpy.pop_return()
                    jump study
                else:
                    play sound "audio/locked.mp3"
                    "This room is locked."
                    if curSection == 2:
                        e "Could Wick be in there? I need to find a key to this
                        damn door."
                    return

            "Stay":
                return
    elif curRoom == 4:
        # From bathroom
        menu:
            "Go to master bedroom":
                $ renpy.pop_return()
                jump masterBedroom

            "Go to dining room":
                $ renpy.pop_return()
                jump diningRoom

            "Go to child's room":
                $ renpy.pop_return()
                jump childsRoom

            "Stay":
                return
    elif curRoom == 5:
        # From dining room
        menu:
            "Go to kitchen":
                $ renpy.pop_return()
                jump kitchen

            "Go to bathroom":
                $ renpy.pop_return()
                jump bathroom

            "Go to study":
                if studyUnlocked == True:
                    if firstStudy == True:
                        e "Let's quickly unlock this. Please be behind this
                        door, Wick..."
                    play sound "audio/unlock.mp3"
                    $ renpy.pause(1, hard=True)
                    $ renpy.pop_return()
                    jump study
                else:
                    play sound "audio/locked.mp3"
                    "This room is locked."
                    if curSection == 2:
                        e "Could Wick be in there? I need to find a key to this
                        damn door."
                    return

            "Go to foyer":
                $ renpy.pop_return()
                jump foyer

            "Stay":
                return
    elif curRoom == 6:
        # From study
        menu:
            "Go to garage":
                $ renpy.pop_return()
                jump garage

            "Go to dining room":
                $ renpy.pop_return()
                jump diningRoom

            "Go to living room":
                $ renpy.pop_return()
                jump livingRoom

            "Stay":
                return
    elif curRoom == 7:
        # From child's room
        menu:
            "Go to bathroom":
                $ renpy.pop_return()
                jump bathroom

            "Go to foyer":
                $ renpy.pop_return()
                jump foyer

            "Stay":
                return
    elif curRoom == 8:
        # From foyer
        menu:
            "Go to child's room":
                $ renpy.pop_return()
                jump childsRoom

            "Go to dining room":
                $ renpy.pop_return()
                jump diningRoom

            "Go to living room":
                $ renpy.pop_return()
                jump livingRoom

            "Stay":
                return
    elif curRoom == 9:
        # From living room
        menu:
            "Go to study":
                if studyUnlocked == True:
                    if firstStudy == True:
                        e "Let's quickly unlock this. Please be behind this
                        door, Wick..."
                    play sound "audio/unlock.mp3"
                    $ renpy.pause(1, hard=True)
                    $ renpy.pop_return()
                    jump study
                else:
                    play sound "audio/locked.mp3"
                    "This room is locked."
                    if curSection == 2:
                        e "Could Wick be in there? I need to find a key to this
                        damn door."
                    return

            "Go to foyer":
                $ renpy.pop_return()
                jump foyer

            "Stay":
                return

    return


label toolboxMenu:
    menu:
        "Use hammer" if hasHammer:
            "You use the hammer to bash it open, but you only manage to dent it
            out of shape."
            e "Damn it! This is useless. Need to try something else."

        "Use screwdriver" if hasScrewdriver:
            if hasBeenOiled == True:
                "The screws yield to the twist of the screwdriver."
                e "Yes, it worked!"
                "You manage to disassemble the toolbox to discover its only
                content is a key."
                e "This has got to be the key for that locked door!"
                $hasToolbox = True
                "You take the key."
                hide garagetoolbox
                $studyUnlocked = True
            else:
                "You try to twist the screws out, but it won't budge. If only
                there was a way to lubricate it."

        "Use oil" if hasOil and hasBeenOiled == False:
            "You tip the can of oil over the toolbox. A gush of oil flows out,
            drenching the entire toolbox."
            "It's too difficult to grip the toolbox to pry it open, but perhaps
            it can be dismantled."
            $hasBeenOiled = True

        "Cancel":
            return

    return

label displaySceneElements:

    # Master Bedroom Elements
    if curRoom == 1:

        if isTeddyBearMoving == True and teddyBearLocation == 1:
            if masterBedroomLight <= 0:
                show teddyBear dark at teddyMasterBedroomPos zorder 20
            else:
                show teddyBear light at teddyMasterBedroomPos zorder 20
        else:
            hide teddyBear


    # Kitchen Elements
    elif curRoom == 2:

        if isTeddyBearMoving == True and teddyBearLocation == 2:
            if kitchenLight <= 0:
                show teddyBear dark at teddyKitchenPos zorder 20
            else:
                show teddyBear light at teddyKitchenPos zorder 20
        else:
            hide teddyBear


        if hasKitchenKnife == False:
            if kitchenLight <= 0:
                show kitchenKnife dark at kitchenKnifePos zorder 20
            else:
                show kitchenKnife light at kitchenKnifePos zorder 20
        else:
            hide kitchenKnife

        if hasKitchenSalt == False:
            if kitchenLight <= 0:
                show kitchenSalt dark at kitchenSaltPos zorder 20
            else:
                show kitchenSalt light at kitchenSaltPos zorder 20
        else:
            hide kitchenSalt

    # Garage Elements
    elif curRoom == 3:

        if isTeddyBearMoving == True and teddyBearLocation == 3:
            if garageLight <= 0:
                show teddyBear dark at teddyGaragePos zorder 20
            else:
                show teddyBear light at teddyGaragePos zorder 20
        else:
            hide teddyBear

        if hasFuel == False:
            show fuel at fuelPos zorder 20
        else:
            hide fuel

        if hasOil == False:
            if garageLight <= 0:
                show oil dark at oilPos zorder 20
            else:
                show oil light at oilPos zorder 20
        else:
            hide oil

        if hasScrewdriver == False:
            if garageLight <= 0:
                show screwdriver dark at screwdriverPos zorder 20
            else:
                show screwdriver light at screwdriverPos zorder 20
        else:
            hide screwdriver

        if hasHammer == False:
            if garageLight <= 0:
                show hammer dark at hammerPos zorder 20
            else:
                show hammer light at hammerPos zorder 20
        else:
            hide hammer

        if hasSaw == False:
            if garageLight <= 0:
                show saw dark at sawPos zorder 20
            else:
                show saw light at sawPos zorder 20
        else:
            hide saw

        if hasToolbox == False:
            if garageLight <= 0:
                show toolbox dark at toolboxPos zorder 20
            else:
                show toolbox light at toolboxPos zorder 20
        else:
            hide toolbox

    # Bathroom Elements
    elif curRoom == 4:

        if isTeddyBearMoving == True and teddyBearLocation == 4:
            if bathroomLight <= 0:
                show teddyBear dark at teddyBathroomPos zorder 20
            else:
                show teddyBear light at teddyBathroomPos zorder 20
        else:
            hide teddyBear

    # Dining Room Elements
    elif curRoom == 5:

        if isTeddyBearMoving == True and teddyBearLocation == 5:
            if diningRoomLight <= 0:
                show teddyBear dark at teddyDiningRoomPos zorder 20
            else:
                show teddyBear light at teddyDiningRoomPos zorder 20
        else:
            hide teddyBear

        if hasCandleStick == False:
            if diningRoomLight <= 0:
                show candleStick dark at candleStickPos zorder 20
            else:
                show candleStick light at candleStickPos zorder 20
        else:
            hide candleStick

        if hasSilverKnife == False:
            if diningRoomLight <= 0:
                show silverKnife dark at silverKnifePos zorder 20
            else:
                show silverKnife light at silverKnifePos zorder 20
        else:
            hide silverKnife

        if hasDiningRoomSalt == False:
            if diningRoomLamp1 <= 0:
                show diningRoomSalt dark at diningRoomSaltPos zorder 20
            else:
                show diningRoomSalt light at diningRoomSaltPos zorder 20
        else:
            hide diningRoomSalt

    # Study Elements
    elif curRoom == 6:

        if isTeddyBearMoving == True and teddyBearLocation == 6:
            if studyLight <= 0:
                show teddyBear dark at teddyStudyPos zorder 20
            else:
                show teddyBear light at teddyStudyPos zorder 20
        else:
            hide teddyBear

        if studyLight <= 0:
            show photo dark at photoPos zorder 20
        else:
            show photo light at photoPos zorder 20


        if hasLetter == False:
            if studyLight <= 0:
                show letter dark at letterPos zorder 20
            else:
                show letter light at letterPos zorder 20
        else:
            hide letter

    # Child's Room Elements
    elif curRoom == 7:
        if isTeddyBearMoving == True and teddyBearLocation == 7:
            if childsRoomLight <= 0:
                show teddyBear dark at teddyChildsRoomPos zorder 20
            else:
                show teddyBear light at teddyChildsRoomPos zorder 20
        else:
            hide teddyBear


    # Foyer Elements
    elif curRoom == 8:

        if isTeddyBearMoving == True and teddyBearLocation == 8:
            if foyerLight <= 0:
                show teddyBear dark at teddyFoyerPos zorder 20
            else:
                show teddyBear light at teddyFoyerPos zorder 20
        else:
            hide teddyBear

        if hasSilverOrnament == False:
            if foyerLight <= 0:
                show silverOrnament dark at silverOrnamentPos zorder 20
            else:
                show silverOrnament light at silverOrnamentPos zorder 20
        else:
            hide silverOrnament

    # Living Room Elements
    elif curRoom == 9:

        if isTeddyBearMoving == True and teddyBearLocation == 9:
            if livingRoomLight <= 0:
                show teddyBear dark at teddyLivingRoomPos zorder 20
            else:
                show teddyBear light at teddyLivingRoomPos zorder 20
        else:
            hide teddyBear

        if hasSilverLetterOpener == False:
            if foyerLight <= 0:
                show silverLetterOpener dark at silverLetterOpenerPos zorder 20
            else:
                show silverLetterOpener light at silverLetterOpenerPos zorder 20
        else:
            hide silverLetterOpener

    return


# ITEM INTERACTION EVENTS ######################################################

# MASTER BEDROOM ITEMS #
label intHintMasterBedroom:
    play sound "audio/music_box.mp3"
    return

label intSilverHairpin:
    show masterhairpin at truecenter zorder 30
    $hasSilverHairpin = True
    "You open the drawer to discover a silver hairpin."
    "You take the silver hairpin."
    hide masterhairpin
    return

label intDiary:
    show masterbedroomdiary at truecenter zorder 30
    "It appears to be a diary. You flip it open and begin skimming through
    entries."
    "{i}I cannot go on. I have lost the love of my life; my precious daughter,
    Rose. How could this happen? I put little Rose down for her sleep and ran a
    warm bath for myself. John had again closed himself off in his study.{/i}"
    "{i}I was, however, used to his absence as there are many times he needed to
    travel for work. I am grateful for his financial support, and what I don’t
    receive from him emotionally, I get from Rose.{/i}"
    "{i}I had cut the water and slipped into the tub. The house was silent.
    It remained like this for a long while. It began to unsettle me and I
    decided to check on Rose. I drained the bath, wrapped a towel around myself
    and stepped into her room{/i}."
    "{i}At first I thought she was still sleeping but then I noticed that she
    was a pale shade of blue. I went dizzy. My baby had suffocated in her crib.
    I collapsed on the floor.{/i}"
    "{i}The community have shunned me. Spat at me. Exiled me. I have been
    labelled a unfit mother and an abomination from my own husband. I have
    nothing. I am nothing. My soul is broken.{/i}"
    "{i}Tonight I will be returning to the bath. I will be resting with you
    soon, my love. {/i}"
    e "This is horrible. Could this be why this place is haunted?"
    $hasViewedDiary = True
    hide masterbedroomdiary
    return

label intLightMasterBedroomMain:
    if masterBedroomLight == 0:
        call switchLight from _call_switchLight_1
        $masterBedroomLight = 1
        show sceneMasterBedroom light
    else:
        call switchLight from _call_switchLight_2
        $masterBedroomLight = 0
        show sceneMasterBedroom dark
    return

label intLightMasterBedroomLamp1:
    if masterBedroomLamp1 == 0:
        call switchLight from _call_switchLight_3
        $masterBedroomLamp1 = 1
        show masterBedroomOverlay1 zorder 9
    else:
        call switchLight from _call_switchLight_4
        $masterBedroomLamp1 = 0
        hide masterBedroomOverlay1
    return

label intLightMasterBedroomLamp2:
    if masterBedroomLamp2 == 0:
        call switchLight from _call_switchLight_5
        $masterBedroomLamp2 = 1
        show masterBedroomOverlay2 zorder 9
    else:
        call switchLight from _call_switchLight_6
        $masterBedroomLamp2 = 0
        hide masterBedroomOverlay2
    return

# KITCHEN ITEMS #
label intHintKitchen:
    play sound "audio/utensils.mp3"
    return

label intKitchenKnife:
    show kitchenknife at truecenter zorder 30
    $hasKitchenKnife = True
    "It's an old chef's knife. The blade is rather dull."
    "You take the kitchen knife."
    hide kitchenknife
    return

label intKitchenSalt:
    show salt at truecenter zorder 30
    $hasKitchenSalt = True
    "It's a bottle of salt."
    "You take the salt."
    hide salt
    $saltCount += 1
    return

label intLightKitchenMain:
    if kitchenLight == 0:
        call switchLight from _call_switchLight_7
        $kitchenLight = 1
        show sceneKitchen light
    else:
        call switchLight from _call_switchLight_8
        $kitchenLight = 0
        show sceneKitchen dark
    return

# GARAGE ITEMS #
label intHintGarage:
    play sound "audio/radio.mp3"
    return

label intFuel:
    show garagefuel at truecenter zorder 30
    $hasFuel = True
    "You take the fuel."
    e "The fuel! Alright. I just need to drag this heavy bastard to the
    generator now. This better work."
    hide garagefuel
    return

label intGenerator:
    if hasFuel == True:
        # Play sound
        play sound "audio/pouring.mp3"
        "You dump the fuel into the generator. You yank the recoil cord."
        play sound "audio/generator_start.mp3"
        $ renpy.pause(2, hard=True)
        with hpunch
        "The generator begins to shake."
        $ renpy.pause(2)
        e "Yes! Wick, I'm coming for you, boy. With some lights on, this house
        won't be so damn creepy."

        $ renpy.pause(1, hard=True)
        # Turn on Light
        call switchLight from _call_switchLight_9
        $garageLight = 1
        show sceneGarage light
        call displaySceneElements from _call_displaySceneElements_36

        e "Finally, some lights!"
        $ renpy.pause(1, hard=True)
        play sound "audio/toy_squeak.mp3"
        $ renpy.pause(0.5, hard=True)
        e "What was that?!{fast} Was that a toy squeak? Could it be Wick?! I
        need to go check."

        $firstPoweredKitchen = True
        jump kitchen
    else:
        "You yank the recoil cord several times, but nothing happens."
        e "Come on! Work damn it!"
        e "Sigh, it needs some juice. Surely the fuel would be around here
        somewhere."
    return

label intOil:
    show garageoil at truecenter zorder 30
    $hasOil = True
    "You see an oil can. It's giving off a strong odor."
    "You take the oil."
    hide garageoil
    return

label intScrewdriver:
    show garagescrewdriver at truecenter zorder 30
    $hasScrewdriver = True
    "You see a Phillips head screwdriver. It's in surprisingly good
    condition."
    "You take the screwdriver."
    hide garagescrewdriver
    return

label intHammer:
    show garagehammer at truecenter zorder 30
    $hasHammer = True
    "You see a rusted hammer. The wood has rotted and the head is
    loose. Clearly not suitable for any heavy duty work."
    "You take the hammer."
    hide garagehammer
    return

label intSaw:
    show garagesaw at truecenter zorder 30
    $hasSaw = True
    "You see a rusty saw. Given its condition, it probably wouldn't
    cut through much."
    "You take the saw."
    hide garagesaw
    return

label intToolbox:
    show garagetoolbox at truecenter zorder 30
    "It's an old rusty toolbox. There's something rattling
    inside."

    if hasHammer == True or hasScrewdriver == True or hasOil == True:
        call toolboxMenu from _call_toolboxMenu
    else:
        "You muster all your strength to open the toolbox, but it
        is jammed tight."
        e "There maybe something around here I can use to get it
        open."

    hide garagetoolbox
    return

label intLightGarageMain:
    if garageLight == 0:
        call switchLight from _call_switchLight_10
        $garageLight = 1
        show sceneGarage light
    else:
        call switchLight from _call_switchLight_11
        $garageLight = 0
        show sceneGarage dark
    return

# BATHROOM ITEMS #
label intHintBathroom:
    play sound "audio/tap.mp3"
    return

label intToilet:
    e "Judging by the smell this must be the toilet. Let's leave this closed."
    return

label intBathroomSalt:
    show salt at truecenter zorder 30
    $hasBathroomSalt = True
    "You open the bathroom sink cabinet to discover salt."
    "You take the salt."
    hide salt
    $saltCount += 1
    return

label intLightBathroomMain:
    if bathroomLight == 0:
        call switchLight from _call_switchLight_12
        $bathroomLight = 1
        show sceneBathroom light
    else:
        call switchLight from _call_switchLight_13
        $bathroomLight = 0
        show sceneBathroom dark
    return

label intLightBathroomLamp1:
    if bathroomLamp1 == 0:
        call switchLight from _call_switchLight_14
        $bathroomLamp1 = 1
        show bathroomOverlay1 zorder 9
    else:
        call switchLight from _call_switchLight_15
        $bathroomLamp1 = 0
        hide bathroomOverlay1
    return

label intLightBathroomLamp2:
    if bathroomLamp2 == 0:
        call switchLight from _call_switchLight_16
        $bathroomLamp2 = 1
        show bathroomOverlay2 zorder 9
    else:
        call switchLight from _call_switchLight_17
        $bathroomLamp2 = 0
        hide bathroomOverlay2
    return

label intLightBathroomLamp3:
    if bathroomLamp3 == 0:
        call switchLight from _call_switchLight_18
        $bathroomLamp3 = 1
        show bathroomOverlay3 zorder 9
    else:
        call switchLight from _call_switchLight_19
        $bathroomLamp3 = 0
        hide bathroomOverlay3
    return

# DINING ROOM ITEMS #
label intHintDiningRoom:
    play sound "audio/glasses.mp3"
    return

label intCandleStick:
    show diningcandlestick at truecenter zorder 30
    $hasCandleStick = True
    "You take the candlestick."
    hide diningcandlestick
    return

label intSilverKnife:
    show diningknife at truecenter zorder 30
    $hasSilverKnife = True
    "You take the silver knife."
    hide diningknife
    return

label intDiningRoomSalt:
    show salt at truecenter zorder 30
    $hasDiningRoomSalt = True
    "You take the salt."
    hide salt
    $saltCount += 1
    return

label intLightDiningRoomMain:
    if diningRoomLight == 0:
        call switchLight from _call_switchLight_20
        $diningRoomLight = 1
        show sceneDiningRoom light
    else:
        call switchLight from _call_switchLight_21
        $diningRoomLight = 0
        show sceneDiningRoom dark
    return

label intLightDiningRoomLamp1:
    if diningRoomLamp1 == 0:
        call switchLight from _call_switchLight_22
        $diningRoomLamp1 = 1
        show diningRoomOverlay1 zorder 9
    else:
        call switchLight from _call_switchLight_23
        $diningRoomLamp1 = 0
        hide diningRoomOverlay1
    return

# STUDY ITEMS #
label intLetter:
    show studyletter at truecenter zorder 30
    "It appears to be a letter."
    "{i}My darling John,\n
    I hate these long nights alone without you.\n
    You must see me again. Live with me. Be with me.\n
    You don’t love her. You don’t love either of them.{/i}"
    "{i}That pathetic woman you call a wife has burdened you with a first born
    not worthy of your name. Get rid of them, John. Get rid of them both.\n
    Your beloved,\n
    Beatrix{/i}"
    "The letter has a sender address. It comes from Seattle. This is too much."
    $hasLetter = True
    "You take the letter."
    hide studyletter
    return

label intCheque:
    show studychequebook at truecenter zorder 30
    "It appears to be a cheque book."
    e "A cheque book for... John Amity? Is this the bastard who took my dog?
    It can’t be. This cheque looks like it’s been made out to a airline. Where
    did you go, John?"
    $hasCheque = True
    "You take the cheque book."
    hide studychequebook
    return

label intChloroform:
    show studychloroform at truecenter zorder 30
    "It appears to be a chemical bottle."
    e "Chloroform? Geez, it’s half empty. You can kill someone with a dose like
    that."
    $hasChloroform = True
    "You take the bottle of chloroform."
    hide studychloroform
    return

label intBook:
    show studybook at truecenter zorder 30
    "The books on the shelf is copious, but you skim through the
    titles hoping for something useful."
    "One title stands out, {i}Safeguarding Your Home from Evil Spirits{/i} by
    Gerald Rivera. You quickly browse through the table of contents to discover
    a chapter of interest, \"Chapter XIII, Banshing Evil Spirits\"."
    "A spirit that enters a \"banishing circle\" will be forced to return to the
    netherworld. There are detailed instructions as well as a diagram on how to
    create one."
    "1. Draw an outer circle counter-clockwise.{w}
    \n2. Mark out 4 runes in order of north, east, south, and west.{w}
    \n3. Draw a smaller inner circle clockwise.{w}
    \n4. Draw a 5-pointed star within the smaller circle, beginning and ending
    on the east."
    e "Gotta find something large enough to draw this \"banishing circle\". Will
    also need something to draw with."
    $hasViewedBook = True
    hide studybook
    return

label intPhoto:
    show studyportrait at truecenter zorder 30
    "It’s a family portrait with a beautiful wife, smiling and holding her baby.
    The man standing beside her is looking serious."
    $hasViewedPhoto = True
    hide studyportrait
    return

label intLightStudyMain:
    if studyLight == 0:
        call switchLight from _call_switchLight_24
        $studyLight = 1
        show sceneStudy light
    else:
        call switchLight from _call_switchLight_25
        $studyLight = 0
        show sceneStudy dark
    return

label intLightStudyLamp1:
    if studyLamp1 == 0:
        call switchLight from _call_switchLight_26
        $studyLamp1 = 1
        show studyOverlay1 zorder 9
    else:
        call switchLight from _call_switchLight_27
        $studyLamp1 = 0
        hide studyOverlay1
    return

label intLightStudyLamp2:
    if studyLamp2 == 0:
        call switchLight from _call_switchLight_28
        $studyLamp2 = 1
        show studyOverlay2 zorder 9
    else:
        call switchLight from _call_switchLight_29
        $studyLamp2 = 0
        hide studyOverlay2
    return

# CHILD'S ROOM ITEMS #
label intHintChildsRoom:
    play sound "audio/toy_squeak.mp3"
    return

label intStain:
    "You take note of the markings on the carpet."
    e "What’s this stain?{w=1.0} It’s not blood."
    "You cautiously inspect it. The smell is faint and slightly sweet."
    "You stumble backwards feeling a little light-headed."
    e "It’s chloroform."
    e "So to recap, the wife was unfortunate to have been married to a bastard
    husband, who didn't have any love for either his wife or child and instead
    had an affair."
    e "Then in a conspiracy to get rid of them, he poisoned his own daughter
    with chloroform, and set the scene so that the wife would be accused with
    negligence."
    e "He succeed, as the wife blamed herself, and eventually took her own life.
    He then quickly took off to join his mistress."
    e "But the wife couldn't find rest even in death, and now haunts this place,
    consumed with the pain of having lost her child."
    e "Despite everything that's happened, she's not the real evil, just lost
    and in grief. Maybe there's a way to grant her closure, if she could learn
    of what really happened."
    $hasConcludedInvestigation = True

    if debug == True:
        "INVESTIGATION COMPLETED, FLAG SET FOR BEST ENDING ROUTE"
    return

label intLightChildsRoomMain:
    if childsRoomLight == 0:
        call switchLight from _call_switchLight_30
        $childsRoomLight = 1
        show sceneChildsRoom light
    else:
        call switchLight from _call_switchLight_31
        $childsRoomLight = 0
        show sceneChildsRoom dark
    return

label intLightChildsRoomLamp1:
    if childsRoomLamp1 == 0:
        call switchLight from _call_switchLight_32
        $childsRoomLamp1 = 1
        show childsRoomOverlay1 zorder 9
    else:
        call switchLight from _call_switchLight_33
        $childsRoomLamp1 = 0
        hide childsRoomOverlay1
    return

label intLightChildsRoomLamp2:
    if childsRoomLamp2 == 0:
        call switchLight from _call_switchLight_34
        $childsRoomLamp2 = 1
        show childsRoomOverlay2 zorder 9
    else:
        call switchLight from _call_switchLight_35
        $childsRoomLamp2 = 0
        hide childsRoomOverlay2
    return

# FOYER ITEMS #
label intHintFoyer:
    play sound "audio/chime.mp3"
    return

label intBasement1:
    play sound "audio/banging_door.mp3"
    e "Ugh! It wont budge!"
    "There is something strange about this door, almost as if it's frozen. It's
    cold to the touch and completely immovable. Even the door handle doesn't
    yield in the slightest."
    return

label intBasement2:
    if isDoor1Salted == False or isDoor2Salted == False or saltCount == 0:
        e "There's bound to be salt in here. If I can cover the three
        doors in this room, I may be able to trap her. I doubt she'll
        want to leave the house, so she'll have only one place to go..."

    e "But how do I get her in here. Maybe there's something here
    I could use to lure her. What would be precious to her? Perhaps
    something related to her child?"
    return

label intSilverOrnament:
    show foyersilverornament at truecenter zorder 30
    $hasSilverOrnament = True
    "You take the silver ornament."
    hide foyersilverornament
    return

label intSaltDoor1:
    if saltCount > 0:
        "You salt the doorway."
        $isDoor1Salted = True
        $saltCount -= 1
        if isDoor1Salted and isDoor2Salted and saltCount > 0:
            e "That's two doors done. Now for the lure."
        elif isDoor1Salted and isDoor2Salted and saltCount == 0:
            e "That's two doors, but we need some more salt."
    else:
        "We need to find some salt."
    return

label intSaltDoor2:
    if saltCount > 0:
        "You salt the doorway."
        $isDoor2Salted = True
        $saltCount -= 1
        if isDoor1Salted and isDoor2Salted and saltCount > 0:
            e "That's two doors done. Now for the lure."
        elif isDoor1Salted and isDoor2Salted and saltCount == 0:
            e "That's two doors, but we need some more salt."
    else:
        "We need to find some salt."
    return


label intLightFoyerMain:
    if foyerLight == 0:
        call switchLight from _call_switchLight_36
        $foyerLight = 1
        show sceneFoyer light
    else:
        call switchLight from _call_switchLight_37
        $foyerLight = 0
        show sceneFoyer dark
    return

# LIVING ROOM ITEMS #
label intHintLivingRoom:
    play sound "audio/whistling_wind.mp3"
    return

label intSilverLetterOpener:
    show livingletteropener at truecenter zorder 30
    $hasSilverLetterOpener = True
    "You take the silver letter opener."
    hide livingletteropener
    return

label intCanvas:
    show canvas at truecenter zorder 30
    "You look upon an intriguing abstract painting. It should be large enough
    for a banishing circle."
    e "It's a pity to destroy a work of art, but probably won't be missed too
    much."
    "You take the canvas."
    $hasCanvas = True
    hide canvas
    if livingRoomLight == 0:
        show sceneLivingRoom darkNoPainting
    else:
        show sceneLivingRoom lightNoPainting
    return

label intSoot:
    show soot at truecenter zorder 30
    "You look into an old fireplace. Nothing much in here but soot. Maybe this
    could be used for drawing."
    e "Guess there's no choice but to get my hands dirty."
    "You take a handful of soot."
    $hasSoot = True
    hide soot
    return

label intBanishingCircle:
    if hasCanvas and hasSoot:
        show canvas at truecenter zorder 30
        "You lay the painting upside-down, now seeing only a blank canvas."
        "You grab a pinch of soot from your pocket."
        e "Okay, how do we do this?"
        call constructBanishingCircle from _call_constructBanishingCircle
        hide canvas
        show banishing_circle at truecenter zorder 30
        e "That should do it! Now to give her a send-off."
        e "You take the banishing circle."
        $hasBanishingCircle = True
        hide banishing_circle
    else:
        "There's a wide open space to make a banishing circle, but we're going
        to need something to draw on and something to draw with."
    return

label intLightLivingRoomMain:
    if hasCanvas:
        if livingRoomLight == 0:
            call switchLight from _call_switchLight_38
            $livingRoomLight = 1
            show sceneLivingRoom lightNoPainting
        else:
            call switchLight from _call_switchLight_39
            $livingRoomLight = 0
            show sceneLivingRoom darkNoPainting
        return
    else:
        if livingRoomLight == 0:
            call switchLight from _call_switchLight_40
            $livingRoomLight = 1
            show sceneLivingRoom light
        else:
            call switchLight from _call_switchLight_41
            $livingRoomLight = 0
            show sceneLivingRoom dark
        return

label intLightLivingRoomLamp1:
    if livingRoomLamp1 == 0:
        call switchLight from _call_switchLight_42
        $livingRoomLamp1 = 1
        show livingRoomOverlay1 zorder 9
    else:
        call switchLight from _call_switchLight_43
        $livingRoomLamp1 = 0
        hide livingRoomOverlay1
    return

# MISC ITEMS #
label intTeddyBear:
    show teddy at truecenter zorder 30
    $hasTeddyBear = True
    e "What's this...{w=1.0} a teddy bear?{w=1.0} Was this here before?"
    $isTeddyBearMoving = False
    hide teddy
    return

label intNoLights:
    "This must be a light switch."
    call switchLight from _call_switchLight_44
    e "Damn, power must be out. Maybe there's a power generator around here
    somewhere."
    return

label intNoLights2:
    "This must be a light switch."
    call switchLight from _call_switchLight_45
    e "I need to get the generator running first."
    return

label setTeddyLocation:
    $teddyBearLocation = ghostOldLocation
    return

label switchLight:
    play audio "audio/switch.mp3"
    return

label doorOpen:
    play audio "audio/door_open.mp3"
    #$ renpy.pause(1, hard=True)
    return

label doorHandle:
    play audio "audio/door_handle.mp3"
    #$ renpy.pause(1, hard=True)
    return

label playMusic:
    play music "audio/main_bg.mp3"
    return

label playWhispers:
    play music "audio/whispers.mp3"
    return

label playHeartbeats:
    play music "audio/heartbeat.mp3"
    return

label playNightSounds:
    play music "audio/night.mp3"
    return

label pauseMusic:
    stop music fadeout 1.0
    return

label ghostLaugh:
    play sound "audio/ghost_laugh.mp3"
    return

label ghostLaugh2:
    play sound "audio/ghost_laugh2.mp3"
    return

label ghostScream:
    play sound "audio/aud_scream.mp3"
    return

label ghostShriek:
    play sound "audio/ghost_shriek.mp3"
    return

label slash:
    play audio "audio/slash.mp3"
    return

label stab:
    play audio "audio/stab.mp3"
    return

label hit:
    play audio "audio/hit.mp3"
    return

label burst:
    play audio "audio/burst.mp3"
    return

label smash:
    play audio "audio/smash.mp3"
    return

label scratch:
    play audio "audio/scratch.mp3"
    return

label vortexOpen:
    play audio "audio/vortex_open.mp3"
    return

label vortexClose:
    play audio "audio/vortex_close.mp3"
    return

label dogBark1:
    play sound "audio/dog_bark1.mp3"
    return

label dogBark2:
    play sound "audio/dog_bark2.mp3"
    return

label dogPanting:
    play sound "audio/panting.mp3"
    return

label dogLick:
    play sound "audio/lick.mp3"
    return

label breathing:
    play audio "audio/lick.mp3"
    return

label ghostTaunt:
    $ renpy.pause(1, hard=True)
    call ghostLaugh2 from _call_ghostLaugh2_1
    show ghost anim
    return

label ghostStrike:
    $ renpy.pause(1, hard=True)
    call ghostScream from _call_ghostScream_3
    $ renpy.pause(0.5, hard=True)
    show ghost anim
    with vpunch
    return

label ghostVanish:
    hide ghost
    with dissolve
    return

label whiteFlash:
    show white
    $ renpy.pause(0.1, hard=True)
    hide white
    with dissolve
    return

label redFlash:
    show red
    $ renpy.pause(0.1, hard=True)
    hide red
    with dissolve
    return


# Banishing Circle Construction #
label constructBanishingCircle:
    menu:
        "Draw outer circle counter-clockwise":
            "You draw a large circle in a counter-clockwise direction."

        "Draw outer circle clock-wise":
            "You draw a large circle in a clockwise direction."
            $isBanishingCircleCorrect = False

    menu:
        "Mark 4 runes for each direction, starting north and ending west":
            "You draw runes in the order of north, east, south, and west."

        "Mark 4 runes for each direction, starting east and ending north":
            "You draw runes in the order of east, south, west, and north."
            $isBanishingCircleCorrect = False

        "Mark 4 runes for each direction, starting north and ending east":
            "You draw runes in the order of north, west, south, and east."
            $isBanishingCircleCorrect = False

    menu:
        "Draw smaller inner circle counter-clockwise":
            "You draw a smaller circle in a counter-clockwise direction."
            $isBanishingCircleCorrect = False

        "Draw smaller inner circle clockwise":
            "You draw a smller circle in a clockwise direction."

    menu:
        "Draw a star beginning and ending on the north":
            "You draw 5-pointed star in the center beginning and ending on the
            north."
            $isBanishingCircleCorrect = False

        "Draw a star beginning and ending on the east":
            "You draw 5-pointed star in the center beginning and ending on the
            east."

        "Draw a star beginning and ending on the south":
            "You draw 5-pointed star in the center beginning and ending on the
            south."
            $isBanishingCircleCorrect = False

        "Draw a star beginning and ending on the west":
            "You draw 5-pointed star in the center beginning and ending on the
            west."
            $isBanishingCircleCorrect = False
    return

image wicksm light = "prologue/wicksm.png"
image wicksm dark = "prologue/wickdarksm.png"

define ds = Dissolve(2.0, 0.0, 0.0)

label prologue:
    call playNightSounds from _call_playNightSounds
    scene woods
    with fade
    "The sun is setting on what you can only envisage as a pleasant evening."

    scene woodscloseup
    with Dissolve(2)
    show wicksm dark at truecenter
    with easeinleft
    call dogBark2 from _call_dogBark2_3
    $ renpy.pause(2, hard=True)

    scene black
    show wicksm light at truecenter
    with dissolve
    call dogPanting from _call_dogPanting_2
    $ renpy.pause(2, hard=True)

    "You are out on a stroll with Wick, a Golden Retriever, who has been your
    faithful companion for 8 years."

    scene woodscloseup
    show wicksm dark at truecenter
    with dissolve
    call dogBark1 from _call_dogBark1_1

    "Out of the blue, he appears agitated and begins frantically pacing about."
    "Before you can attempt to console him, he dashes off, heading straight into
    a grove."

    hide wicksm
    with easeoutright

    #play sound "audio/running.mp3"
    play extraAudio2 "audio/running.mp3" fadein 1.0
    play extraAudio "audio/breathing.mp3" fadein 4.0
    scene black
    with Dissolve(2)
    "You give chase, desperately trying to keep up, but it's not long before you
    lose sight of him."

    "Still, you are determined to bring him back, and you decide to pursue in
    the same general direction. You run for what feels like an eternity."

    stop extraAudio2 fadeout 2.0
    "Just as you are about to collapse from exhaustion, you catch a glimpse of
    something beyond a cluster of trees."

    scene housedistant
    with Dissolve(5)

    "Amidst the scarce lighting you can barely discern what appears to be a
    house{w=2} - a very old and dilapidated house."

    scene houseclose
    with Dissolve(3)

    "There seems to be no sign of any occupants, but you approach the house,
    still gasping for breath."

    "As you close in on the front door, you notice a faint glint on the floor."

    stop extraAudio fadeout 5.0
    show hand
    with easeinbottom

    "Upon closer inspection, you recognise the small metal plate - a dog tag
    engraved, Wick.{w=2} In a moment you are assaulted by a flurry of questions,
    and panic sets in."

    "As you are haunted by the thought of your poor friend suffering, fear soon
    turns to fury and everything is drowned out by one overriding sentiment:{w=2}
    NO ONE...{w=1} MESSES...{w=1} WITH...{w=1} MY DOG!{w=1}"

    hide hand
    with easeoutbottom
    "Without hesitation, you decide to barge in, not even giving a thought to
    knocking on the door."

    call doorHandle from _call_doorHandle
    "Surprisingly, the door offers no resistance, as it
    swings wide open."

    call pauseMusic from _call_pauseMusic_10
    scene black
    with fade

    return
