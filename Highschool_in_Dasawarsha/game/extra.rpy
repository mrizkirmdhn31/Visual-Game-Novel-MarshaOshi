# Extras Screens

image pager_button = im.FactorScale("extra/pager_cr.jpg", 0.25)
image lorong_button = im.FactorScale("extra/lorong_cr.jpg", 0.25)
image kepsek_button = im.FactorScale("extra/kantor_kepsek_cr.jpg", 0.25)
image kelas_button = im.FactorScale("extra/kelas_cr.jpg", 0.25)
image ruangtamu_button = im.FactorScale("extra/ruang_tamu_cr.jpg", 0.25)
image mall_button = im.FactorScale("extra/mall_cr.jpg", 0.25)
image kantin_button = im.FactorScale("extra/kantin_cr.jpg", 0.25)


# image bglock_button = "gui/bg_locked.jpg"

init python:

    # Gallery
    # g = Gallery()

    # A button with an image that is always unlocked
    # g.button("pager_cr")
    # g.image("pager_cr")
    
    # g.button("lorong_cr")
    # g.image("lorong_cr")

    # g.button("kantor_kepsek_cr")
    # g.image("kantor_kepsek_cr")

    # g.button("kelas_cr")
    # g.image("kelas_cr")
    
    # g.button("ruang_tamu_cr")
    # g.image("ruang_tamu_cr")

    # g.button("mall_cr")
    # g.image("mall_cr")

    # g.button("kantin_cr")
    # g.image("kantin_cr")


    # Ending Unlocked Pict

    # g_ed = Gallery()

    # g_ed.button("pager")
    # g_ed.image("pager")
    # g_ed.unlock("pager")

    # g_ed.button("lorong")
    # g_ed.image("lorong")
    # g_ed.unlock("lorong")

    # Button used for locked image

    # g_ed.locked_button = "bglock_button"

    # Transition used when switching images

    # g.transition = dissolve
    # g_ed.transition = dissolve    



    # Music
    mr = MusicRoom(fadeout=1.0)

    # Add Music files

    mr.add("audio/list_music/Run_Run_Run_(off_vocal).mp3", always_unlocked=True)
    mr.add("audio/list_music/eien_pressure.mp3", always_unlocked=True)
    mr.add("audio/list_music/oshibe.mp3", always_unlocked=True)



## Extras Navigation Screen

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Characters") action ShowMenu("characters") alt "Characters"

        # textbutton _("Music List") action ShowMenu("music") alt "Music List"

        textbutton _("Gallery") action ShowMenu("bg_gallery") alt "Gallery"
        
        # textbutton _("Ending Unlocked") action ShowMenu("ed_gallery") alt "Ending Unlocked"

        textbutton _("Note For Marsha") action ShowMenu("catatan") alt "Notes"

        textbutton _("Return") action Return() alt "Return"


## Extras Menu Screen

screen extras_menu(title, scroll = None, yinitial = 0.0):
    style_prefix "game_menu"
    
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    
    label title

    use extras_navigation

## About characters ################################################################
##
## This screen describe about characters in this games
## example of how to make a custom screen.

screen characters():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use extras_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters"

        vbox:

            add "GC/profil_0.jpg" fit "contain"
            text _("\n")
            add "GC/profil_1.jpg" fit "contain"
            text _("\n")
            add "GC/profil_2.jpg" fit "contain"
            text _("\n")
            add "GC/profil_3.jpg" fit "contain"
            text _("\n")
            add "GC/profil_4.jpg" fit "contain"
            text _("\n")
            add "GC/profil_5.jpg" fit "contain"
            text _("\n")
            add "GC/profil_6.jpg" fit "contain"
            text _("\n")
            add "GC/profil_7.jpg" fit "contain"
            text _("\n")
            add "GC/profil_8.jpg" fit "contain"



style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Music List

screen music():

    tag menu

    use extras_menu(_("Music List")):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.

            textbutton "Run Run Run (Off Vocal)" action mr.Play("audio/list_music/Run_Run_Run_(off_vocal).mp3")
            textbutton "Eien Pressure (Off Vocal)" action mr.Play("audio/list_music/eien_pressure.mp3")
            textbutton "Oshibe to Meshibe to Yoru no ChouChou (Off Vocal)" action mr.Play("audio/list_music/oshibe.mp3")
            
            null height 20

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous() alt "Previous Song"
                textbutton "Next" action mr.Next() alt "Next Song"

            null height 20 

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        ## Restore the main menu music upon leaving.
        ## You can actually comment this out if you want to let players enjoy the music
        ## while looking at the other screens.
        # on "replaced" action Play("music", "audio/list_music/Run_Run_Run_(off_vocal).mp3")

# End Credit Scroll

# Credit ending scene

# Content of your credits screen
define credits_string = _p("""
{size=+35}Credits{/size}
\n\n
{size=+15}Game Designer:{/size}
\n
Vhyrie
\n
Authormagang
\n
{size=+15}Game Programmer:{/size}
\n
Tetsuoga
\n
{size=+15}Art Director:{/size}
\n
Vhyrie
\n
{size=+15}Background Artist:{/size}
\n
Vhyrie
\n 
Dilgudil
\n
{size=+15}Character Artist:{/size}
\n
Vhyrie
\n 
Wisnue
\n
{size=+15}UI Artist:{/size}
\n
Bass
\n 
{size=+15}Script Writer:{/size}
\n
Authormagang
\n
{size=+15}Sound Engineer:{/size}
\n
Tetsuoga
\n 
Authormagang
\n
{size=+15}Song:{/size}
\n
"Kamu, Selamanya"
\n
{size=+15}Vocal Performed by:{/size}
\n
Meowkwang
\n
Yeorin
\n
{size=+15}Written by:{/size}
\n
Dimas Jimbo
\n
Wisnue
\n
{size=+15}Composed by:{/size}
\n
MoisslsYours
\n
{size=+15}Arranged by:{/size}
\n
MoisslsYours
\n
Dimas Jimbo
\n
{size=+15}Mixed by:{/size}
\n
Dimas Jimbo
\n
Meowkwang
\n
Yeorin
\n
{size=+15}Mastered by:{/size}
\n
Dimas Jimbo
\n
{size=+15}Backing Vocals by:{/size}
\n
Bronis
\n
Uty
\n
Kepin
\n
Andi
\n
Arkan
\n\n
{size=+15}Special Thanks{/size}
\n
Hamba Marsha
\n\n
{size=+15}Very Special Thanks{/size}
\n
Marsha Lenathea Lapian
\n\n\n\n\n\n\n\n
{size=+12}
\n
Terima kasih sebesar-besarnya kami ucapkan pada semua pihak yang terlibat dalam pembuatan Visual Novel MarshaOshi: Highschool in Dasawarha.\n 
Visual Novel ini kami persembahkan untuk Marsha sebagai hadiah ulang tahunnya yang ke-17 sekaligus untuk semua fans Marsha. Semoga Marsha bahagia dan sehat selalu diumur ke-17 ini.\n
Panjang umur hal-hal baik!
\n\n\n
MarshaOshi
\n\n
{size=+15}Made with Ren'Py{/size} 
\n
{size=+15}[renpy.version_only].{/size}\n\n\n\n
{size=+15}Thanks for Playing!{/size}\n\n\n\n
{size=+15}Twitter{/size}
{size=+15}@marshaoshi_{/size}
\n
{size=+15}Instagram{/size}
{size=+15}marshaoshi_{/size}
{size=+15}{/size}
""")



# This controls the position and speed of your end credits
transform credits_scroll(t):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    linear t yanchor 1.0 ypos 0.0

# The actual end credits screen that we call

screen credits(t):

    style_prefix "credits"

    # Ensure that the game_menu screens don't appear and interrupt the credits

    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    # If a player has sene the credits before, this button appears.

    if persistent.credits_seen:
        
        textbutton _("Skip End Credits") action Jump("skip_credits"):
            xalign 1.0 yalign 1.0

    # When t is up, the game will go to the next line.
    timer t action Return()
    # The contents of your credits screen is here.
    text credits_string text_align 0.5 at credits_scroll(t)

style credits_text:
    size gui.title_text_size
    color "#000000"

# Pesan untuk Marsha

screen catatan():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Note For Marsha"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## Your text goes here.
            if gui.dev_notes:
                text "[gui.dev_notes!t]\n"

## Type your special message here.
define gui.dev_notes = _p("""Halo Marsha, pertama-tama selamat ulang tahun ke-17. Happy sweet 17 yak. Cie udah bisa nyanyi lagu seventeen sekarang wkwkwk. Btw hadiah dari aku game ini aja ya, soalnya aku seneng bisa masuk bagian tim developer buat bikin game visual novel pertama MO ini.\n
Kalo ditanya susah apa gak ya... Susah-susah gampang tapi aku bawa seneng aja soalnya ilmu aku kepake juga dan bisa belajar banyak tentang bahasa pemrograman python ini. FYI kalo kamu mau kepo aja ya hehehe...\n
Bisa nyelesein game ini juga reward bagi anak-anak MO yang bener-bener khusus buat kamu. Kamu kalo mau ajak member-member lain juga boleh soalnya beberapa ada mereka juga di game ini. Walau gak semua yaaa...\n
Oh iya, kalo boleh jujur aku juga ngikutin kamu baru-baru ini loh Sha wkwkwkwk, jadi belom lama sebenernya. Masuk MO pun juga baru-baru ini juga.\n
Aku pun ganyangka juga bisa ikut bantu buat project STS sweet 17 kamu ini.\n
Mungkin itu dulu aja, kalo semisal dikasih kesempatan VC kita ketemu di VC aja yak!\n
-Tetsuoga-""")

screen bg_gallery():
    
    tag menu
    
    use extras_menu(_("Gallery"), scroll="viewport"):

        vbox:

            add "extra/pager_cr.jpg" fit "contain"
            text _("\n")
            add "extra/lorong_cr.jpg" fit "contain"
            text _("\n")
            add "extra/kelas_cr.jpg" fit "contain"
            text _("\n")
            add "extra/mall_cr.jpg" fit "contain"
            text _("\n")
            add "extra/kantin_cr.jpg" fit "contain"
            text _("\n")
            add "extra/kantor_kepsek_cr.jpg" fit "contain"
            text _("\n")
            add "extra/ruang_tamu_cr.jpg" fit "contain"
            text _("\n")
            # xalign 0.5
            # yalign 0.5
            # spacing 30

            # grid 1 7:
               
            #     add g.image("pager_cr", "pager_button", xalign=0.5, yalign=0.5)
            #     add g.image("lorong_cr", "lorong_button", xalign=0.5, yalign=0.5)
            #     add g.image("kantor_kepsek_cr", "kepsek_button", xalign=0.5, yalign=0.5)
            #     add g.image("kelas_cr", "kelas_button", xalign=0.5, yalign=0.5)
            #     add g.image("ruang_tamu_cr", "ruangtamu_button", xalign=0.5, yalign=0.5)
            #     add g.image("mall_cr", "mall_button", xalign=0.5, yalign=0.5)
            #     add g.image("kantin_cr", "kantin_button", xalign=0.5, yalign=0.5)

            #     spacing 15

            
            # textbutton "Return" action Return()

# screen ed_gallery:

#     tag menu
    
#     use extras_menu(_("Ending Unlocked"), scroll="viewport"):

#         vbox:
#             xalign 0.5
#             yalign 0.5
#             spacing 30

#             grid 2 2:

#                 add g.make_button("pager", "pager_button", xalign=0.5, yalign=0.5)
#                 add g.make_button("lorong", "lorong_button", xalign=0.5, yalign=0.5)
#                 add g.make_button("pager", "pager_button", xalign=0.5, yalign=0.5)
#                 add g.make_button("lorong", "lorong_button", xalign=0.5, yalign=0.5)

#                 spacing 15

            
            # textbutton "Return" action Return()