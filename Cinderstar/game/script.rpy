#for the faded or non hovered secret or hidden option for the dialogues
default reloj_desbloqueado = False
#for avoiding asking the same question all over again
default maniquies = False
default pdrawers = False

#for the notify and new findings############
default director = False
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

#for the notify thingy
init python:
    def notificar(pista_texto):
        renpy.notify("New finding! " + pista_texto)


#for the trembling movement

transform constant_shake:
    subpixel True
    # Randomizes the offset slightly every 0.05 seconds
    choice:
        linear 0.05 xoffset 5 yoffset -5
    choice:
        linear 0.05 xoffset -5 yoffset 5
    choice:
        linear 0.05 xoffset -3 yoffset -3
    choice:
        linear 0.05 xoffset 5 yoffset 3
    repeat

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Schell", who_color='ffffff', window_background = Frame("images/textboxschell.png"), callback = typing_callback)
define y = Character("You", who_color = 'ffffff', window_background = Frame("images/textboxyou.png"), callback = typing_callback)
define v = Character("Vladan", who_color = 'ffffff', window_background = Frame("images/barrattextovladan.png"), callback = typing_callback)
define n = Character(" ??? ", who_color = 'ffffff', window_background = Frame("images/textboxnarrador.png"), callback = typing_callback)

image fuegomovil = Movie(size=(2800,1100), channel = "movie", play = "images/fueguito.webm")
image reina = Movie(size=(1920,1080), channel = "movie", play = "images/reina.webm")

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
    s "Ok so the drill rings, right?"
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
                    $johncage = True
                    $notificar("Jhonnas Craige")
                    hide sgrin
                    show ssonriente
                    s "Quite ironic though."
                    y "Didn't Menschsein mean 'being human' in german? Sorry to interrupt..."
                    $director = True
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

                        "That was another of you jokes, right? Sorry, just keep going...":
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
    "en espera wait wait 1"
    return

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

    if director:
        n "The director's name is Menschsein. Probably his last name."
        n "He makes all these weird plays."
        $points +=1
    
    if concordia:
        n "The theater's name is Concordia, don't forget that."
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
        $points +=1
    
    if normal:
        n "I have no words about the plays!"
        n "They are comedic but ABSURD."
        n "They aren't normal."
        n "The people here take it seriously."
        n "As those who criticizes movies and while they have only watched Fruit Fiction as their only elite knowledge movie."
        n "Bleh."
        $points +=1
  
    if scripts:
        n "We need to keep an eye on Mr Menschsein's scripts."
        n "They live I think."
        n "Or however you want to put it."
        $points +=1
    
    if johncage:
        n "As I mentioned before, did you notice that she mention Jhonnas Craige?"
        n "Her family must have been an art enthusiast to know him and probably respect him."
        $points +=1
    
    if pestanas:
        n "She for real isn't normal I mean look at those eyelashes."
        n "She's a human converted into a doll...What is she?"
        $points +=1
   
    if competitividad:
        n "There's probably a competivity culture around the theater, don't you think?"
        n "Like, who's more special than who."
        n "No 'Yay! Let's help each other out' culture."
        n "Kinda sad."
        $points +=1
    
    if efectivamente:
        n "Yeah you're right. She's indeed not normal. She's a burnt body dressed as a doll."
        n "It was not only the lashes..."
        $points +=1
    
    if relojes11:
        n "Those clocks..."
        n "There must be a reason why they look like the only time is 11 o'clock"
        n "We can ask our beloved agent about that."
        n "It can be a clue to the entity's whereabouts."
        $points +=1
    
    if thequeen:
        n "Who's 'The Queen'? Could it be the entity?"
        $points +=1

    if god:
        n "Who is 'god'? Is it the entity? Could it be?"
        $points +=1
    
    if father:
        n "Who is 'father'? If it was the doctor, whatever he is, he must have been a good one."
        n "Probably one who had an obsession with dolls."
        n "Haven't you read something about it at the secret room behind the yellow door at the B building?"
        $points +=1
    

    n "Hmmm..."
    if points >= 7:
        n "Hey not bad, we yes WE got solid information to give to our dear agent, yay!"
    if points <= 7:
        n "Oh oops."
        n "Damn it!"
        n "We don't have enough information to share..."
        n "I would have given you a game over but I will let you see the end of this."
    
    n "She already considers you a friend, so be careful because according to the J-414 records, the entity mingling around can kill you if it knows you don't belong here."
    n "I repeat."
    n "You {b}don't{/b} belong here."





