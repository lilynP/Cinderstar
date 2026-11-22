default persistent.language_chosen = False

screen language_choice():
    modal True
    add Solid("#000000AA")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 400
        background Frame("gui/overlay/game_menu.png")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 50

            text "Select language / Selecciona el idioma":
                xalign 0.5
                text_align 0.5
                size 40
            hbox:
                xalign 0.5
                spacing 100

                textbutton "English":
                    text_size 35
                    xsize 250
                    ysize 80
                    background Frame("gui/button/choice_idle_background.png", 20,20)
                    action[SetField(persistent, "language_chosen", True), Language(None), Return(True)]
                textbutton "Español":
                    text_size 35
                    xsize 250
                    ysize 80
                    background Frame("gui/button/choice_idle_background.png", 20,20)
                    action[SetField(persistent, "language_chosen", True), Language("spanish"), Return(True)]
                    