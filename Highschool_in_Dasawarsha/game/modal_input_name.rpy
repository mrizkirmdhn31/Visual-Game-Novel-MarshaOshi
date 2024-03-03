screen name_input(message, ok_action, output_var="player", characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890  ", len = 15):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action ok_action

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5
            
            # This is the line we change to use our new variables.
            input default "" value VariableInputValue(output_var) length len allow characters

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen popup_message(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action ok_action

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5
            
            # This is the line we change to use our new variables.
            # input default "" value VariableInputValue(output_var) length len allow characters

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action