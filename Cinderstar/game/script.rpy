# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Schell", who_color='ffffff')
define p = Character("Interviewer")



# The game starts here.

label start:

    stop music

    scene fondoo

    show spensativa
    with fade

    s "What does 'poggers' mean?"

    hide spensativa
    show strescuartos

    s "You're scary man, are you even human?"

    "Looks like someone didn't like your comment! Try again later!"


    

    return
