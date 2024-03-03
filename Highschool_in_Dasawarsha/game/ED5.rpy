label pulang2:
    $ renpy.block_rollback()
    $ quick_menu = True
    show marsha_angry
    mcname "Ikut dulu aja."
    marsha_angry "Ke mana?"
    mcname "Udah, ikut dulu aja."
    marsha_angry "Ok."
    marsha_angry "Iya. Gausah narik-narik."
    marsha_angry "Ga suka."
    hide marsha_angry
    stop music

    jump pulang3

label pulang3:
    $ renpy.block_rollback()
    scene ruang tamu with fade
    "Sesampainya di rumah Marsha"
    "[mcname] langsung masuk ke ruang keluarga diikuti Marsha"
    "Ada Kak Indah di ruang keluarga"
    mcname "Selamat sore kak Indah"
    play music "audio/bgm/falling_love.mp3"
    show indah with dissolve
    indah "Eh, [mcname]."
    hide indah
    show indah_smile
    indah_smile "Makasih ya udah anterin Marsha pulang."
    marsha4 "Mau anterin pulang aja kamu izin ke kak Indah dulu?"
    mcname "Izinlah. Masa enggak."
    hide indah_smile
    show indah_happy
    indah_happy "hahaha"
    hide indah_happy
    show indah
    indah "Aku lagi nyeduh teh."
    indah "Kalian mau?"
    mcname "Mau kak."
    marsha1 "Iya aku mau juga kak."
    hide indah
    show indah_smile
    indah_smile "Yaudah bentar ya, aku ambilin dulu."
    hide indah_smile
    "Indah meninggalkan [mcname] sama Marsha berdua"
    mcname "Sini."
    mcname "Duduk, sha."
    show marsha_angry
    marsha_angry "Siapa yang nyuruh kamu duduk?"
    hide marsha_angry
    $ quick_menu: False
    menu:
        "M-Maaf Sha...":
            jump ruang_tamu

label ruang_tamu:
    $ quick_menu: True
    show marsha_angry
    marsha_angry "Aku masih marah ya sama kamu."
    marsha_angry "Ga usah anggep kayak rumah sendiri."
    mcname "Maaf."
    hide marsha_angry
    "Marsha duduk"
    "Sementara [mcname] masih berdiri"
    "Tidak lama kemudian, kak Indah datang sambil membawa teh"
    show indah
    indah "Loh Sha? Kok [mcname] ga disuruh duduk?"
    indah "Sini duduk, ini tehnya diminum dulu yuk."
    marsha4 "Gausah."
    marsha4 "Minum aja sambil berdiri."
    hide indah
    show indah_angry
    indah_angry "Hush!" with hpunch
    indah_angry "Sha, kok kamu gitu sih."
    marsha4 "Biarin aja."
    marsha4 "Dia mau langsung pulang kok."
    indah_angry "Ga boleh gitu Marsha..."
    hide indah_angry
    show indah_smile
    indah_smile "Ayo kalian duduk dulu, temenin aku minum teh."
    mcname "Iya."
    mcname "Makasih kak Indah."
    hide indah_smile
    "Akhirnya [mcname] duduk, walaupun berbeda sofa sama Marsha dan kak Indah"
    scene ruang tamu with fade
    show indah
    indah "Kalian kenapa sih? Lagi berantem?"
    marsha_angry "..."
    hide marsha_angry
    hide indah
    $quick_menu = False
    menu:
        "Gatau kak. Marsha nyuekin aku dari kemarin.":
            jump dapur

label dapur:
    $ renpy.block_rollback()
    $quick_menu = True
    show indah
    marsha4 "Dih apaan sih. Kok playing victim gitu?"
    hide indah
    show indah_angry
    indah_angry "Hei. Udah udah."
    hide indah_angry
    show indah_smile
    indah_smile "Yang lagi mau dirayain ulang tahunnya kok sewot banget."
    marsha4 "Abis si..."
    marsha3 "Eh... Apa?"
    stop music
    hide indah_smile
    show atin_happy at right with dissolve
    show ashel_happy at right:
        xpos 0.75
    with dissolve
    show freya_happy at left:
        xpos 0.25
    with dissolve
    show azizi_happy at left with dissolve
    play music "audio/sfx/confetti.mp3" noloop
    semua "HAPPY BIRTHDAY MARSHA!" with vpunch
    hide atin_happy
    hide ashel_happy
    hide freya_happy
    hide azizi_happy
    show cake with dissolve
    play music "audio/bgm/kelas.mp3"
    azizi1 "Yey!" with vpunch
    azizi1 "Selamat ulang tahun Marsha! I love youuuu."
    freya1 "Selamat ulang tahun Ca! Wish you all the best."
    ashel1 "Uuuu happy birthday bestieee. Muach muach."
    atin1 "Habede yak. Keren dah lu."
    hide azizi1
    hide freya1
    hide ashel1
    hide atin1
    hide cake
    show marsha_cry
    "Marsha menengok ke arah [mcname]."
    hide marsha_cry
    $quick_menu = False
    menu:
        "Eum... Selamat ulang tahun ya. Aku gak lupa kok hehehe.":
            jump dapur3

label dapur3:
    $ renpy.block_rollback()
    $quick_menu = True
    hide azizi
    hide freya
    hide ashel
    hide atin
    show indah_happy
    indah_happy "Happy birthday adikku sayang."
    indah_happy "Panjang umur, sehat selalu ya."
    hide indah_happy
    show marsha_cry
    marsha_cry "Eung... Teman-teman makasih ya."
    marsha_cry "Gue pikir kalian ngelupain ulang tahun gue."
    marsha_cry "Gue udah suudzon banget kemaren seharian."
    show marsha_cry at center, bounce
    marsha_cry "Pokoknya sayang kalian banyak-banyak, maengs!"
    hide marsha_cry
    "Mereka merayakan bersama-sama di rumah Marsha."
    stop music  

    call credits5 from _call_credits5   

    return

label credits5:
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

    label skip_credits5:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return