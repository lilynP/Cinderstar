#for the faded or non hovered secret or hidden option for the dialogues
default reloj_desbloqueado = False
#for avoiding asking the same question all over again
default maniquies = False
default pdrawers = False

#for the notify and new findings############
default directorr = False
default concordia = False
default brujas = False
default marcel = False
default normal = False
default johncage = False
default pestanas = False
default competitividad = False
default efectivamente = False
default scripts = False
default relojes11 = False
default thequeen = False
default god = False
default father = False

#and its credit score
default points = 0

########################################################

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

#for the notify thing on the top left
init python:
    def notificar(pista_texto):
        renpy.notify("New finding! " + pista_texto)

# for the content warning

label before_main_menu:

    scene black with Pause(1)

    show text _("A story by Ramelden") at truecenter with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    

    if not persistent.shown_warning:
        
        $ persistent.shown_warning = True
        call screen content_warning with dissolve

    return

#for the language selection

label splashscreen:
    if not persistent.language_chosen:
        call screen language_choice
    return


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Schell", who_color='ffffff', window_background = Frame("images/textboxschell.png"), callback = typing_callback)
define y = Character("You", who_color = 'ffffff', window_background = Frame("images/textboxyou.png"), callback = typing_callback)
define v = Character("Vladan", who_color = 'ffffff', window_background = Frame("images/barrattextovladan.png"), callback = typing_callback)
define n = Character(" ??? ", who_color = 'ffffff', window_background = Frame("images/textboxnarrador.png"), callback = typing_callback)
define chicas = "?"
define c = DynamicCharacter("chicas", who_color = 'ffffff', what_color = '3E424B', window_background = Frame("images/textboxcc.png"), callback = typing_callback )

image fuegomovil = Movie(size=(2800,1100), channel = "movie", play = "images/fueguito.webm")
image reina = Movie(size=(1920,1080), channel = "movie", play = "images/reina.webm")
image sangre = Movie(size=(1920,1080), channel = "movie", play = "images/sangre.webm")

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
    play music "audio/hostil.mp3" volume 3.0
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
    play music "audio/vladaninicioo.mp3" volume 2.0
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
    hide sexplicando1
    show spensativa
    s "Well, what do you want to know about it?"

    call screen menu_reloj


label askdrawers:
    if pdrawers:
        hide spensativa
        show strescuartos
        s "Haven't you already asked me about my drawers?"
        hide strescuartos
        show skidding
        s "Can you even focus on the interview?"
        s "I think it's clear that I won't open them for you."
        hide skidding
        jump menupreguntasprincipales
    else:
        $pdrawers = True
        jump drawers
    

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
            play sound "audio/wrong.mp3"
            hide smikan
            show smolestadaminimamente
            s "You know damn well that us actresses don't ask for press interview yet you still invade my privacy."
            menu:
                "{b}It's just a simple question, why the frown?{/b}":
                    play sound "audio/wrong.mp3"
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
            hide sseria
            show spensativa
            s "About what?"
            s "The fact that they didn't let me be the main actress?"
            y "Yeah, don't have the need to be the main actress at all times?"
            hide spensativa
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
    s "Ok so the bell rings, right?"
    hide skidding
    show sgrin
    s "The play is about to start, and Marcel and I appear together."
    $marcel = True
    $notificar("Actor's name")
    s "The set is a half empty house with a clock on the wall, that doesn't tick by the way,"
    s "A table on the center of the set, a lightbulb hanging on the table, that ALSO doesn't work,"
    s "A door drawn with a crayon, and a chair, just there."
    hide sgrin
    show ssonriente
    s "I go, and from the lines I remember I exclaim 'It's empty'."
    hide ssonriente
    show sdisgusto
    s "then, Marcel, well, Marcel with that {b}stupid{/b} role of a {b}stupid{/b} man, comes to me walking backwards like some beeping robot, and asks me:"
    hide sdisgusto
    show sexplicando1
    s "'The cup?' so I yell at him saying:"
    hide sexplicando1
    show smolestaojoabierto with vpunch
    s "'NO, NOT THE CUP!! MY SOUL! IT'S EMPTY! HAVEN'T YOU REALIZED AFTER ALL THESE YEARS?!"
    hide smolestaojoabierto 
    show sbrazoscruzados
    s "But yes, also the cup'"
    $normal = True
    $notificar("Peculiar plays")
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
                    play sound "audio/wrong.mp3"
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
            hide sexplicando1
            scene escena1 with fade
            s "'Nothing.'"
            s "'Haven't you realized the light above us doesn't work anymore?'"
            s "'It consumes energy!! Our soul!! It turns life into a lightless realm.'"
            s "'Just look at me...'"
            s "'Do you see me as the person you met 10 years ago at the cafe?'"
        
            menu:
                "So...what you just mentioned...'The light above us doesn't work anymore' Has it happened to you before?":
                    y "I mean, feeling 'lightless' after a play or..."
                    y "Something that consumes you without you having the possibility to do something about it?"
                    scene fondoo
                    show sexplicando1
                    s "Probably...Back when I was still a small actress and everything was so consuming!"
                    s "I still remember when I couldn't remember the scripts as fast as I remember them nowadays..."
                    hide sexplicando1
                    show sseria
                    y "What was the hardest script you have ever been given?"
                    hide sseria
                    show skidding
                    s "So here at Concordia we have many directors you know?"
                    $concordia = True
                    $notificar("Theater name")
                    hide skidding
                    show smikan
                    s "But the problem here is that the scripts are weird, but dream like {sc=5} WEIRD {/sc}"
                    s "You ever dreamed you were a woman daubed in squid oil, running around the city, screaming and nobody turning to look at you?"
                    s "But everything is screamed in a language you have never heard of but you know for some reason?"
                    hide smikan
                    show sbrazoscruzados
                    s "Yeah, that level of weird."
                    s "The 'I can't control this' level of weird."
                    hide sbrazoscruzados
                    show sgrin
                    y "I have never heard of that kind of dreams before, but they do sound interesting!"
                    s "So, the scripts work some way the same as a dream, but just the scripts from Mr Menschsein as far I have seen."
                    
                    hide sgrin
                    show ssonriente
                    s "Quite ironic though."
                    y "Didn't Menschsein mean 'being human' in german? Sorry to interrupt..."
                    $directorr = True
                    $notificar("Director's name")
                    hide ssonriente
                    show spensativa
                    s "Yes, but it is a language I haven't heard in so much time, because here at Concordia not many use it."
                    menu: 
                        "Yeah, haven't heard of it around here either...Just in books from the library...":
                            hide spensativa
                            show soh
                            s "Yes, me too..."
                            hide soh
                            show sgrin
                            y "Do you often head to the library?"
                            hide sgrin
                            show ssonriente
                            play sound "audio/correct.wav" volume 0.5
                            s "Yes I do! I try to look for some some books about biology or some mythical facts!"
                            s "They are fun to read in the meantime and help me concentrate better."
                            y "How do you concentrate better?"
                            hide ssonriente
                            show sgrin
                            s "You know, haven't you ever read a book and thought...'Wow! I feel much clearer now!'?"
                            y "Probably, why?"
                            hide sgrin
                            show spensativa
                            s "That's probably what I felt."
                            s "Did you know some witches are depicted with a reversed broom?"
                            $brujas = True
                            $notificar("Depiction of witches")
                            hide spensativa
                            show sexplicando1
                            s "It's awesome how some books lie to us..."
                            y "Yeah haha..."
                            hide sexplicando
                            $reloj_desbloqueado = True
                            jump menupreguntasprincipales
                        "But it is a well known language...!":
                            play sound "audio/wrong.mp3"
                            stop music
                            hide spensativa
                            show sbrazoscruzados
                            s "Sorry, what?"
                            menu: 
                                "Oh nothing":
                                    s "Hmmm..."
                                "It's just that I knew before she brought me here":
                                    s "'She'?"
                            n "She's already suspicious of you, just say 'nothing'"
                            y "Yep, nothing! So what scripts did you want to mention?"
                            y "Sorry, we took a little detour didn't we?"
                            hide sbrazoscruzados
                            show sincomoda
                            s "Yeah we did haha..."
                            hide sincomoda
                            show spensativa
                            s "So I might say there were three scripts that really caught me off guard..."
                            y "What were they?"

                            hide spensativa
                            play music "audio/normalmusic2.mp3"
                            
                            
                            #opcional: lo mismo que sguion pero con la vista ahora desde arriba
                            scene sguion
                            s "So the first one was my first ever script, in which I would 'forget' everything I read..."
                            s "But it wasn't actually me forgetting the lines."
                            s "It was actually the script changing everytime I memorized it..."
                            s "As if it KNEW that I was trying to memorize it."
                            scene sguion1
                            s "It gave me a breakdown because the director wanted it to be due in less than a week, I think?"
                            s "And the script wouldn't help."
                            s "Turns out it was on purpose and it was a 'creative' added value to the story."
                            s "Still, regardless of the creativity, I did NOT like it at all."
                            y "You mean the script or the added value?"
                            s "Both, I couldn't handle none of them, but I wouldn't quit because of that..."
                            scene fondoo
                            show sseria
                            y "Now tell me about the second and third one...I'm curious."
                            hide sseria
                            show spensativa
                            s "Ok so..."
                            hide spensativa
                            scene sguion
                            s "The second one was just straight up boring."
                            s "It was just 200 blank pages."
                            s "Mr. Menschsein said that I had to express it with my look, but you know?"
                            s "Each page is at least one minute of play."
                            s "So, 200 pages would mean around 3,33 hours!"
                            s "Just staying silent and expressing whatever he wanted me to try to express with only my eyes..."
                            s "I know I am sometimes quiet and I enjoy the silence, but this one was too much."
                            s "The script ONLY contained sticky notes to express certain 'feelings' with my eyes."
                            s "It was awful still."
                            y "Reminds me of a music piece from a certain someone..."
                            $johncage = True
                            $notificar("Jhonnas Craige")
                            s "ME TOO! But copyright is a thing right?"
                            s "You think you can cut that from the recording right?"
                            y "Yes sure, this isn't live."
                            y "Yet."
                            scene fondonegro with fade
                            $renpy.pause(1)
                            n "While you cut your footage let me point out something."
                            n "Did you notice?"
                            n "She knows Jhonnas Craige!"
                            n "Can't even say his real name because Ramelden can get sued."
                            n "The agent told you about the fact that she has origins from planet Earth right?"
                            n "This is JUUUICY information!"
                            n "Ok ok just keep cropping the footage."
                            scene fondoo
                            show smikan
                            y "And...Done!"
                            y "Nobody can hear what you just said."
                            hide smikan
                            show ssonriente
                            s "Thanks! Ok so moving on to the third one..."
                            hide ssonriente
                            show spensativa
                            s "It had impossible didascalies..."
                            y "Like which ones?"
                            s "You ever heard someone say 'go down upstairs' or viceversa?"
                            y "Yes. But only in spanish. Like uhhh, 'subir abajo', like that?"
                            hide spensativa
                            show sexplicando1
                            s "Yes, that script had a lot of those."
                            s "It was very confusing, but not hard."
                            $scripts = True
                            $notificar("Abnormal scripts")
                            s "This one probably gave me the less mental pain from the three I wanted to mention."
                            hide sexplicando1
                            show sseria
                            y "Was this one also written by Mr. Menschsein?"
                            s "Yes..."
                            y "Do you have any comments on him that you want to share?"
                            hide sseria
                            show spensativa
                            s "Not really..."
                            hide spensativa
                            show soh
                            s "He's actually amazing, but his creative process is sometimes questionable."
                            hide soh
                            show ssonriente
                            s "Still, it has good results in the end, that's what matters to me."
                            s "That's why he is what he is right now mmhm."
                            y "Alright then, so..."
                            y "Keeping up with the main question..."
                            hide ssonriente
                            show soh
                            s "Oh true!"
                            stop music
                            play music "audio/normalmusic.mp3"
                            $reloj_desbloqueado = True
                            jump menupreguntasprincipales




                "So what you are telling me until now is that 'The lightbulb's concept is forgetfullness and the fallout of love between a couple, right?":
                    scene fondoo
                    show ssonriente
                    s "Yes! You got it!"
                    y "Hmmm"
                    y "So why is its name 'The lightbulb'?"
                    hide ssonriente
                    show sgrin
                    s "Oh that's because you haven't heard the ending yet..."
                    s "So Marcel just says 'I am looking at you..."
                    hide sgrin
                    show sexplicando1
                    s "And I just follow him you know?"
                    hide sexplicando1
                    show sdisgusto
                    s "And he says, 'And...You have an eyelash on you cheek'"
                    hide sdisgusto
                    show smolestaojoabierto with vpunch
                    s "SO I JUST CRASH OUT YOU KNOW?"
                    hide smolestaojoabierto
                    show sdisgusto
                    s "I yell at him again saying that I don't even have eyelashes, that these are drawn..."
                    menu:
                        "Wait, you don't have eyelashes?":
                            s "Sigh."
                            $pestanas = True
                            $notificar("She isn't a common person")
                            play sound "audio/wrong.mp3"
                            y "Sorry if that uncomfortable! My apologies..."
                            stop music fadeout 2.0
                            
                            s "It's not that...It's just..."
                            s "It makes me remember that I am nothing without..."
                            s "All this."
                            play music "audio/normalmusic2.mp3"
                            hide sdisgusto
                            show sincomoda
                            y "What do you mean 'nothing'?"
                            hide sincomoda
                            show snerviosa
                            s "It's complicated, but you don't have to worry about it!"
                            hide snerviosa
                            show sincomoda
                            y "So, what's the background?"
                            s "So, you know, haha..."
                            s "This isn't my real body!"
                            hide sincomoda
                            show snerviosa
                            s "Everything you see was tailored and sewn to my size."
                            play sound "audio/wrong.mp3"
                            y "So you have had surgery?" with vpunch
                            
                            s "Kind of."
                            hide snerviosa
                            show sincomoda
                            s "Next question please..."
                            hide sincomoda
                            stop music fadeout 2.0
                            play music "audio/normalmusic.mp3" fadein 2.0
                            $reloj_desbloqueado = True
                            jump menupreguntasprincipales

                        "That was another one, right? Sorry, just keep going...":
                            hide sdisgusto
                            play sound "audio/correct.wav" volume 0.5
                            show sexplicando1
                            s "Yes."
                            s "Then we start to question the one who wrote us and the scene around us."
                            s "Like the broken lightbulb! And I just yell that I feel judged, by everything around us."
                            hide sexplicando1
                            show sgrin
                            s "After all that, Marcel just says 'I forgot my lines'."
                            hide sgrin
                            show ssonriente
                            s "It was so funny!"
                            s "I thought that was an improvisation but that was actually on the script!"
                            hide ssonriente
                            show skidding
                            s "We are supposed to be absurd but not forgetful you know?"
                            hide skidding
                            show ssonriente
                            s "So I just replied with my famous line:"
                            s "'You never had anything to say.'"
                            menu: 
                                "Is that supposed to be famous?":
                                    play sound "audio/wrong.mp3"
                                    stop music
                                    hide ssonriente
                                    show skidding
                                    s "Huh? Of course?"
                                    hide skidding
                                    show sseria
                                    s "It's peak comedy here at Concordia."
                                    hide sseria
                                    show skidding
                                    s "Are you telling me you are some kind of meathead?"
                                    menu:
                                        "{sc=5}What even is Concordia?{/sc}":
                                            play sound "audio/wrong.mp3"
                                            play music "audio/horrormusic.mp3" volume 2.0
                                            hide skidding
                                            show smikan at center, constant_shake
                                            s "So you are not from here?"
                                            y "W-wait! I can explain! I just have bad memory you know?"
                                            s "No..."
                                            hide smikan
                                            show smolestadaminimamente at center, constant_shake
                                            s "That's not just 'bad memory' if you live somewhere, you must know the name of the place you are living in right?"
                                            s "AT LEAST the planet you live in."
                                            s "If you are not from here you must know this place by the name 'Spikeball', right?"
                                            hide smolestadaminimamente
                                            show sjuzgona
                                            s "And you must be a filthy spook, a bloody backstabbing fraud."
                                            y "I swear! I am not a spy! You have to believe me!"
                                            s "I don't think that's true huh."
                                            s "Just look at your hands, they are sweating."
                                            hide sjuzgona
                                            show sdisgusto
                                            s "Ugh, I hate bad liars."
                                            s "And by the way, I never said the word 'spy'."
                                            s "You just fell inside your own trap."
                                            y "I am not-!{nw=0.2}" with vpunch
                                            
                                            scene fondonegro
                                            $renpy.pause(1)
                                            stop music fadeout 2.0
                                            play audio "audio/reina.mp3"
                                            
                                            play movie "images/reina.webm"
                                            $ renpy.pause(5, hard=True)
                                            pause 5

                                            $renpy.pause(2)
                                            $renpy.block_rollback()
                                            n "Oopsie"
                                            
                                            $renpy.full_restart()


                                        "I'm just kidding with you ma'am, it's just, you know? I am a little different.":
                                            #FALTA SPRITE COMO VLADAN MOLESTO PERO CON SCHELL SERIA
                                            hide skidding
                                            show svladan
                                            play music "audio/horrormusic.mp3" volume 2.0
                                            s "Why are you different?" 
                                            s "Do you happen to have had a sad backstory?"
                                            s "A malformation from birth?"
                                            s "A superpower?"
                                            s "A talent better than anyone else here at the theatre?"
                                            s "A talent better than mine?"
                                            $competitividad = True
                                            $notificar("Competition?")
                                            s "A disability?"
                                            s "Why?"
                                            s "{sc=5}Why are you different?{/sc}"
                                            s "Huh."
                                            s "Or perhaps..."
                                            s "{sc=5}Are you a traveler from the other ground?{/sc}"
                                            n "You don't have to answer her."
                                            n "Everyone is different in their own way!! <3"
                                            n "Don't listen to her."
                                            n "Here, answer her this:"
                                            y "My apologies I tried to get into your life, but this feels way too personal. Can I ask you other questions?"
                                            hide svladan
                                            show sjuzgona
                                            s "Fuah, sure."
                                            hide sjuzgona
                                            stop music
                                            play music "audio/normalmusic.mp3"
                                            $reloj_desbloqueado = True
                                            jump menupreguntasprincipales

                                "Ohh, now I can see where you are going":
                                    s "As you may"
                                    hide ssonriente
                                    #se le rompe la cara
                                    stop music fadeout 2.0
                                    play music "audio/normalmusic2.mp3" fadein 1.0
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
                                    $renpy.pause(1)
                                    hide scararotanerviosa
                                    scene fondonegro
                                    play sound "audio/coser.mp3"
                                    $renpy.pause(2)
                                    scene fondoo
                                    show sincomoda
                                    s "Sorry, this must have been kind of annoying."
                                    y "Not really."
                                    $efectivamente = True
                                    $notificar("You're right, she isn't normal")
                                    y "It's just a part of you and it's amazing to see the other faces of people."
                                    hide sincomoda
                                    show smikan
                                    play sound "audio/correct.wav" volume 0.5
                                    s "That sound beautiful"
                                    y "Mhm!...So...Keeping up with the stuff in your dressing room..."
                                    stop music fadeout 1.0
                                    play music "audio/normalmusic.mp3" fadein 1.0
                                    $reloj_desbloqueado = True
                                    jump menupreguntasprincipales
 

            $reloj_desbloqueado = True
            jump menupreguntasprincipales


label relojenlapared:
    s "Which one? This?"
    stop music fadeout 2.0
    play music "audio/normalmusic2.mp3" 
    hide spensativa
    scene reloj with fade
    y "Yes, that one, why did you decide to use that specific clock?"
    $relojes11 = True
    $notificar("11 o'clock")
    s "I think it represents my eyes perfectly."
    y "Hmmm..."
    y "You may be right."
    y "But why that design?"
    s "Well, I like ballerinas a lot."
    s "I used to practice ballet back when I was a child."
    s "That's the only vivid memory I have from when I was a youngster."
    s "But, now I just can't you know?"
    menu:
        "I want to ask you about the time...Why is it all 11s?":
            scene fondoo
            show skidding
            s "Do you even have a clock in your house?"
            menu:
                "I never knew how to read it. That's why I brought a sand timer with me.":
                    hide skidding
                    show soh
                    s "Woo..."
                    s "Old fashioned."
                    y "Yes, I like to bring it around and look at it. So I don't have to look at the clock!"
                    y "I have a timer for 1, 5 and 10 minutes."
                    hide soh
                    show ssonriente
                    s "Ah that's nice."
                "I do have a clock, it's just that I never look at the time haha...":
                    hide skidding
                    show sdisgusto
                    s "Then how do you tell what time it is? Aren't you a professional?"
                    y "Yes I am, but my school never taught me these...I am so sorry..."
                    hide sdisgusto
                    show strescuartos
                    s "Anyway."
                    s "This interview is about me so I couldn't care less."
            y "Yeah so tell me, why are all of the numbers 11s?"
            hide strescuartos
            hide ssonriente
            show soh
            s "Oh so you don't know?"
            s "The queen actually made this system since she dreamed of it."
            $thequeen = True
            $notificar("Queen?")
            
            hide soh
            show skidding
            s "She told me it all started when she was a child, but she implemented it until now."
            hide skidding
            show sdisgusto
            s "It's still confusing to look at you know?"
            hide sdisgusto
            show sexplicando1
            s "But just imagine a regular clock, having the same numbers but just replaced with an eleven."
            hide sexplicando1
            show sseria
            y "Oh so that's why, Yeah, I think I can manage it...But what happens when you tell the time?"
            y "Is it just 'Hey, it's 11:11, time for a break'?"
            hide sseria
            show spensativa
            s "Yes I guess, you just get used to it. Some people tend to point with their finger at the time so they don't get confused."
            s "They still don't know they are confused, it's an habit taken as normal..."
            hide spensativa
            show sseria
            y "So you don't think it's a normal thing to do?"
            hide sseria
            show spensativa
            s "Not really...I respect the queen and all but this method of her has confused me since it became a rule..."
            hide spensativa
            show sseria
            y "Yeah but don't feel like that!"
            y "You might learn how to read it well sometime soon. Just wait."
            hide sseria
            show ssonriente
            "Hey! Schell had a nice feeling about you! That happens not so often. Congrats!"
            n "But HEY HEY HEYYY!!!!" with vpunch
            n "EXCUSE ME, WHY ARE YOU TWO TALKING LIKE TWO FRIENDS?!?!!?"
            jump resumen

        "I want to ask you about the eye.":
            scene fondoo
            show sseria
            y "Wouldn't you think it's a bit creepy to look at?"
            y "Or...Have the feeling someone is watching you at all times?"
            hide sseria
            show spensativa
            s "It's not creepy at all...It's beautiful actually."
            y "Why do you think that?"
            s "I don't know, I like the feeling of being watched. Specially by that eye."
            hide spensativa
            show sseria
            y "Do you think it gives you a pleasant feeling?"
            s "It's god."
            hide sseria
            show ssonriente
            s "God sees us everyday."
            $god = True
            $notificar("God?")
            y "Don't you feel controled by it?"
            s "Oh not at all! I like the fact it is looking at me! It even has my eyes."
            menu:
                "And the ballerina?":
                    hide ssonriente
                    show sdisgusto
                    s "We already talked about that I think."
                    y "I know but, I want to know why does she specifically look like that."
                    hide sdisgusto
                    show spensativa
                    stop music fadeout 2.0
                    play music "audio/abandonado.mp3" fadein 2.0
                    s "I think to recreate how I used to look like when I was younger I guess..."
                    y "How come? Have you changed a lot?"
                    hide spensativa
                    show sseria
                    s "Father says I have, and a lot."
                    y "How?"
                    y "Can I {b}see{/b}?"
                    hide sseria
                    show sincomoda
                    s "..."
                    hide sincomoda
                    
                    scene smascara with fade
                    $renpy.pause(1)
                    scene smascara1 with fade
                    $renpy.pause(1)
                    scene fondonegro with fade
                    play sound "audio/coser.mp3"
                    $renpy.pause(1)
                    scene smascara2 with fade
                    
                    s "Do I still look pretty to you?"
                    menu:
                        "{sc=5}You never looked pretty to me in the first place.{/sc}":
                            stop music
                            $renpy.block_rollback()
                            play music "audio/horrormusic.mp3" volume 2.0 fadein 2.0
                            s "..."
                            s "..."
                            s "..."
                            s "..."
                            s "Leave."
                            s "Please."
                            s "{sc=5}LEAVE NOW.{/sc}" with vpunch

                            scene fondonegro
                            stop music
                            play music "audio/abandonado.mp3"
                            play sound "audio/puerta.wav"
                            $renpy.pause(1)
                            scene fondocc
                            play sound "audio/paso.wav"
                            $renpy.pause(1)
                            scene fondocczoom
                            play sound "audio/paso.wav"
                            $renpy.pause(1)
                            scene fondocczoom1
                            play sound "audio/paso.wav"
                            $renpy.pause(1)
                            scene fondocc with fade

                            show ccsorpresa with fade
                            c "Hey! Watch out!" with vpunch
                            c "Wait...Who are you?"
                            "You freak out because you have never seen a siamese girl before."
                            "Just don't show it please. It's rude"
                            $chicas = "Siameses"
                            y "Hello miss...?"
                            c "Chirrel! and Cherryl!"
                            y "Hi misses...So I was trying to interview Schell but I made her upset haha..."
                            y "(What am I even doing?)"
                            hide ccsorpresa
                            show cclying
                            c "Did you say something about her beauty?"
                            menu:
                                "Yes":
                                    hide cclying
                                    show ccconfunsion
                                    c "Do they even know how to treat a girl like her? Like yes yes..."
                                "No":
                                    hide cclying
                                    show ccwow
                                    c "Hmm, that's weird, it even looks like..."
                                    hide ccwow
                                    show cclying
                                    c "YOU'RE LYINGGGG" with vpunch
                            y "OK I DIDN'T MEAN TO!" with vpunch
                            y "I was trying to be honest with her!"
                            y "The conversation went so good I didn't think I would say that..."
                            hide cclying
                            hide ccconfunsion
                            show ccconfunsion
                            c "You really don't know how to handle girls right?"
                            c "What did you even say to her?"
                            y "So she took off her mask and-{nw=0.3}"
                            hide ccconfunsion
                            show ccwow
                            c "WAIT FOR REAL?" with vpunch
                            c "SHE TOOK OFF HER MASK?"
                            c "Do you even know what you just achieved?"
                            y "Not really..."
                            n "What do you mean you don't know?"
                            n "We were trying to get information from her you dumbass."
                            hide ccwow
                            show cclover
                            c "ARE YOU SURE YOU AREN'T HER LOVER OR SOMETHING!?"
                            c "Hhahshsajdahsd SCHELL HAS A LOVER!! SCHELL HAS A LOVER!!{nw=0.3}"
                            y "N-NO!!!!!" with vpunch
                            y "WE ARE NOT LOVERS!!"
                            c "Do you think there's something I can do to help?"
                            hide cclover
                            show cclying
                            c "Erm..."
                            hide cclying
                            show ccsorpresa
                            c "No."
                            hide ccsorpresa
                            show ccwow
                            c "OH TRUE!"
                            hide ccwow
                            show cclover
                            c "You might see your lover for a last time, she's having a play in some time."
                            c "Like a farewell kiss mwah mwah-{nw=0.3}"
                            y "O-OKAY I GOT IT!!!!" with vpunch
                            hide cclover
                            show ccsorpresa
                            y "I will go and see her."

                            #### ANIMACION DE SCHELL ACTUANDO ALGUNA WEÁ ###
                            scene fondonegro
                            stop music
                            play music "audio/horrormusic.mp3"
                            y "Yeah now I know why I am a trial agent."
                            y "Not someone like him..."
                            y "Sigh..."
                            
                            scene fondo1vladan
                            show vladan2
                            v "Hmm."
                            hide vladan2
                            show vladan3
                            v "What did I tell you?"
                           

                            scene fondonegro with fade
                            $renpy.pause(1)
                            
                            play sound "audio/slimeo.mp3"
                            play movie "images/slimeo.webm"
                            
                            $renpy.pause(14)
                            $renpy.full_restart()
                        "{sc=5}Yes! You do look good.{/sc}":
                            scene fondonegro
                            stop music
                            play music "audio/normalmusic2.mp3"
                            play sound "audio/coser.mp3"
                            scene fondoo
                            show ssonriente
                            s "Yay! I knew you would say that! Good doggy!"
                            "You feel uncomfortable with her good doggy comment but you still keep up."
                            y "Can I still ask you about your dressing room?"
                            hide ssonriente
                            show soh
                            s "Yes! Anything for you."
                            y "Ok so I was looking around and I saw this painting on the wall."
                            hide soh
                            scene pintura
                            y "What is it? What does it represent?"
                            s "To be honest, not even I know about it. It was painted by father."
                            menu:
                                "Then what do you think it represents?":
                                    s "Hmmm..."
                                    s "Probably my admirers being represented as crocodiles."
                                    s "And me hanging with my feet on that rope."
                                    y "(I think she makes everything about herself.)"
                                    n "Yes she does."
                                "Father? Who's 'father'?":
                                    show ssonriente at left
                                    s "The man who gave me this body."
                                    $father = True
                                    $notificar("Father of hers")
                                    s "I owe him so much."
                                    s "That's why I act."
                            y "And you're OK with that?"
                            s "With what?"
                            y "To keep pleasing others as payment?"
                            hide ssonriente
                            show smikan at left
                            s "I don't think it's bad actually haha."
                            s "I think we should be grateful about everything...So yeah, I am doing this because I want to, yep."
                            y "Alright, I feel that's valid enough."
                            "You don't."
                            jump resumen
                "And the numbers?":
                    hide ssonriente
                    show sdisgusto
                    s "Hmm?"
                    s "Are you even from here?"
                    y "I-I am, I just use a sand timer! This one!"
                    "You show her the sand timer."
                    s "That's very old fashioned."
                    s "But now old fashioned in the fashion way you know?"
                    s "I think it makes you look older haha."
                    s "And that's not a compliment by the way."
                    y "You're kind of right haha..."
                    hide sdisgusto
                    show skidding
                    s "You never knew how to read an average clock? Hmmm..."
                    n "Don't make it worse! She's already suspicious of you! D:"
                    menu:
                        "I actually do, it's just that I prefer this one.":
                            hide skidding
                            show strescuartos
                            s "Oh alright."
                            n "You just saved yourself! Be glad!"
                            n "I didn't even intervene yet you could handle it! Good job little demon."
                        "No, I actually don't.":
                            hide skidding
                            show ssonriente
                            s "Haha it can be a bit hard can't it?"
                            n "WAIT WHAT?" with vpunch
                            n "She was supposed to throw you out of the room!!!!"
                            n "What is happeningggg hhghasjfhhsjrhghjs"
                    hide strescuartos
                    hide ssonriente
                    show sseria
                    y "So, keep talking to me about your room! Is there anything else you want to add?"
                    n "This conversation line sounds so forced LMAO get creative please."
                    hide sseria
                    show spensativa
                    s "Hmmm, not reallyyy..."
                    hide spensativa
                    show soh
                    s "OH, no, no. Yes. I want to show something to my fans!"
                    s "Thanks to these ladies I am stitched well!"
                    s "Let me show you all my strong and beautiful threads!"
                    hide soh
                    scene sthreads with fade
                    
                    
                    s "These are the reasons why I can bring you all my amazing superb marvelous plays!"
                    y "And why do you think they are important?"
                    s "Because they make me look beautiful and not like some mess without 'mascara'."
                    y "Do you often feel insecure about your looks?"
                    y "Your {sc=5}actual{/sc} looks?"
                    s "..."
                    s "That's not a question to ask."
                    y "Oh sure anyway..."
                    jump resumen




    

label maniquies:
    if maniquies:
        hide spensativa
        show snerviosa
        s "Wait...didn't you already ask me about those?"
        hide snerviosa
        show skidding
        s "Are you even paying attention to our conversation?"
        y "I...uh..."
        hide skidding
        show strescuartos
        s "Move on already."
        hide strescuartos
        jump menupreguntasprincipales
    else:
        $maniquies = True
        jump menupreguntasprincipales1


label resumen:
    scene fondonegro with fade
    $renpy.pause(2)
    "A memory comes flashing to you like a bullet train..."

    scene fondo1vladan with fade
    show vladan3 with fade
    v "You have to manipulate her."
    v "You have to bring us information."
    hide vladan3 with dissolve
    scene fondonegro with fade
    $renpy.pause(1)
    "It was like that right?"
    "Right?"

    $renpy.pause(1)
    n "Hey I think you two have talked more than enough. I think it's time you choose a path..."
    n "I mean, you have gotten enough information! Let's see..."
    n "I mean you have {b}bad{/b} memory, you know?"

    if directorr:
        n "The director's name is Menschsein. Probably his last name."
        n "He makes all these weird plays."
        n "These plays must have a meaning though."
        n "We can ask around the ███ to see if anyone gets a meaning from the plays."
        n "We never know if that director is the entity or not."
        y "Wait which entity?"
        n "Ah you don't remember? You're the one who read the damn article about it."
        y "I don't remember doing so."
        n "It was before VladVlad came in and yaddayadda."
        y "Hmmm...No..?"
        n "Yeah he probably did it."
        y "Did what?"
        n "Uhh nothing."
        $points +=1
    
    if concordia:
        n "The theater's name is Concordia, don't forget that."
        n "That's how these freaks call it instead of 'Spikeball'."
        n "It's a whole new world for you."
        n "Yeah, like the song."
        $points +=1
   
    if brujas:
        n "Even the witches depicted in books are weird, have you heard the girl? They flight with a reverse broom!"
        n "Are they onto something?"
        n "Concordia people are like aliens for real."
        n "Or not?"
        $points +=1
   
    if marcel:
        n "Oh yeah true, the Marcel guy."
        n "Who even is that?"
        n "Is he from here? Or is he someone like HER?"
        n "Like, not from here and comes from the other ground."
        n "That's probably not his name at all, it can be an alias."
        n "Maybe he was created by the entity..."
        y "WHAT'S WITH YOU AND THE ENTITY?"
        n "Calm down bruh I am trying to remember what you gathered."
        $points +=1
    
    if normal:
        n "Oh YEAH!"
        n "I have no words about the plays!"
        n "They are comedic but ABSURD."
        n "They aren't normal."
        n "The people here take them seriously."
        n "As those who criticizes movies and while they have only watched Fruit Fiction as their only elite knowledge movie."
        n "Bleh."
        $points +=1
  
    if scripts:
        n "We need to keep an eye on Mr Menschsein's scripts."
        n "They live I think."
        n "Or however you want to put it."
        $points +=1
    
    if johncage:
        n "As I mentioned before, did you notice that she mentioned Jhonnas Craige?"
        n "Her family must have been an art enthusiast to know him and probably respect him."
        n "Even if I dislike his 'music' blehhh..."
        y "I think all art should be respected, don't be rude."
        n "Nonsense."
        $points +=1
    
    if pestanas:
        n "Hmmmm...."
        n "She for real isn't normal I mean look at those eyelashes."
        y "Hey! That's rude!"
        n "She's a human converted into a doll...What is she?"
        $points +=1
   
    if competitividad:
        n "About the culture inside the Spikeball..."
        n "There's probably a competivity culture around the theater, don't you think?"
        n "Like, who's more special than who."
        n "No 'Yay! Let's help each other out' culture."
        n "Kinda sad."
        $points +=1
    
    if efectivamente:
        n "My bad."
        n "Yeah you're right. She's indeed not normal. She's a burnt body dressed as a doll."
        n "It was not only the lashes..."
        y "When did I even say something about her?"
        n "Shhhh."
        $points +=1
    
    if relojes11:
        n "Those clocks..."
        n "There must be a reason why they look like the only time is 11 o'clock"
        n "We can ask our beloved agent about that."
        n "It can be a clue to the entity's whereabouts."
        $points +=1
    
    if thequeen:
        n "And who's 'The Queen'? Could it be the entity?"
        n "Something tells me she is!!!!!!!"
        y "You are just a fragment from my thoughts you know? There isn't 'something'"
        n "Shut your mouth."
        $points +=1

    if god:
        n "By the way, who is 'god'? Is it the entity? Could it be? Is it related to the queen?"
        n "I need answers."
        $points +=1
    
    if father:
        n "And yeah, who is 'father'? If he was a doctor, whatever he is, he must have been a good one."
        n "Probably one who had an obsession with dolls."
        n "Haven't you read something about it at the secret room behind the yellow door at the B building?"
        n "If he was from the other ground he must have been an assasin."
        n "Like the Black Dahlia case or something."
        y "That doesn't make any sense!"
        $points +=1
    

    n "Hmmm..."
    if points >= 7:
        n "Hey not bad, we yes WE got solid information to give to our dear agent, yay!"
    if points <= 7:
        n "Oh oops."
        n "Damn it!"
        n "We don't have enough information to share..."
        n "I would have given you a game over but I will let you see the end of this."
    
    n "Even if you consider her a friend already, we must leave as soon as possible."
    n "Remember the J-414 records."
    y "What did they say?"
    n "Augh c'mon you READ it."
    y "I don't remember that!"
    n "The entity mingling around!!"
    n "Yeah and you don't belong here so it can kill you if it finds out and blah blah blah."
    n "I repeat."
    n "You {b}don't{/b} belong here."
    

    n "You have to decide."
    n "Either be her friend and be a disgrace to the ███ or become a bad influence to her and leave immediately."
    n "Hsjashd we are done with the booooring part of this game."
    n "We already reached the part Ramelden wrote as the summary of the game!"
    n "So, EJEMPH, what are you choosing, mate?"


label decision:
    while True:
        $resultado, veces_esquivado = renpy.call_screen("decisionesquiva")

        if resultado == "enemy":
            if veces_esquivado >= 5:
                n "Did you really think I would let you click that?"
                n "You even wasted your time trying to click it."
                n "Watching you struggle was so funny Hasdjsdjh"
                n "Anyway, let's proceed."
                y "But I wanted to be her friend!"
                n "You really think you can be friends with someone you had to betray from the very beginning?"
                n "It's like trying to be friends with someone who was your lover."
                n "Remember! This is no dating sim!"
            jump renemy
        

label renemy:
    scene fondoo
    show ssonriente
    stop music
    play music "audio/horrormusic.mp3"
    n "Woah!!"
    n "Great job! Now he will be grateful for this, now go!"
    y "Hey umm..."
    y "Don't you sometimes feel that your thankfulness has become a prison to you?"
    hide ssonriente
    show snerviosa
    s "Sorry what?"
    y "I mean you said that we should be grateful about everything. Don't you think it can become a prison?"
    hide ssonriente
    show sincomoda
    s "Why a prison? haha..."
    y "You also mentioned something about your father right?"
    s "I don't think so..."
    hide sincomoda
    show snerviosa
    y "You said your father gave you this body and all right?"
    s "Of course...!"
    hide snerviosa
    show sincomoda
    scene fondooevil
    show sincomoda
    y "Well, what if when you are at the play and he claps, he claps for the play only?"
    y "And not his DAUGHTER?"
    show sincomoda at center, constant_shake
    s "Haha silly, what are you even saying? Haha..."
    s "My father loves me so much..."
    s "He literally stitched me with all his effort and saved me...!"
    s "You can't just assume something like that...We are friends."
    
    y "You trust someone who just came in and interviewed you as a job and you consider them a friend?"
    y "You must have very low self esteem."
    y "Pretty contradictory for an actress like you."
    y "Or the actress you claim to be."
    s "But we talked and...!{nw=0.5}"
    y "Haven't your {b}real{/b} parents warned you about strangers?"
    y "I AM a stranger. How come you don't realize I don't come from here?"
    hide sincomoda
    hide sincomoda
    show scelestia2
    s "WHAT?" with vpunch
    y "I am an agent helper, Schell. That's my job. My {sc=5}REAL{/sc} job."
    scene fondooevil1
    hide scelestia2
    show sgiffany
    y "To betray others who think I am interested in them."
    y "That smile of yours, isn't it fake?"
    stop music
    s "..."
    s "..."
    y "I must admit, you are a great actress." 
    y "You even showed me a different side of yours when we first started talking and now you're probably not even feeling bad about what I am saying."
    y "But returning to your smile...Do you force it? Is it genuine? Or a well fabricated lie?"
    hide sgiffany
    show smolestaojoabierto
    s "STOP IT! You're so mean...!" with vpunch
    s "SECURITY-!{nw=0.2}"
    y "They can't hear you." with vpunch
    play music "audio/horrormusic.mp3" volume 3.0
    hide smolestaojoabierto
    show scelestia
    s "Gah!" with vpunch
    y "Perhaps that question was a bit out of context hmmm, but I need to keep interviewing you."
    y "Perhaps you being tired at times represents your humanity, the fact that you're still a human."
    y "{b}Even if you're a naked meat moving piece.{/b}"
    hide scelestia
    show scelestia1 at center, constant_shake 
    s "WHAT DID YOU SAY TO ME?" with vpunch
    y "Now, let me ask you a final question."
    y "If tomorrow, everyone would stop looking for your thanks and at the same time thanking you, would you still go on that stage?"
    y "If the answer takes long to come from your mouth..."
    y "It's because your belief is not love. Or a passion."
    hide scelestia1
    show scelestia
    y "It's just a devilish lie with a nice face."
    hide sincomoda
    scene sperfil1
    s "..."
    s "..."
    scene sperfil2
    s "Why are you doing this to me?"
    y "I am just trying to interview you."
    y "Oh, and now that you just mentioned we are friends..."
    y "I believe friends can ask more profound questions, can't they?"
    y "Rather than the chitchat we were spitting earlier."
    scene sperfil2 at constant_shake
    s "{sc=5}Y-you...{/sc}"
    s "{sc=5}You're straight up fake...{/sc}"
    s "{sc=5} Even if I tell you to stop you just DON'T!!{/sc}"
    s "{sc=5}I can't stand you anymore...{/sc}"
    s "{sc=5}And you are telling me this right when I am going on stage in some time...{/sc}"
    s "{sc=5}{size=*3}YOU ARE DISGUSTING.{/size}{/sc}"






