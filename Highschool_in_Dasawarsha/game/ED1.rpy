label ED1:
    $ renpy.block_rollback()
    $quick_menu = True
    play music "audio/sfx/thunder.mp3" noloop
    hide marsha
    show marsha_confused
    marsha_confused "!!!!!!!" with hpunch
    hide marsha_confused
    show marsha_cry
    "Marsha menangis"
    hide marsha_cry with moveoutright
    "Meninggalkan [mcname] sendiri lari ke kelas."
    call credits from _call_credits
    return

label credits:
    $ renpy.block_rollback()
    ## for hide quickmenu for the last part, so they don't appear at bottom
    $quick_menu = False

    # hide the textbox
    window hide

    scene background_ending with fade

    play music "audio/list_music/kamu_selamanya.mp3" fadeout 1.0

    # Find "End Credits Scroll" in extras.rpy to change text.
    
    call screen credits(75.0)

    $ persistent.credits_seen = True

    scene black with fade

    # Player can skip the credits

    label skip_credits:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return