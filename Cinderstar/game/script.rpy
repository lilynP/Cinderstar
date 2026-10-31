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
    play music "audio/hostil.mp3" volume 2.0
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

    $renpy.pause(2)
    play music "audio/horrormusic.mp3" volume 2.0
    n "Hello :3"
    n "I think there is something you must know"
    n "Hi! I'm either your mind or a god! Nice to meet ya!"
    n "Ok so when talking to the actress, you will sometimes get an answer right out of your mouth without deciding what to say."
    n "This is me helping you and saving your dumb ahh to not ruin your mission."
    n "But sometimes..."
    n "I {b}won't{/b} be there"
    n "So keep that in mind"
    n "{b}You have to select the right answer.{/b}"
    n "Okie dokie :3 Bye bye! and good luck! She's probably complicated so take care! ^^"
    stop music
    $renpy.pause(2)

    scene fondoo

    play music "audio/normalmusic.mp3"

    show sseria
    with fade

    y "So that's what you went through to reach this?"
    s "Yes I did, of course"
    
    menu:
        "I understand":
            hide sseria
            show strescuartos
            s "Yes you must!"
            s "You are here to interview me either way"
        "You still look flawless, you know":
            hide sseria
            show strescuartos
            s "I know that"
    hide strescuartos
    show sseria
    y "So...{w}about your dressing room...{w=1.0} Can you talk some more about it?"
    hide sseria
    show spensativa
    
    jump menupreguntasprincipales

    return

label menupreguntasprincipales:
    menu:
        
        s "Well, what do you want to know about it?"
        "I want to know what you keep inside your drawers":
            stop music
            
            hide strescuartos
            hide spensativa
            show snerviosa
            
            s "That is, I must say, a creepy question indeed..."
            menu:
                "Return and ask something more normal":
                    call mybad
                    
                    jump menupreguntasprincipales
                    
                "Continue being a creep":
                    call creep
        "I want to know about the leg mannequins on the corner.":
            hide spensativa
            "En espera"
            jump menupreguntasprincipales1



label mybad:
    stop music
    play music "audio/normalmusic.mp3"
    y "You know, you're right, my bad"
    hide smikan
    hide snerviosa
    show strescuartos
    s "Yeah"
    s "Is it your first time interviewing an actress from my league?"
    s "You sure are oblivious..."
    jump menupreguntasprincipales
    return
    

label creep:
    play music "audio/horrormusic.mp3" volume 2.0
    y "You think? Because I just feel curiosity towards you and I want to know."
    hide snerviosa
    show smikan
    s "You think the press will want to know what I keep inside these?"
    s "By the way, shouldn't you be asking real questions instead of random bullshit?"
    menu:
        "{sc=5}JUST TELL ME ALREADY{/sc}":
            play sound "audio/wrong.wav"
            hide smikan
            show smolestadaminimamente
            s "You know damn well that us actresses don't ask for press interview yet you still invade my privacy."
            menu:
                "{b}It's just a simple question, why the frown?{/b}":
                    play sound "audio/wrong.wav"
                    s "..."
                    s "{sc=5}Really...?{/sc}"
                    hide smolestadaminimamente
                    show smolestaojoabierto with vpunch
                    s "The first question you ask is this and not look at my achievements?"
                    s "my {sc=5}BEAUTIFUL{/sc} dressing room, {sc=5}BEAUTIFUL{/sc} {b}ME{/b}?"
                    hide smolestaojoabierto
                    show smolestaojocerrado with vpunch
                    s "There are millions of questions you can ask being a professional interviewer..."
                    s "...yet you only arouse anger and resentment inside me..."
                    hide smolestaojocerrado
                    show smolestadaminimamente
                    s "..."
                    s "..."
                    s "You know what,{w} just {b}leave{/b} already{w=1.0}"
                    s "I hate you."
                    hide smolestadaminimamente
                    show smolestaojoabierto with vpunch
                    s "I HATE YOUR JOB"
                    s "I HOPE YOU WOULD JUST ROT ALIVE AS A DECOMPOSING CADAVER DOES INSIDE A PIT OF BURNT BOD-{nw=0.3}"
                    hide smolestaojoabierto
                    show scouch with hpunch
                    play sound "audio/cuerdas.mp3"
                    $renpy.pause(1)
                    hide scouch
                    show scararota with dissolve
                    s "..."
                    s "..."
                    s "..."
                    s "...ouch"
                    hide scararota
                    show scararotanerviosa
                    s "Just {b}GO{/b} now."
                    s "I don't want to see you."
                    hide scararotanerviosa
                    scene fondonegro
                    play sound "audio/puerta.wav"
                    n "You already ruined it all."
                    n "Don't bother going up to him again"
                    $renpy.full_restart()

                "You know, you're right, my bad":
                    hide smolestadaminimamente
                    
                    call mybad

        
        "You know, you're right, my bad.":
            stop music
            play music "audio/normalmusic.mp3"
            call mybad
            jump menupreguntasprincipales
    return