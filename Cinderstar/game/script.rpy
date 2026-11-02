#for the faded or non hovered secret or hidden option for the dialogues
default reloj_desbloqueado = False
#for avoiding asking the same question all over again
default maniquies = False

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

image fuegomovil = Movie(size=(2800,1100), channel = "movie", play = "images/fueguito.webm")

# The game starts here.

label start:

    stop music
    
    play music "audio/schellinicio.mp3"

    scene fuegomovil with dissolve
    "I could not remember I was alive."
    "I do not remember how I looked like,"
    scene fuego3 with fade
    "and I will never remember who I was by the time I was a nobody."
    scene foto with fade
    "I would have never thought how ephemeral my life could be."
    "If the meaning of the end of my life would be briefed to one of my dad's quotes:"
    scene fotofuego with fade
    "'The world ends when we die'"
    scene cenizas with fade
    "Or if in reality, I was just a myriad of ashes,"
    scene manoalzandose with fade
    "Floating on the firmament of infinity;"
    "the firmament that looked back at me while my remains of my body were burning to death."
    scene manocerrandose with fade
    "That was probably the first time I could enjoy with my hands the star sprinkled sky I longed to reach and touch ever since I was a kid."
    scene aquamarinespiders with dissolve
    "Why would I even think some aquamarine spiders would save me from my imminent death?"

    stop music fadeout 2.0

    scene fondonegro with fade
    $renpy.pause(3)



    scene fondo1vladan with eyesopen 
    with dissolve
    
    show vladan2 with fade
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
    with eyesclose

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
    hide sseria
    hide strescuartos
    hide smikan
    show spensativa
    s "Well, what do you want to know about it?"

    call screen menu_reloj


label drawers:
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

label menupreguntasprincipales1:
    hide spensativa
    show soh
    s "Oh these?"
    hide soh
    show spensativa
    s "They were commissioned by Marcel after we prepared for an audition"
    menu:
        "What audition? Tell me about it":
            hide spensativa
            show soh
            s "Oh!"
            s "You remember 'Stockings more like gloves' right?"
            hide soh
            show spensativa
            s "I wasn't the main actress because of my physique and the director wanted someone way more..."
            hide spensativa
            show skidding
            s "Different? but capable"
            hide skidding
            show sseria
            y "Weren't you ashamed of yourself because of that?"
            s "About what?"
            s "The fact that they didn't let me be the main actress?"
            y "Yeah, don't have the need to be the main actress at all times?"
            hide sseria
            show skidding
            s "Oh no! Not really!"
            s "I mean I like to be the image of the play but it can become tiring you know?"
            hide skidding
            show sseria
            y "I see..."
            jump lightbulb
        "Who is Marcel?":
            hide spensativa
            show sjuzgona 
            s "So you haven't researched enough about me, right?"
            menu:
                "I promise I have! I am just forgetful!":
                    hide sjuzgona
                    show skidding
                    s "Are you kidding me? He was literally my closest colleage when acting for 'The lightbulb'."
                    menu:
                        "What's 'The lightbulb'?":
                            hide skidding
                            show sseria
                            s "One. of. my. most. famous. plays."
                            hide sseria
                            show skidding
                            s "Are you really an interviewer? Journalist, whatever you are?"
                            y "I swear I am! I am sorry!"
                            hide skidding
                            show strescuartos
                            s "Just because you say sorry doesn't mean that I have to forgive you."
                            y "..."
                            n "Oh?"
                            hide strescuartos
                            show ssonriente
                            s "Just kidding!"
                            s "..."
                            s "..."
                            s "Haha I'm a real good humorist am I?"
                            menu:
                                "Yes. you got me there for a sec.":

                                    jump lightbulb
                                "...No?":
                                    hide ssonriente
                                    show snerviosa
                                    $renpy.pause(2)
                                    jump lightbulb
                        "OOH I remember now, sorry!":
                            y "Sorry! I tend to forget things out of nowhere...my apologies...!"
                            hide skidding
                            show smikan
                            s "Oh okay."
                            s "Then let's keep going"
                            $renpy.pause(2)
                            stop music
                            play music "audio/horrormusic.mp3" volume 2.0
                            n "WHY ARE YOU EVEN PLAYING" with vpunch
                            n "You know, you just chose the boring path now."
                            n "The game will be shorter than you expected."
                            n "And it will probably make zero sense to you now."
                            n "Your interview will be LAMEEEE as hell right now LMAO"
                            stop music
                            play music "audio/normalmusic.mp3"
                            $reloj_desbloqueado = True
                            jump menupreguntasprincipales
                "No, I have not":
                    hide sjuzgona
                    show strescuartos
                    s "It shows."
                    hide strescuartos
                    show snerviosa
                    $renpy.pause(2)
                    n "That 2 second pause was her being uncomfortable with a presence that is SUPPOSED to make her comfortable with fun questions."
                    s "So..."
                    n "She's probably gonna ask something to keep the conversation"
                    n "I knew you were bad at this, but you are BAD BAD"
                    jump lightbulb



label lightbulb:
    
    hide snerviosa
    hide sseria
    show ssonriente
    s "Anyways, do you want me to demonstrate you a bit of 'The lightbulb'?"
    menu:
        "Yes sure! Tell me about it.":
            jump lightbulbdemos
        "...Ok?":
            hide ssonriente
            show strescuartos
            s "What do you mean '...Ok?' I will tell you about it anyways."
            jump lightbulbdemos


label lightbulbdemos:
    hide ssonriente
    hide strescuartos
    show skidding
    s "Ok so the drill rings, right?"
    hide skidding
    show sgrin
    s "The play is about to start, and Marcel and I appear together."
    s "The set is a half empty house with a clock on the wall, that doesn't tick by the way,"
    s "a table on the center of the set, a lightbulb hanging on the table, that ALSO doesn't work,"
    s "a door drawn with a crayon, and a chair, just there."
    hide sgrin
    show ssonriente
    s "I go, and from the lines I remember I exclaim 'It's empty'."
    hide ssonriente
    show sdisgusto
    s "then, Marcel, well, Marcel with that stupid role of a stupid man, comes to me walking backwards like some beep boop robot, and asks me:"
    hide sdisgusto
    show sexplicando1
    s "'The cup?' so I yell at him saying:"
    hide sexplicando1
    show smolestaojoabierto with vpunch
    s "'NO, NOT THE CUP!! MY SOUL! IT'S EMPTY! HAVEN'T YOU REALIZED AFTER ALL THESE YEARS?!"
    hide smolestaojoabierto 
    show sbrazoscruzados
    s "But yes, also the cup'"
    hide sbrazoscruzados
    show ssonriente
    menu:
        s "It's so funny isn't it? The punchline."
        "I don't think that was funny at all...":
            hide ssonriente
            stop music
            
            show sjuzgona
            s "Huh? Why?"
            y "You know, the Marcel guy entering the scene, and everything...It's absurd..."
            hide sjuzgona
            show sdisgusto
            s "Oh heavens..."
            hide sdisgusto
            show skidding
            s "Do you forget where you are?"
            s "You must be a big fleshy deal!"
            menu:
                "Hey that's enough uhhh let's just stick to the first question, ok?":
                    hide skidding
                    show sseria
                    y "So umm..."
                    hide sseria
                    play music "audio/normalmusic.mp3"
                    $reloj_desbloqueado = True
                    jump menupreguntasprincipales
                "I kinda am.":
                    hide skidding
                    show sbrazoscruzados
                    play sound "audio/wrong.wav"
                    s "What did you say?"
                    y "Nah, nothing."
                    s "..."
                    s "..."
                    hide sbrazoscruzados
                    play music "audio/normalmusic.mp3"
                    $reloj_desbloqueado = True
                    jump menupreguntasprincipales
        "Mmhmm!":
            play sound "audio/correct.wav" volume 0.5
            hide ssonriente
            show sexplicando1
            s "Yeah! So I keep reproaching him because he makes dumb comments and yadda yadda"
            hide sexplicando1
            show skidding
            s "I tell him he has 'filled up' my life with forgetfullness, and I just can't drink it you know?"
            hide skidding
            show sexplicando1
            s "He asks 'What do you want me to do to fix it?' and I break into tears, yelling:"
            ###NO OLVIDAR###
            #aqui tiene que haber un sprite de schell como llorando actoralmente, puede ser o una escena o un sprite
            # "Nothing, haven't you realized the light above us doesn't work anymore? It consumes energy!! Our soul!!
            #It turns life into a lightless realm. Just look at me...Do you see me as the person you met 10 years ago at the cafe?"






label relojenlapared:
    "en espera wait wait 1"
    return

label maniquies:
    if maniquies:
        hide spensativa
        show snerviosa
        s "Wait...didn't you already ask me about those?"
        hide snerviosa
        show skidding
        s "Are you even paying attention to our conversation"
        y "I...uh..."
        hide skidding
        show strescuartos
        s "Move on already."
        hide strescuartos
        jump menupreguntasprincipales
    else:
        $maniquies = True
        jump menupreguntasprincipales1

