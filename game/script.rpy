# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define trudy = Character("[name]")


# The game starts here.

label start:

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

        show trudy-neutral

        "Jogging always felt like the only times I could truly be free. With the music pounding in my ears and the wind flowing through my hair, I felt boundless and featherlight." 
        
        "Looking at the nicely trimmed bushes lining the sidewalk, I took a deep breath in." 
        
        "I’d always wondered how it would be like to fit in. Loneliness was more of a circumstance than a choice at this point."

        "My jogging route took me to the post office, where I rarely stopped by. I had no reason to, as I kept to myself for the most part."
        
        "The occasional package was sent to me, but nothing worth checking for."

        "Upon opening my P.O. box, I noticed a slightly crumpled letter. It was the only thing in the small box, and I gently took it out to observe it."

        # show letter

        python:
            name = renpy.input("On the envelope was my name in elegant handwriting: To ")
            name = name.strip() or "Trudie"

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
            
            "By the end of the night, all my belongings were packed and ready to go. It was time to start anew."
            
            jump chapter_one

        label choice_ignore:
            trudy "Just junk."
            
            "I tossed the letter in the trash and made my way back home."

            jump end

    label chapter_one:
        scene farm

        "As I shut the door of the taxi behind me, my thoughts raced through my mind."

        "What was the farm going to look like? What was I going to do on the farm? What was I doing? I don't know how to farm!"
                    
        "The farm was a bit of a distance from where I had been dropped off. I took in my surroundings." 
                
        "Begonias adorned every inch of the place. I supposed it was how the farm received its name."
    
        "After about 5 minutes of slow walking, I finally made it to the entrance to the farm."

        show trudy-shock
        
        "The gates creaked softly as I stepped past them, and the dirt on the ground caked around my shoes. There was an air of moodiness about the farm."
        
        "The crops seemed to sink into the ground, while the few livestock wandered around hopelessly." 
        
        "Old machinery collected dust and grime on the outskirts of the fields, broken and dilapidated."

        "I took a breath in. There was work to be done."


    label chapter_two:

    label chapter_three:

    label end:
    # This ends the game.

    return
