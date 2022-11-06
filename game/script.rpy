# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define trudy = Character("[name]")
define aub = Character("Aubrey Jenes")
define bis = Character("Biscuit 'Kit' Croissant")
define cou = Character("Cheval Chourgette")
define dan = Character("Dan Immals")

define money = 200

# The game starts here.

label start:
    call prologue

    return


label prologue:
    scene room

    "Beep-beep-beep! The incessant honking outside my window wakes me from my slumber. It wasn’t like I got much sleep anyways."

    "The cloud cover is thick today. In the dead heat of summer, a choking heaviness fills my lungs. I struggle to breathe."

    "I would panic, but I've lived with this feeling for as long as I can remember; the numbness of routine has already settled in my bones."

    show trudy-neutral

    "Bringing myself to my desk is easier said than done. The brightness of the screen sears my glazed eyes as I scan the emails piling up in my inbox." 
    
    "Nothing new, nothing interesting. Just advertisements and spam messages galore." 
    
    "I’ve given up on expecting emails back from job applications." 
    
    "The golden wings of hope between my ribs are bogged down by the humidity, and the fluttering in my chest is more likely panic. Or a heart attack."

    "I decide to take a walk to clear my mind. Though the air is smoggy and suffocating, it feels better than the apartment walls closing in on me."

    scene street

    show trudy-neutral:
        xalign 0.25
        yalign 1.0

    "Jogging is freeing, in a way. With music pounding in my ears and the breeeze in my hair, I feel boundless and featherlight."

    "I lose my loneliness in the winding city streets."
    
    "Looking at the stately, trimmed bushes lining the sidewalk, I pause for a breath."

    "My route has led me to the post office." 
    
    "Although I rarely stop by – I have no reason to. I get the occasional package, but nothing worth checking for. – today I decide I might as well."

    "Upon opening my P.O. box, I discover a slightly crumpled letter. It is the only thing in the small box, and I gently take it out to observe it."
    
    show letter:
        xalign 0.75
        yalign 1.0

    python:
        name = renpy.input("On the envelope is my name in elegant handwriting: To ")
        name = name.strip() or "Trudy"

    "My brows furrow in confusion. Who could it be from?"

    menu:
        "{i}Open the envelope.{/i}":
            jump choice_open

        "{i}Ignore.{/i}":
            jump choice_ignore
    
    label choice_open:

        "The Letter" "Dear [name], if this letter has found you, I have already made my way into the afterlife. I know we haven't talked much in recent years, but you are the only person I believe I can truly trust." 
        
        "The Letter" "This letter is to let you know that you now have full ownership of my farm, Begonia Grove."
        
        "The Letter" "It’s not much, but it’s the only thing I have left to offer you. I hope that you can give it new life — maybe even more than I could."

        "The Letter" "Sincerely, Grandpa"
        
        "My breath catches in my throat for a moment. This is a chance, a sign, an opportunity to find a new meaning to my mundane life."

        hide letter
        
        "By the end of the night, all of my belongings are packed and ready to go. It is time to start anew."
        
        jump chapter_one

    label choice_ignore:
        trudy "Just junk."

        hide letter
        
        "I toss the letter in the trash and make my way back home."

        # This ends the game.
        return


label chapter_one:
    scene blank

    show screen day_break("week one: sunday")
    pause
    hide screen day_break

    "As I shut the door of the taxi behind me, my thoughts race through my mind."

    "What is the farm going to look like? What am I going to do there? What am I doing? I don't know how to farm!"

    scene farm
                
    "There is a long driveway up to the farm from the road where I have been dropped off. I take in my surroundings." 
            
    "Red begonias adorn every inch of the place. I suppose that is how the farm received its name."

    "After a slow five minute walk, I finally made it to the entrance."

    show trudy-shock
    
    "The gates creak softly as I push past them, and the mud on the ground from a recent rain cakes around my shoes."
    
    "The sky hangs low on the horizon. The crops - for some reason, all carrots - sink into the ground, while the few livestock wander around aimlessly." 
    
    "Old machinery sits on the outskirts of the fields, broken and dilapidated. I touch one, and my finger comes away with a buildup of dust and grime."

    "I breathe in the country air. There is a lot of work to be done."

    label day_one:
        scene sunset

        show screen day_break("week one: monday")
        pause
        hide screen day_break

        "The crowing of a lone rooster startles me awake."

        show trudy-neutral
        
        "It strikes a chord inside me, strangely. Perhaps because of how raw the sounds is in comparison to the industrial cacophony that I typically rise to."

        "I throw on a simple tee and work pants before heading down to the fields."
        
        "I am dedicating the rest of my life savings to fixing the farm - all $200 of the crumpled bills in my wallet."
        
        trudy "What should I start with today?"

        # mini game
        scene farm

        show screen money_game("Sell eggs collected from chickens","Fix machinery","Buy fertilizer")
        pause

        scene night

        "I wipe the sweat from my brow and stretch out my sore joints."
        
        trudy  "All in a day’s work!"

        "As I shuffle back to my bed, I can’t help but feel uneasy, as if there was someone - or something - watching me."
        
        "I shake my head before slinking into the warmth of my blankets. It was probably nothing."

    label day_two:
        scene sunset

        show screen day_break("week one: tuesday")
        pause
        hide screen day_break

        "The sun feels warm on my skin as it peeks through the thin linen curtains covering the windows."

        show trudy-neutral

        "I slept in today, still groggy from the previous day’s work."

        # mini game
        scene farm

        show screen money_game("Sell milk collected from cows","Weed crops","Buy new machinery parts")
        pause

        scene night

        "A gust of wind rushes at me as I close the barn gates for the night. I feel a chill run down my spine."
        
        "A shower of begonia petals flutter around me like a crimson celebration."

        "I am torn between awe and the urge to hurry home."
        
        trudy "What a sight to behold."

    label day_three:
        scene sunset

        show screen day_break("week one: wednesday")
        pause
        hide screen day_break

        "I awoke before the farm did this morning. It was still dark outside, but the fields called to me in a distant dream."

        show trudy-shock
        
        "They said something about...hurrying. Hurry and tend to them. The fields are thirsty and waiting."
        
        "A shot of adrenaline invigorates me further."

        # mini game
        scene farm
        
        show screen money_game("Sell carrots","Water crops","Buy more chickens")
        pause

        scene night

        "A wave of exhaustion passes through my body as I sit on a tipped over milking bucket."

        "For a split second, the cows seem to smile at me, almost if they were appreciating my hard work."

        "I smile back, patting one on the nose. Things are looking up."

    label day_four:
        scene sunset

        show screen day_break("week one: thursday")
        pause
        hide screen day_break

        "The days are beginning to feel natural. Running a farm is hard work, but honest and rewarding all the same."

        show trudy-happy

        "Everything here is beautiful, from the brightness of the morning sun to the crowing of the lone rooster."

        # mini game
        scene farm
        
        show screen money_game("Sell eggs collected from chickens","Tend to livestock","Buy better cow feed")
        pause

        scene night

        "Looking at the farmscape, I grin."

        "For the first time in forever, I can see a future for myself."

    label day_five:
        scene sunset

        show screen day_break("week one: friday")
        pause
        hide screen day_break

        show trudy-happy

        "Energy courses through my veins. I never knew routine could feel this good."

        # mini game
        scene farm
        
        show screen money_game("Sell carrots","Take a break","Give out free samples")
        pause

        scene night

        "I count the money I have in my pocket. [money] dollars."

        trudy "I can work with this."

        "Tomorrow is the weekend. It is time to explore."

    jump chapter_two


label chapter_two:
    show screen day_break("week one: saturday")
    pause
    hide screen day_break

    label kit:
        scene blank

        "It’s the first Saturday of the month, and I step outside to greet the fresh air."

        scene farm

        "Past the hill, in the distance, I see a person standing near the gate."

        "I go out to welcome them."

        show trudy-happy:
            xalign 0.25
            yalign 1.0

        trudy "Hello! Who might you be?"

        show kit:
            xalign 0.75
            yalign 1.0

        bis "Biscuit Crossaint, but you can call me Kit. I live next door - it's good to finally meet you!"

        "Kit is incredibly bubbly and happy to see me."

        menu:
            "{i}I like her immediately.{/i}":
                jump kit_good

            "{i}It's too early to deal with this much energy.{/i}":
                jump kit_bad

            "Go away.":
                jump chapter_three

        label kit_good:
            trudy "Nice to meet you too! What brings you around?"

            bis "Today's market day down in the town. Everybody in the county will be there and it's my neighborly duty to invite you along!"
        
            bis "Do you have anything you want to sell? I’ll have flower infused honey and baked treats at my stand."

            "I have a seemingly neverending supply of carrots. This is the perfect opportunity to get rid of them!"

            trudy "Of course!"

            scene blank

            "Kit and I walk to the market and chat about my move from the city."

            "We part ways at the town square to set up out own stalls. I promise to find them later for a free cookie."

            jump aubrey

        label kit_bad:
            hide trudy-happy
            show trudy-neutral:
                xalign 0.25
                yalign 1.0

            trudy "What do you want."

            "Kit hesitates."

            bis "Today's market day down in the town. Everybody in the county will be there and it's my neighborly duty to invite you along!"
        
            bis "Do you have anything you want to sell? I’ll have flower infused honey and baked treats at my stand."

            "I have a seemingly neverending supply of carrots. This is the perfect opportunity to get rid of them!"

            trudy "Sure."

            scene blank

            "Kit and I walk to the market in silence. Although I prefer it, Kit seems to find it awkward."

            "We part ways at the town square to set up out own stalls."

            jump aubrey

    label aubrey:


    label zach:

    label dan:

    jump chapter_three


label chapter_three:
    show screen day_break("a sneak peak")
    pause
    hide screen day_break

    scene farm
    show trudy-wink:
        xalign 0.25
        yalign 1.0
    show dan:
        xalign 0.75
        yalign 1.0
    
    scene blank
    show trudy-shock
    hide trudy-shock

    show screen day_break("more to come...")
    pause
    hide screen day_break

    return


# Displays before each day
screen day_break(day):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        text day


# Money decision mini-game
screen money_game(plus, zero, minus):
    frame:
        xalign 0.5 yalign 0.5
        xpadding 60 ypadding 60
        vbox:
            spacing 50
            text "$[money]" xalign 1.0 yalign 0.5
            textbutton plus xalign 0.5 yalign 0.5:
                action [Hide("money_game"), Call("add_money", 50)]
            textbutton zero xalign 0.5 yalign 0.5:
                action Hide("money_game")
            textbutton minus xalign 0.5 yalign 0.5:
                action [Hide("money_game"), Call("sub_money", 50)]


# Updates money variable
label add_money(x):
    $ money += x
    return


label sub_money(x):
    $ money -= x
    return

