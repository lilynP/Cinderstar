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
    show vladan1 

    v "CAUSA TE TIENES QUE IR"

    hide vladan1



    scene fondoo

    show spensativa
    with fade

    s "What does 'poggers' mean?"

    hide spensativa
    show strescuartos

    s "You're scary man, are you even human?"

    n "Looks like someone didn't like your comment! Try again later!"


    

    return
