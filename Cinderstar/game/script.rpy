# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Schell", who_color='ffffff', window_background = Frame("images/textboxschell.png"))
define y = Character("You")
define v = Character("Vladan", who_color = 'ffffff', window_background = Frame("images/barrattextovladan.png"))
define n = Character(" ???  ", who_color = 'ffffff', window_background = Frame("images/textboxnarrador.png"))



# The game starts here.

label start:

    stop music

    scene fondo1vladan
    show vladan2
    v "..."
    hide vladan2
    show vladan3

    v "You woke up"
    hide vladan3
    show vladan2
    v "..."
    hide vladan2
    show vladan3
    v "Don't be scared"

    hide vladan3
    show vladan2
    v " "
    hide vladan2
    show vladan3
    v "You have been selected for the code 45590-bqn mission"
    v "You OUGHT to finish it"
    hide vladan3

    show vladan1
    v "YOU HAVE TO ENTER THE SPIKEBALL EVEN IF YOU DO NOT WANT IT"
    v "YOU HAVE TO BRING US INFORMATION"

    y "Gah!"

    hide vladan1
    show vladan3
    v "Just..."
    hide vladan3
    show vladan2
    v "..."
    hide vladan2
    show vladan3
    v "Do not get too comfortable"
    v "She is the only one we have discovered until now that has origins from here."
    v "Of course she will mix knowledge from here and there"
    hide vladan3

    show vladan2
    v "..."
    hide vladan2
    show vladan3
    v "Just..."
    v "Don't get discovered, because..."
    v "You can die"
    hide vladan3

    show vladan1
    v "STOP COMPLAINING"
    v "YOU WERE THE CHOSEN ONE"
    hide vladan1
    show vladan3
    v "Don't you dare disappoint"
    hide vladan3
    "His voice resonates in your mind like some church bell"
    "Your conciousness starts fading..."
    
    "And you finally close your eyes...Again."

    with fade
    scene fondonegro



    scene fondoo

    show spensativa
    with fade

    s "What does 'poggers' mean?"

    hide spensativa
    show strescuartos

    s "You're scary man, are you even human?"

    n "Looks like someone didn't like your comment! Try again later!"


    

    return
