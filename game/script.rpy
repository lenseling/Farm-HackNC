# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define trudy = Character("[name]")
define aub = Character("Aubrey Jene")
define bis = Character("Biscuit 'Kit' Croissant")
define cou = Character("Cheval 'Zach' Chourgette")
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
                
    "There is a long driveway up a hill to the farm from the road where I have been dropped off. I take in my surroundings." 
            
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

        "I am torn between awestruck appreciation and the urge to hurry home."
        
        trudy "What a sight to behold."

    label day_three:
        scene sunset

        show screen day_break("week one: wednesday")
        pause
        hide screen day_break

        "I wake up before the farm this morning. It is still dark outside, but the fields called to me in a distant dream."

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

    jump chapter_two


label chapter_two:
    show screen day_break("week one: saturday")
    pause
    hide screen day_break

    label meet_kit:
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

        bis "Biscuit Crossaint, Kit for short. I live next door - it's good to finally meet you!"

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

            "We part ways at the bustling town square to set up our own stalls. I promise to find them later for a sample of their famous begonia honey."

            jump meet_aubrey

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

            "We part ways at the bustling town square to set up our own stalls."

            jump meet_aubrey

    label meet_aubrey:
        "My first customer arrives within minutes."

        scene farm # market

        show aubrey:
            xalign 0.75
            yalign 1.0

        "A tall woman with aubergine hair saunters over. She sneers at my carrots."

        aub "And you are?"

        show trudy-shock:
            xalign 0.25
            yalign 1.0

        menu:
            "{i}I'm scared.{/i}":
                jump aub_bad
            "{i}I refuse to back down.{/i}":
                jump aub_good
            "{i}I'm too stunned to speak.{/i}":
                "The woman looks me up and down and scoffs, unimpressed."

                "?" "Well I clearly don't have to worry about {i}you{/i}."

                jump zach_aub_bad

        label aub_good:
            hide trudy-shock
            show trudy-neutral:
                xalign 0.25
                yalign 1.0
            
            "I push back my shoulders and look her evenly in the eye."
            
            trudy "I'm [name]. And you?"
            
            aub "[name]...The Begonia girl, yes? Aubrey Jene. Pleasure."
            
            aub "Listen up, new girl. I like you. There's a lot of things you don't know about this town. Don't get cocky."

            "She starts to walk away, then pauses and turns back."

            aub "And don't you dare think you can usurp me at the county fair."

            jump zach_aub_good
            
        label aub_bad:
            trudy "I-I’m [name]. I-I’m pretty new around these parts, I’ve been here for about a week."

            "?" "Excuse me? Speak up, will you. Whatever."

            aub "Listen up, new girl. My name is Aubrey Jene and I've won the county fair for three years running. Don’t try and steal my thunder."

            trudy "..."

            "Aubry rolls her eyes and stalks away in her red cowboy boots."

            jump zach_aub_bad

    label zach_aub_good:
        hide aubrey

        "I breathe out a sigh of relief. As I gaze at her retreating form, I catch the eye of a young man in the crowd."

        "?" "Quite impressive, darling, quite impressive indeed. Why, I haven't seen someone go toe to toe with Aubrey Jene in...I can't recall!"

        jump meet_zach

    label zach_aub_bad:
        hide aubrey

        "I let out a shuddering sigh and look into the crowd of people. There is a young man gazing back at me sympathetically."

        "?" "Oh, dear. [name], was it? We're sorry about her, she's always like that."

        "I smile back at him, relieved to meet a friendlier face."

        jump meet_zach

    label meet_zach:
        show zach:
            xalign 0.75
            yalign 1.0

        "?" "The name's Chourgette. Cheval Chourgette. Pleasure to meet your aquaintance."

        "I take a closer look at him. He's clean shaven, with high, aristocratic features."
        
        "Although his clothes look about the same cut as everyone else's, they are clearly newer and made of a silken material that shimmers subtly as he moves."

        menu:
            "Where'd you get your shirt?":
                "Chourgette beams, then abortedly tries to wink. The result is unexpectedly hilarious."

                "Chourgette" "Family secret, I'm afraid. But for you...stop by my estate someday. We ride horses. I'll give you the tour."

                "Chourgette" "Also, Zach is fine."

                jump meet_zach_2
            "...Chourgette? Like the vegetable?":
                "Chourgette" "We're French! You can call me Zach, though."

                "Chourgette winks."

                jump meet_zach_2
            "Nice to meet you, Cheval Chourgette.":
                "He makes a slight pout."

                "Chourgette" "Zach is fine, too."

                jump meet_zach_2

    label meet_zach_2:
        cou "Anywho, so good to see a new face in town. How are you settling in?"

        trudy "I'm doing great. I've made some real progress on the farm this week!"

        cou "Wonderful, wonderful. Could I get two of those carrots? They look mighty fine."

        "I hand Zach the two best carrots on my stand. Zach motions to a man behind him - a servant of some sort - to hand him his wallet."

        cou "Cash. Quaint, isn't it."

        "He sounds distracted. When I try to take the money from his outstretched hand, he leans in, refusing to let go."

        "I tug at it, but he continues to stare intently into my eyes. Finally, he seems to startle."

        cou "Yes, wonderful to hear, indeed."

        cou "We will meet again, [name]."

        "Zach turns and walks away with brisk strides, his previously unseen servants trailing behind him."

        "I think I catch a flash of an emotion - disappointment? relief? sorrow? or perhaps something darker - on his face as he vanishes into the crowd."

        hide zach

        trudy "How strange..."

    label meet_dan:
        "While I'm still pondering the strange interaction, another man appears at my stand."

        show dan:
            xalign 0.75
            yalign 1.0

        "I jump in surprise."

        "?" "Hello, could I have some carrots?"

        trudy "Sure. I didn’t catch your name?"

        dan "It’s Dan. Nice to meet you."

        trudy "Nice to meet you as well. Enjoy the carrots!"

        "Dan nods. When I look up from counting out his change, he seems to have disappeared."

        hide dan

    scene sunset

    show trudy-neutral

    trudy "What an interesting town."

    "A strong wind blows in from north and the shed door clatters in agreement."

    trudy "Isn't it a tad too cold for the middle of summer?"

    "From my farmhouse at the top of the hill, I gaze at the rolling fields below."

    scene night

    "Nestled in scattered crooks and crannies throughout the countryside, warm little lights flicker in the hearths of tiny, distant homes."

    trudy "So beautiful..."

    "Kit had pointed out all the houses to me on our way back from the market."
    
    "There, far to the north, bordering the Red Woods, is the Chourgette estate."

    "The closest farm to the east is Immals Ranch, famous mostly for the tragic disappearance of their son years earlier."

    "To the west, the Aubergine Vineyard stands proud as the most prominent exporter in the county, having made a remarkable recovery from the brink of bankruptcy."

    "A cluster of brighter lights due north of the ranch marks the town, like a guiding star."

    show trudy-happy

    trudy "Strange as it is, I think I could grow to love this place."

    "A whistling gust of wind kicks up a shower of begonia petals, sounding like high, wild laughter."

    jump chapter_three


label chapter_three:
    scene blank

    show screen day_break("Thank you for playing our demo :D.")
    pause
    hide screen day_break

    scene farm
    show trudy-wink:
        xalign 0.25
        yalign 1.0

    show screen day_break("To read more, please consider supporting the team!")
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

