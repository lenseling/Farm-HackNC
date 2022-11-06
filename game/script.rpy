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

    "The cloud cover is thick today. A sense of heaviness fills the atmosphere, almost choking me."

    "It felt like every other day that I had lived in the past 28 years of my life; however the numbness of routine had already settled in my bones."

    show trudy-neutral

    "Bringing myself to my desk was easier said than done. The brightness of the screen seared my eyes as I glazed over the emails piling up in my inbox." 
    
    "Nothing new, nothing interesting. Just advertisements and spam messages galore." 
    
    "I’d already given up on expecting emails back from job applications – I never knew why I still kept a sliver of hope left in my chest."

    "I decided to take a walk to clear my head. Though the air was smoggy and suffocating, it felt better than the apartment walls surrounding me."

    scene street

    show trudy-neutral:
        xalign 0.25
        yalign 1.0

    "Jogging always felt like the only times I could truly be free. With the music pounding in my ears and the wind flowing through my hair, I felt boundless and featherlight." 
    
    "Looking at the nicely trimmed bushes lining the sidewalk, I took a deep breath in." 
    
    "I’d always wondered how it would be like to fit in. Loneliness was more of a circumstance than a choice at this point."

    "My jogging route took me to the post office, where I rarely stopped by. I had no reason to, as I kept to myself for the most part."
    
    "The occasional package was sent to me, but nothing worth checking for."

    "Upon opening my P.O. box, I noticed a slightly crumpled letter. It was the only thing in the small box, and I gently took it out to observe it."
    
    show letter:
        xalign 0.75
        yalign 1.0

    python:
        name = renpy.input("On the envelope was my name in elegant handwriting: To ")
        name = name.strip() or "Trudy"

    "My brows furrowed in confusion. Who could it be from?"

    menu:
        "Open the envelope":
            jump choice_open

        "Ignore":
            jump choice_ignore
    
    label choice_open:

        "The Letter" "Dear [name], if this letter has found you, I have already made my way into the afterlife. I know we never talked much, but you are the only person I believe I can truly trust." 
        
        "The Letter" "This letter is to let you know that you are now in full ownership of my farm, Begonia Grove."
        
        "The Letter" "It’s not much, but it’s the only thing I have to give to my granddaughter. I hope that you can give it new life, and maybe even more than I could."

        "The Letter" "Sincerely, Grandpa"
        
        "My breath caught in my throat for a moment upon finishing the letter. This was my chance, my opportunity to truly find a new meaning to my mundane life."

        hide letter
        
        "By the end of the night, all my belongings were packed and ready to go. It was time to start anew."
        
        jump chapter_one

    label choice_ignore:
        trudy "Just junk."

        hide letter
        
        "I tossed the letter in the trash and made my way back home."

        # This ends the game.
        return

label chapter_one:
    scene blank

    show screen day_break("day zero")
    pause
    hide screen day_break

    "As I shut the door of the taxi behind me, my thoughts raced through my mind."

    "What was the farm going to look like? What was I going to do on the farm? What was I doing? I don't know how to farm!"

    scene farm
                
    "The farm was a bit of a distance from where I had been dropped off. I took in my surroundings." 
            
    "Begonias adorned every inch of the place. I supposed it was how the farm received its name."

    "After about 5 minutes of slow walking, I finally made it to the entrance to the farm."

    show trudy-shock
    
    "The gates creaked softly as I stepped past them, and the dirt on the ground caked around my shoes. There was an air of moodiness about the farm."
    
    "The crops seemed to sink into the ground, while the few livestock wandered around hopelessly." 
    
    "Old machinery collected dust and grime on the outskirts of the fields, broken and dilapidated."

    "I breathe in the country air. There was work to be done."

    label day_one:
        scene farm

        show screen day_break("day one")
        pause
        hide screen day_break

        "The crowing of a lone rooster startled me awake."

        show trudy-neutral
        
        "It struck a chord inside me to hear something so raw in comparison to the industrial cacophony that I typically arose to."

        "I threw on a simple tee and work pants before heading down to the fields."
        
        "I dedicated the rest of my life savings to fixing the farm - all $200 of the crumpled bills in my wallet."
        
        trudy "What should I start with today?"

        # mini game
        scene farm

        show screen money_game("Sell eggs collected from chickens","Fix machinery","Buy fertilizer")
        pause

        "I wiped the sweat from my brow and stretched out my sore joints."
        
        trudy  "All in a day’s work!"

        "As I shuffled back to my bed, I couldn’t help but feel uneasy, as if there was someone - or something - watching me."
        
        "I shook my head before slinking into the warmth of my blankets. It was probably nothing."

    label day_two:
        scene farm

        show screen day_break("day two")
        pause
        hide screen day_break

        "The sun felt warm on my skin as it peeked through the thin linen blinds covering the windows."

        show trudy-neutral

        "I slept in today, still feeling a bit groggy from the previous day’s work."

        "I checked my wallet to see how much money I had to work with. [money] dollars. Not bad. I’ll see what I can get done."

        # mini game
        scene farm

        show screen money_game("Sell milk collected from cows","Weed crops","Buy new machinery parts")
        pause

        "Upon closing the gates of the barn, I felt a chill run down my spine as a gust of wind swept my hair upwards."
        
        "The petals of the begonias fluttered around me like a celebration of crimson."
        
        trudy "What a sight to behold."

    label day_three:
        scene farm

        show screen day_break("day three")
        pause 
        hide screen day_break

        "I awoke before the farm did this morning. It was still dark outside, but the fields called to me in a distant dream."

        show trudy-neutral
        
        "I count the money on my bedside table. [money] dollars. I’ve got a long day ahead."

        # mini game
        scene farm
        
        show screen money_game("Sell carrots","Tend to livestock","Buy more chickens")
        pause

        "A wave of exhaustion passed through my body as I sat on a tipped over milking bucket."

        "For a split second, the cows seemed to smile at me, almost if they were appreciating my hard work."

        "I smiled back, knowing my labor was paying off."

    label day_four:
        scene farm

        show screen day_break("day four")
        pause
        hide screen day_break

        "The days were beginning to feel natural at this point."

        show trudy-happy

        "From the chirping of the birds to the brightness of the sun in the mornings — for the first time in forever, I felt at home in a place where I belonged."

        "I looked at my wallet, but I didn’t need to count the money. I knew I had [money] dollars from the day before."

        # mini game
        scene farm
        
        show screen money_game("Sell eggs collected from chickens","Take a break","Buy better cow feed")
        pause

        "Looking at the farmscape, I grinned."

        "Change was beginning to instill itself into the roots of the earth. I could feel a shift within myself, and I no longer hated being alone."

    label day_five:
        scene farm

        show screen day_break("day five")
        pause
        hide screen day_break

        "Energy coursed through my veins as things began to fall into routine."

        show trudy-happy

        "I knew I had [money] dollars in savings. I just needed to figure out what to do with it."

        # mini game
        scene farm
        
        show screen money_game("Sell carrots","Meet the neighbors","Give out free samples")
        pause

        "I counted the money I had in my pocket. [money] dollars."

        trudy "I can work with this."

        "Tomorrow was the weekend. It was time to explore."

    jump chapter_two
    
label chapter_two:
    jump chapter_three

label chapter_three:
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
        xalign 0.5 yalign 0.25
        textbutton plus:
            action [Hide("money_game"), Call("add_money", 50)]
    frame:
        xalign 0.5 yalign 0.5
        textbutton zero:
            action Hide("money_game")
    frame:
        xalign 0.5 yalign 0.75
        textbutton minus:
            action [Hide("money_game"), Call("sub_money", 50)]

# Updates money variable
label add_money(x):
    $ money += x
    return

label sub_money(x):
    $ money -= x
    return

