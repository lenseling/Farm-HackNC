# The script of the game goes in this file.

# Declare characters used by this game.

define trudy = Character("[name]")
define aub = Character("Aubrey Jene")
define bis = Character("Biscuit 'Kit' Croissant")
define cou = Character("Cheval 'Zach' Chourgette")
define dan = Character("Dan Immals")

# Keeps track of money and day on farm
define money = 210
define day = 1
define bad_end = 0

# Keeps track of farm's mood
define mood = {0: "Angry", 1: "Sad", 2: "Neutral", 3: "Happy", 4: "Eggcellent"}
define chicken_mood = 1
define cow_mood = 1
define carrot_mood = 1

# Keeps track of action items and action item values
# For each iten in plus: ["item name", money gained if item selected]
# For each item in zero: ["item name", add to eggs, add to milk, add to carrots, valid]
# For each item in minus: ["item name", money lost if item selected]
# Mood affected: 1 for chicken, 2 for cow, 3 for carrot
define plus = {0: ["Sell eggs", 20], 1: ["Sell milk", 20], 2: ["Sell carrots", 25]}
define zero = {0: ["Water crops", 0, 0, 5, True], 1: ["Weed crops", 0, 0, 5, True], 2: ["Tend to livestock", 5, 5, 0, True], 3: ["Fix machinery", 5, 5, 5, False], 4: ["Apply fertilizer", 0, 0, 10, False]}
define minus = {0: ["Buy new machine parts", 50], 1: ["Buy fertilizer", 20], 2: ["Buy better feed", 20], 3: ["Buy more chickens", 30]}

# The game starts here.

label start:
    call prologue from _call_prologue
    return

# Prologue: Trudy recieves a mysterious letter in the mail. Her grandfather has passed away – and is giving her his farm!

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

    # User can input a chosen name. Default name is Trudy.

    python:
        name = renpy.input("On the envelope is my name in elegant handwriting: To ")
        name = name.strip() or "Trudy"

    "My brows furrow in confusion. Who could it be from?"

    # Option to read or ignore letter. Reading will progress story. Ignoring will end game.

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

        jump chapter_end


# Chapter One: Trudy finds Begonia Grove in a state of disrepair. 

label chapter_one:
    play music "/audio/mystery.mp3"

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

    # explain end of day game mechanic
    
    call end_day from _call_end_day

    "Yikes! Gotta watch out for living expenses. There goes $10!"

    "Would Begonia Grove be alright if I didn't take care of it...? Probably not."

    # Start money decision making mini-game sequence. Play through a week of decision making. Repair the farm and avoid going bankrupt!

    label wk1_d1:
        call begin_day("week one: monday") from _call_begin_day

        "The crowing of a lone rooster startles me awake."

        show trudy-neutral
        
        "It strikes a chord inside me, strangely. Perhaps because of how raw the sounds is in comparison to the industrial cacophony that I typically rise to."

        "I throw on a simple tee and work pants before heading down to the fields."
        
        "I am dedicating the rest of my life savings to fixing the farm - all $200 of the crumpled bills in my wallet."
        
        trudy "What should I tackle first?"

        # mini game tutorial
        scene blank
        show screen money_game_exp()
        pause
        hide screen money_game_exp

        # mini game
        call money_money from _call_money_money

        "I wipe the sweat from my brow and stretch out my sore muscles."

        show trudy-neutral
        
        trudy  "All in a day’s work!"

        "As I shuffle back to my bed, I can’t help but feel uneasy, as if there was someone - or something - watching me."
        
        "I shake my head before slinking into the warmth of my blankets. It was probably nothing."

        call end_day from _call_end_day_1

    label wk1_d2:
        call begin_day("week one: tuesday") from _call_begin_day_1

        "The sun feels warm on my skin as it peeks through the thin linen curtains covering the windows."

        show trudy-neutral

        "I slept in today, still groggy from the previous day’s work."

        # mini game
        call money_money from _call_money_money_1

        "A good day's work."

        call end_day from _call_end_day_2

    label wk1_d3:
        call begin_day("week one: wednesday") from _call_begin_day_2

        "I wake up before the farm this morning. It is still dark outside, but the fields called to me in a distant dream."

        show trudy-shock
        
        "They said something about...hurrying. Hurry and tend to them. The fields are thirsty and waiting."
        
        "A shot of adrenaline invigorates me further."

        # mini game
        call money_money from _call_money_money_2
        show trudy-neutral

        "A wave of exhaustion passes through my body as I sit on a tipped over milking bucket."

        "For a split second, the cows seem to smile at me, almost if they were appreciating my hard work."

        hide trudy-neutral
        show trudy-happy

        "I smile back, patting one on the nose. Things are looking up."

        call end_day from _call_end_day_3

    label wk1_d4:
        call begin_day("week one: thursday") from _call_begin_day_3

        "This life is beginning to feel natural."

        show trudy-happy

        "Everything here is beautiful, from the brightness of the morning sun to the crowing of the lone rooster."

        # mini game
        call money_money from _call_money_money_3

        "Looking at the farmscape, I grin."

        "For the first time in forever, I can see a future for myself."

        call end_day from _call_end_day_4

    label wk1_d5:
        call begin_day("week one: friday") from _call_begin_day_4
        show trudy-happy

        "Rise and shine!"

        # mini game
        call money_money from _call_money_money_4
        show trudy-neutral

        trudy "..."

        trudy "..."

        trudy "...Sometimes, I do get a little lonely out here."

        call end_day from _call_end_day_5

    jump chapter_two
    

# Chapter Two: On the first Saturday of the month, a neighbor invites Trudy to the town market. Meet the fascinating characters surrounding Begonia Grove!

label chapter_two:
    stop music fadeout 1

    call begin_day("week one: saturday") from _call_begin_day_5

    # Meet Biscuit 'Kit' Croissant. Bubbly, energetic, sweet – and our next door neighbor!
    # Kit's hobbies inclube experimental beekeeping and following their grandma's baking recipes.

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

        bis "Biscuit Croissant, Kit for short. I live next door - it's good to finally meet you!"

        "Kit is incredibly bubbly and happy to see me."

        # Choosing different prompts unlocks different dialogues.
        # With a future implementation of a heart point system, choosing the "good" ending will help you gain heart points - and vice versa.

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

    # Ruthless, shrewd, and competitive, Aubrey has built her empire from the ground up.
    # She's been crowned Harvest Queen at the county fair for three years running - and she plans to keep it that way.

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

        # Choosing different prompts unlocks different dialogues from Aubrey, as well as a different first meeting with Zach.
        # With a future implementation of a heart point system, choosing the "good" ending will help you gain heart points - and vice versa.

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

    # Zach may seem flamboyant, thoughtless, and richer than the rest of the county put together, but he knows /something/ about this town. They all do.
    # Zach is an equestrian on the side. He doesn't particularly like horses, but he loves when people ask about his name, and that pretty much makes up for it.

    label meet_zach:
        show zach:
            xalign 0.75
            yalign 1.0

        "?" "The name's Chourgette. Cheval Chourgette. Pleasure to meet your aquaintance."

        "I take a closer look at him. He's clean shaven, with high, aristocratic features."
        
        "Although his clothes look about the same cut as everyone else's, they are clearly newer and made of a silken material that shimmers subtly as he moves."

        # Choosing different prompts unlocks different dialogues.
        # With a future implementation of a heart point system, choosing the "good" ending will help you gain heart points - and vice versa.

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

        "I think I catch a flash of an emotion - disappointment? relief? concern? or perhaps something darker - on his face as he vanishes into the crowd."

        hide zach

        trudy "How strange..."

    # Dan's just a guy. He's just some dude. Really. Why are you asking so many questions?

    label meet_dan:
        "While I'm still pondering the interaction, another man appears at my stand."

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

    play music "audio/mystery.mp3" fadeout 1

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


# More farming sim!

label chapter_three:
    label wk2_d0:
        call begin_day("week two: sunday") from _call_begin_day_6
        show trudy-happy

        "That was a nice break. Let's get back into it!"

        # mini game
        call money_money from _call_money_money_5

        "I've only been here a week, but I can already see the fruits of my labors."

        call end_day from _call_end_day_6

    label wk2_d1:
        call begin_day("week two: monday") from _call_begin_day_7
        # mini game
        call money_money from _call_money_money_6

        "A gust of wind rushes at me as I close the barn gates for the night. I feel a chill run down my spine."
        
        "A shower of begonia petals flutter around me like a crimson celebration."

        "I am torn between awestruck appreciation and primal terror. I hurry home."

        show trudy-shock
        
        trudy "What a sight to behold."

        call end_day from _call_end_day_7

    label wk2_d2:
        call begin_day("week two: tuesday") from _call_begin_day_8
        show trudy-shock

        trudy "Another dream last night...I was lying in a flower field, begonias as far as eye could see."

        trudy "They eveloped me while singing the most beautiful song..."

        # mini game
        call money_money from _call_money_money_7
        show trudy-shock

        trudy "I wasn't alone in that field. I remember that now. But who was with me? And why was I so scared?"

        call end_day from _call_end_day_8

    label wk2_d3:
        call begin_day("week two: wednesday") from _call_begin_day_9
        show trudy-happy

        "Rise and shine!"

        # mini game
        call money_money from _call_money_money_8

        "It's not much, but it's honest work."

        call end_day from _call_end_day_9

    label wk2_d4:
        call begin_day("week two: thursday") from _call_begin_day_10
        show trudy-happy

        "Rise and shine!"

        # mini game
        call money_money from _call_money_money_9

        "The work is hard but rewarding. I'm so glad I took this opportunity."

        call end_day from _call_end_day_10

    label wk2_d5:
        call begin_day("week two: friday") from _call_begin_day_11
        show trudy-happy

        "Energy courses through my veins. I never knew routine could feel this good."

        # mini game
        call money_money from _call_money_money_10

        "I count the money I have in my pocket. [money] dollars."

        show trudy-happy

        trudy "I can work with this."

        call end_day from _call_end_day_11
    
    jump chapter_end

# Project is in development :)

label chapter_end:
    if bad_end == 1:
        call bad_end_1 from _call_bad_end_1
    if bad_end == 2:
        call bad_end_2 from _call_bad_end_2

    scene blank

    show screen day_break("Thank you for playing our demo :D.")
    pause
    hide screen day_break

    scene farm

    show screen day_break("To read more, please consider supporting our team!")
    pause
    hide screen day_break

    show trudy-wink

    # This ends the game.
    $ MainMenu(confirm=False)()

# You didn't expect to keep the farm with no money to run it, did you?

label bad_end_1:
    scene farm

    "Begonia Grove sits dilapidated. A foreclosure sign swings angrily on its hinges near the gate. The wind howls long and mourful."

    show kit:
        xalign 0.25 yalign 1.0
    show aubrey:
        xalign 0.75 yalign 1.0

    "Townsperson 1" "Poor girl. A good heart but no head for business, really."

    "Townsperson 2" "It's for the best really. That got to her before..."

    "Townsperson 1" "Yeah. Wonder what they'll do with this place."

    "Townsperson 2" "Whatever it is, I want nothing to do with it."

    "They share a look, and continue on their way."

    scene farm
    return

# Begonia Grove is very particular about its keepers.

label bad_end_2:
    scene blank
    show screen day_break("your crops are dead...")
    pause
    hide screen day_break
    show screen day_break("your cows are starving...")
    pause
    hide screen day_break
    show screen day_break("your chickens have fled the coop...")
    pause
    hide screen day_break
    show screen day_break("what now, little begonia girl?")
    pause
    hide screen day_break
    
    "The wind rises."

    return


# Beginning of day formatting. Return to call block.
label begin_day(d):
    $ day += 1

    scene sunset

    show screen day_break(d)
    pause
    hide screen day_break

    return


# End of day formatting. Check if money/farm happiness is too low. Go to ending if true, return to block if not.
label end_day:
    scene blank

    $ money -= 10

    if day%7 == 6:
        $ chicken_mood -= 1
        $ cow_mood -= 1
        $ carrot_mood -= 1
    
    if money < 0:
        $ bad_end = 1
        jump chapter_end
    elif chicken_mood == 0 and cow_mood == 0 and carrot_mood == 0:
        $ bad_end = 2
        jump chapter_end
    else:
        return


# Blank screen with text. Displays before each day.
screen day_break(day):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        text day


# Money decision mini-game. Return to call block.
# Randomly determine actions and pass to mini-game screen
label money_money:
    scene farm

    $ pval = renpy.random.randint(0,2)
    $ zval = renpy.random.randint(0,4)
    $ mval = renpy.random.randint(0,3)

    # If zval locked, choose new zval
    while (zero[zval][4] == False):
        $ zval = renpy.random.randint(0,4)

    show screen money_game(pval, zval, mval)
    pause
    scene night
    return


# Short explanation of the money mini-game
screen money_game_exp:
    hbox:
        spacing(20)
        text "      "
        vbox:
            box_wrap True
            spacing(40)
            text ""

            text "Each day you have a choice between three actions: sell (for immediate profit), improve (happy farm happy life), or buy (chance your best guess at future gain!)\n"

            text "Any action you make will impact not only the amount of money you have, but also the happiness of one or more elements of your farm.\n"
        
            text "The bank will take your farm away if you go bankrupt – but make sure not to neglect the creatures on your farm either.\n"

            text "Foreclosure is not the worst thing that can happen to you in Begonia Grove.\n"
        text "      "


# Money decision mini-game screen
# If user chooses plus option, add appropriate amount to money
# If user chooses zero option, adjust appropriate plus items
# If user chooses minus option, subtract appropriate amount to money + extras
screen money_game(p, z, m):
    frame:
        xalign 0.5 yalign 0.5
        xpadding 60 ypadding 60
        hbox:
            spacing 60
            vbox:
                spacing 50
                textbutton plus[p][0] xalign 0.5 yalign 0.5:
                    action [Hide("money_game"), Call("set_from_plus", p)]
                textbutton zero[z][0] xalign 0.5 yalign 0.5:
                    action [Hide("money_game"), Call("set_from_zero", z)]
                textbutton minus[m][0] xalign 0.5 yalign 0.5:
                    action [Hide("money_game"), Call("set_from_minus", m)]
            vbox:
                spacing 50
                text "$[money]" xalign 1.0 yalign 0.5
                $ chk = mood[chicken_mood]
                text "Chicken: [chk]" xalign 1.0 yalign 0.5
                $ cow = mood[cow_mood]
                text "Cow: [cow]" xalign 1.0 yalign 0.5
                $ car = mood[carrot_mood]
                text "Carrot: [car]" xalign 1.0 yalign 0.5


# Updates variable from money_game. Return to call block.
label set_from_plus(p):
    if p == 1:
        $ money += plus[p][1] * 3 * chicken_mood
    elif p == 2:
        $ money += plus[p][1] * 3 * cow_mood
    else:
        $ money += plus[p][1] * 2.5 * carrot_mood
    return

# Adjust appropriate plus amounts. If fix machine or fertilize crops, make false. Update mood.
label set_from_zero(z):
    $ plus[0][1] += zero[z][1]
    $ plus[1][1] += zero[z][2]
    $ plus[2][1] += zero[z][3]

    $ chicken_mood += zero[z][1]/5
    $ cow_mood += zero[z][2]/5
    $ carrot_mood += zero[z][3]/5

    if chicken_mood > 4:
        $ chicken_mood = 4
    if cow_mood > 4:
        $ cow_mood = 4
    if carrot_mood > 4:
        $ carrot_mood = 4

    if z == 3:
        $ zero[3][4] = False
    elif z == 4:
        $ zero[4][4] = False
    return

# If buy more chickens, egg price increased by 10
# If buy better feed, tend to livestock bonus increased by 5
# If buy new machine parts, make fix machine available
# If buy fertilizer, make fertilize crops available
label set_from_minus(m):
    $ money -= minus[m][1]
    if m == 3:
        $ plus[0][1] += 10
    elif m == 2:
        $ zero[2][1] += 5
        $ zero[2][2] += 5
    elif m == 1:
        $ zero[4][4] = True
    elif m == 0:
        $ zero[3][4] = True
    return