#for the speaking sounds (typewriter)
init python:
    import random

    type_sounds = [
        "audio/typewriter2.mp3", 
    ]

    def typing_callback(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            
            #adjust dialogue line + cps speed
            for _ in range(135):
                renpy.sound.queue(
                    random.choice(type_sounds),
                    channel = "sound",
                    loop = False
                )
        
        elif event in ("slow_done", "end"):
            #stop any still queued typing sounds when typing finishes or when player clicks to advance 
            renpy.sound.stop(channel = "sound")

        if event == "end":
            #optional: play a line finished click to continue sound
            renpy.sound.play("audio/typewriter1.mp3", channel = "sound")    


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Schell", who_color='ffffff', window_background = Frame("images/textboxschell.png"), callback = typing_callback)
define y = Character("You", who_color = 'ffffff', window_background = Frame("images/textboxyou.png"), callback = typing_callback)
define v = Character("Vladan", who_color = 'ffffff', window_background = Frame("images/barrattextovladan.png"), callback = typing_callback)
define n = Character(" ??? ", who_color = 'ffffff', window_background = Frame("images/textboxnarrador.png"), callback = typing_callback)



# The game starts here.

label start:

    stop music
    
    scene fondo1vladan
    
    show vladan2
    v "..."
    
    y "Mnnnn..."
    y "Huh?!"
    y "What...?"
    hide vladan2
    show vladan3
    v "You woke up"
    play music "audio/vladaninicioo.mp3"
    hide vladan3
    show vladan2
    v "..."
    y "I am, but...Please..."
    hide vladan2
    show vladan3
    v "Don't be scared"
    hide vladan3
    show vladan2
    y "..."
    y "Why am I here?"
    hide vladan2
    show vladan3
    v "You have been selected for the code 45590-bqn mission"
    v "You OUGHT to finish it"
    hide vladan3
    show vladan2
    y "Wait what!?"
    y "But I'm...!"
    y "I don't..."
    hide vladan2
    show vladan1
    v "YOU HAVE TO ENTER THE SPIKEBALL EVEN IF YOU DO NOT WANT IT" with vpunch
    v "YOU HAVE TO BRING US INFORMATION"
    y "Gah!"
    v "YOU UNDERSTAND?"
    y "But..."
    v "NO BUTS" with vpunch
    y "SIR I HAVEN'T EVEN FORMED A SINGLE SENTENCE"
    stop music
    hide vladan1
    show vladan2
    v "Hmmm..."
    hide vladan2
    show vladan3
    v "You are right"
    v "My apologies"
    v "Just..."
    hide vladan3
    show vladan2
    v "..."
    hide vladan2
    show vladan3
    v "Do not get too comfortable"
    hide vladan3
    show vladan2
    "You don't get why he said something about being comfortable but you just go with it"
    hide vladan2
    show vladan3
    
    v "She is the only one we have discovered until now that has origins from here."
    v "Of course she will mix knowledge from here and there"
    hide vladan3

    show vladan2
    y "Who is she?"
    y "What are you even talking about sir I CAN'T understand"

    show vladan2
    v "..."
    hide vladan2
    show vladan3
    v "Just..."
    v "Don't get discovered, because..."
    v "You can {color=#f00}die{/color}"
    play music "audio/vladaninicioo.mp3"
    hide vladan3
    show vladan2
    y "WHAT THE HELL?" with vpunch
    y "YOU TAKE ME OUT OF MY DUTIES, KNOCK ME OUT AND THEN WHEN I WAKE UP..."
    y "YOU JUST TELL ME I'M GOING TO {sc=5}DIE...?{/sc}"
    y "{sc=5}THIS ISN'T FAI-{/sc}{nw=0.3}"
    hide vladan2
    show vladan1
    v "STOP COMPLAINING" with vpunch
    v "YOU WERE THE CHOSEN ONE"
    hide vladan1
    show vladan3
    v "Don't you dare disappoint"
    hide vladan3 with dissolve
    "His voice resonates in your mind like some church bell"
    "Your conciousness starts fading..."
    
    "And you finally close your eyes...{w}Again.{w=1.0}"

    stop music

    with fade
    scene fondonegro

    $renpy.pause(5)
    n "You dumbass!!!!!"
    $renpy.pause(2)

    scene fondoo

    show spensativa
    with fade

    s "What does 'poggers' mean?"

    hide spensativa
    show strescuartos

    s "You're scary man, are you even human?"

    n "Looks like someone didn't like your comment! Try again later!"


    

    return
