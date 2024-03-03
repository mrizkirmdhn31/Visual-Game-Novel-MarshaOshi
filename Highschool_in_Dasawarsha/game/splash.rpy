image splash_animation:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

image marsha_oshi:
    "gui/logo_mo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0

default persistent.firstlaunch = False

image game_logo:
    "gui/logo_vn.png"
    xalign 0.5 yalign 1.0 alpha 0.0
    ease_quad 4.0 alpha 1.0 zoom 1.3


label splashscreen:

    scene black

    $ persistent.firstlaunch = True
    
    show splash_animation
    show text "{color=#FFFFFF}{size=60}Made with Ren'Py [renpy.version_only]{/s}{/c}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 5.0
        linear 1.0 alpha 1.0

    if not persistent.seen_splash:
    
        $ renpy.pause(8.5, hard = True)

        $ persistent.seen_splash = True

    else:
        
        if renpy.pause(8.5):
            jump skip_splash

    label skip_splash:

        pass
    
    scene black
    with fade

    show game_logo:
        xalign 0.5 yalign 0.0

    $ renpy.pause(2.0)

    show text "{color=#FFFFFF}{size=40}Made by{/s}{/c}":
        xalign 0.5 yalign 0.6 alpha 0.0
        pause 1.5
        linear 1.0 alpha 1.0    

    show marsha_oshi:
        xalign 0.5 yalign 0.75 alpha 0.0
        pause 1.5
        linear 1.0 alpha 1.0 

    $ renpy.pause(6.0)

    scene black
    with fade

    $ renpy.movie_cutscene('images/splash.ogv')

    return