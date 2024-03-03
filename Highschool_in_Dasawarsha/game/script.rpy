# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.

label start:
    if config.main_menu_music is not None:
        stop music fadeout 1.0

label perkenalan:
    scene kelas with dissolve
    play music "audio/dream/vntrack01.mp3"
    marsha "Halo"
    show marsha with dissolve
    $ marsha_name = Character("Marsha")
    marsha "Sebelum lanjut boleh kenalan?"
    marsha "Nama kamu siapa?"

    label namemc:
    $ mcname = ""
    $renpy.call_screen("name_input", "Silahkan masukkan nama", ok_action=Jump("processmcname"), output_var="mcname")

    label processmcname:
    if not mcname or mcname == "" : 
        $renpy.call_screen("popup_message","Wajib memasukkan nama!", ok_action=Jump("namemc"))

    hide marsha
    show marsha_happy at bounce, center
    marsha_happy "[mcname] ya? Namanya bagus banget! (>.<)9"
    hide marsha_happy
    show marsha
    marsha "Kalo gitu kita lanjut main ya, selamat menikmati!"

    jump gerbang

    
label gerbang:
    $ renpy.block_rollback()
    scene pager with fade
    play music "audio/sfx/bird.mp3" noloop
    "Depan sekolah Dasawarsha"
    "Waktu menunjukkan pukul 06.30 AM"
    mcname "Pagi yang indah."
    mcname "Hari pertama kegiatan belajar mengajar di tahun terakhir SMA. Sekarang aku seorang senior. Saatnya berburu junior-junior gemas hehe..."
    $ marsha_name = Character("????")
    stop music
    marsha "[mcname]!!!" with vpunch
    marsha "Ihh tungguin!" with vpunch
    play music "audio/bgm/beautiful_sunrise.mp3"
    show marsha with dissolve
    $ marsha_name = Character("Marsha")
    marsha "Pagi [mcname]."
    mcname "Pagi Sha. Tumben kamu baru dateng? Aku kira kamu udah di kelas."
    hide marsha
    show marsha_happy
    marsha_happy "Aku lupa set alarm jadi kesiangan hehehe."
    hide marsha_happy
    show marsha
    marsha "Btw kita sekelas lagi? 12 IPS A?"
    mcname "Iya. Yuk."
    marsha "Eh eh bentar deh, aku mau nanya sesuatu."
    mcname "Apa?"
    marsha "Inget gak hari ini hari apa?"
    hide marsha
    $quick_menu = False
    menu:
        "Inget dong":
            jump gerbang1
        "Enggak":
            jump ED1
 
    return
