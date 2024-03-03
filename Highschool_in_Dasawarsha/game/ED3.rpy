label kelas2:
    $ renpy.block_rollback()
    $ quick_menu = True
    show freya at left:
        xpos 0.20
    show marsha at right:
        xpos 0.85
    marsha "Ok deh. Guys kabarin guru ya kalo gue belum balik. Bilangin gue lagi dipanggil Bu Jesslyn."
    hide marsha
    hide freya
    show azizi_happy at left
    show ashel_happy
    show atin_happy at right
    semua "OKEEEEE!!!" with vpunch
    hide azizi_happy
    hide ashel_happy
    hide atin_happy
    show azizi at left
    show ashel
    show atin at right
    "Marsha kemudian pergi untuk bertemu Bu Jesslyn"
    show ashel at right:
        xpos 0.75
    with moveinright
    show azizi at left:
        xpos 0.25
    with moveinleft
    show freya at left with moveinleft
    azizi "[mcname], lu udah ada rencana belom?"
    mcname "Hah? Rencana? Rencana Apa?"
    hide azizi
    show azizi_angry at left:
        xpos 0.25
    azizi_angry "Hah?!"
    azizi_angry "Marsha kan hari ini ulang tahun!"
    mcname "Hah?"
    mcname "Oh iya!"
    hide azizi atin_angry
    show azizi at left:
        xpos 0.25
    mcname "Astaga... Pantes dia tadi pagi nanyain."
    ashel "Dia tadi nanyain lu?"
    mcname "Iya."
    atin "Eh eh sini ngumpul deh."

    jump kumpul

label kumpul:
    $ renpy.block_rollback()
    stop music
    scene kelas with fade
    show atin at right
    show ashel at right:
        xpos 0.75
    show azizi at left:
        xpos 0.25
    show freya at left
    play music "audio/bgm/curious_kid.mp3"
    azizi "Jadi gimana, ada yang punya ide?"
    atin "Rayain di sekolah aja. Pas pulang sekolah."
    ashel "Eh bagus tuh."
    freya "Oh, gue tau tepat kue kesukaan Marsha. Kita beli di situ aja."
    azizi "Boleh boleh, tapi beli apa aja ya?"
    mcname "Lilin, balon, kue, hiasan dikit."
    ashel "Iya kayaknya itu aja ya."
    freya "Kado gimana?"
    atin "Kalo kado..."
    stop music
    jinan "Ekhem"
    hide azizi
    hide atin
    hide ashel
    hide freya
    show jinan with dissolve
    play music "audio/bgm/kittens.mp3"
    jinan "Wah asik banget ya ngobrolnya sampai gak sadar bel masuk."
    azizi3 "Bu Jinan?!"
    freya2 "Ma... Maaf bu."
    atin2 "Wadoh ada Bu Jinan..."
    ashel3 "B-B-Bu Jinan?"
    $ jinan_name = Character("Bu Jinan")
    jinan "Sudah, balik ke tempat duduk masing-masing."
    hide jinan
    "Kelimanya kembali ke kursi masing-masing."
    show jinan_serious
    jinan_serious "Hm? Ini bangku kosong siapa?"
    ashel2 "Marsha lagi dipanggil Bu Jesslyn, Bu."
    jinan_serious "Hari pertama udah dipanggil ke ruang guru? Ngapain lagi itu anak satu."
    jinan_serious "Azizi, tolong pimpin doa. Habis ini kita langsung masuk materi ya."
    azizi2 "Baik bu."
    hide jinan_serious
    show kelas with fade
    "Ditengah pelajaran."
    show azizi
    azizi "Guys, bahasannya kita lanjut pas istirahat ya. Kita rahasiakan dulu ini dari Marsha, ok?"
    hide azizi
    show freya at left
    show ashel
    show atin at right
    semua "Siap!"
    hide ashel
    hide freya
    hide atin

    jump istirahat

label istirahat:
    $ renpy.block_rollback()
    stop music
    scene kantin with wipeleft
    show atin at right with Dissolve(0.4)
    show ashel at right:
        xpos 0.75
    with Dissolve(0.4)
    show azizi at left:
        xpos 0.25
    with Dissolve(0.4)
    show freya at left with Dissolve(0.4)
    play music "audio/bgm/kantin.mp3"
    atin "Ini kita gapapa di kantin?"
    azizi "Tadinya mau di ruang OSIS tapi ada Marsha sama beberapa adek kelas di ruang OSIS."
    freya "Btw Marsha gak curiga kan?"
    mcname "Enggak. Aman."
    ashel "Tadi bahasan kita sudah sampai mana ya?"
    azizi "Kue, hiasan, balon. Kita belum bahas kado ya."
    freya "Karena yang lain udah patungan, kadonya sendiri-sendiri aja gimana?"
    atin "Patungan juga gapapa sih. Kecuali udah punya kado masing-masing."
    azizi "Belom sih..."
    azizi "Menurut lu gimana?"
    hide azizi
    hide ashel
    hide freya
    hide atin
    $ quick_menu = False
    menu:
        "Ngikut":
            jump istirahat2

label istirahat2:
    $ renpy.block_rollback()
    $ quick_menu = True
    show atin at right
    show ashel at right:
        xpos 0.75
    show azizi at left:
        xpos 0.25
    show freya at left
    ashel "Yeh ngomong gini tapi sebetulnya lu udah nyiapin sendiri kan."
    mcname "Sotoy."
    azizi "Yaudah kita bagi tugas deh. Ada yang beli kado sama cari ruangan."
    atin "Gue sama Ashel nyari ruangan deh."
    hide ashel
    show ashel_angry at right:
        xpos 0.75
    ashel_angry "Siapa elo nentuin jalan hidup gue, Kathrina?!" with hpunch
    hide atin
    show atin_angry at right
    atin_angry "Gausah banyak mau deh lo! Kalo kita yang nyari kado, yang ada 10 menit nyari kado, 3 jam lo keliling mall shopping!" with vpunch
    ashel_angry "Hih! Rese lo! Gamau! Gue gak mau nyari ruangan!" with hpunch
    freya "Udah udah, yaudah. Kita undi aja gimana?"
    "Mereka berlima mulai berundi"
    scene kantin with fade
    show atin_angry at right
    show ashel_angry at right:
        xpos 0.75
    show azizi at left:
        xpos 0.25
    show freya at left
    atin_angry "Kan! Batu sih lo. Ujung-ujungnya sama gue juga."
    ashel_angry "IIIISHHHH!!!!" with vpunch
    freya "Udah udah, kan udah dibagi. Nah [mcname], lu mau ikut siapa? Nyari kado atau ruangan?"
    hide ashel_angry
    hide freya
    hide azizi
    hide atin_angry
    $quick_menu = False
    menu:
        "Nyari kado deh":
            jump istirahat3
        "Nyari ruangan deh":
            jump istirahat4
        
label istirahat3:
    $ renpy.block_rollback()
    $ quick_menu = True
    show atin at right
    show ashel at right:
        xpos 0.75
    show azizi at left:
        xpos 0.25
    show freya at left
    azizi "Oke, tugas udah kebagi. Nanti kita update tugas masing-masing ya."

    jump mall

label mall:
    $ renpy.block_rollback()
    stop music
    scene mall with pixellate
    hide ashel
    hide atin
    hide azizi
    hide freya
    show azizi at right:
        xpos 0.50
    with dissolve
    show freya at left:
        xpos 0.55
    with dissolve
    play music "audio/bgm/coffee_jazz.mp3"
    azizi "Wah gue jarang banget ke mall ini. Ternyata ok juga."
    freya "Wah gue malah kaget lu jarang ke mall Zee. Padahal ini kan deket sekolah kita."
    mcname "Jadi kita mau kadoin Marsha apa?"
    zeefre "Baju! Buku!" with vpunch
    hide azizi
    show azizi_angry at right:
        xpos 0.50
    azizi_angry "Hah? Yakali masa ulang tahun 17 dikasih buku si Fre!"
    show freya_angry at left:
        xpos 0.55
    freya_angry "Baju lagi, baju lagi! Baju dia udah banyak kan. Kita harus kasih sesuatu yang memorable dong! Ih!"
    hide azizi_angry
    hide freya_angry
    show azizi at right:
        xpos 0.50
    show freya at left:
        xpos 0.55
    azizi "Hm... Make up gimana?"
    mcname "Dia aja sehari-hari cuma pake liptint."
    hide azizi
    hide freya
    show azizi_confused at right:
        xpos 0.50
    show freya_confused at left:
        xpos 0.55
    zeefre "..."
    azizi_confused "[mcname], kok lu apal sih?"
    mcname "Keliatan kali."
    hide azizi_confused
    hide freya_confused
    show azizi_sad at right:
        xpos 0.50
    show freya at left:
        xpos 0.55
    azizi_sad "Enggak ah. Gue kurang peka kali ya."
    freya "Makanya. Lu ternyata merhatiin Marsha banget ya."
    mcname "Fokus. Kita mau cari kado."
    hide azizi_sad
    show azizi at right:
        xpos 0.50
    azizi "Hmm iya iya. Denial banget."
    freya "Jadinya apa nih? Gue males kelamaan di sini, kita harus sat set sat set."
    azizi "Sumpah deh. Baju. We should give her something wearable and memorable."
    freya "Selain baju lah~"
    freya "Kan kita patungan berlima, masa baju doang."
    azizi "Outer? Celana? Sepatu?"
    azizi "Yaudah, gimana kalo kita muter dulu, abis itu kita tentuin mau beliin apa."

    jump mall2

label mall2:
    $ renpy.block_rollback()
    scene mall with fade
    hide azizi
    hide freya
    show azizi at right:
        xpos 0.50
    with dissolve
    show freya at left:
        xpos 0.55
    with dissolve
    "Setelah 2x muterin mall"
    freya "Hadeh ini gede juga ini mall. Capek gue."
    azizi "Iya. Mana tadi gue ketemu Bu Jinan sama Bu Jesslyn."
    hide freya
    show freya_confused at left:
        xpos 0.55
    freya_confused "Hah?" with vpunch
    freya_confused "Terus gimana?"
    azizi "Ya gue sapa lah. Terus mereka nanya gue ngapain sendiri di mall."
    hide freya_confused
    show freya at left:
        xpos 0.55
    freya "Lu jawab apa?"
    azizi "Gue jawab aja lagi nyari kado buat Marsha bareng kalian."
    mcname "Lu nanya gak mereka lagi ngapain?"
    azizi "Nanya dong. Mereka mau nonton katanya."
    azizi "Gak kaget sih, setau gue mereka emang temenan dari lama."
    mcname "Ih kok lu kepo sih."
    hide azizi
    show azizi_angry at right:
        xpos 0.50
    azizi_angry "Bacot lu! Liat aja nanti gue aduin ke Marsha lu ga inget hari ini ultah dia."
    mcname "Idih cepu~"
    freya "Hee udah udah. Malah berantem."
    freya "Kita jadinya beli apa ini? Udah sore banget, gue masih harus rangkum pelajaran hari ini."
    hide azizi_angry
    show azizi at right:
        xpos 0.50
    stop music
    mcname "Sepatu?"
    "Azizi dan Freya saling menatap."
    play music "audio/bgm/just_happy.mp3"
    show azizi_confused at right:
        xpos 0.50
    show freya_confused at left:
        xpos 0.55
    zeefre "Lah iya!" with vpunch
    hide azizi_confused
    show azizi_angry at right:
        xpos 0.50
    azizi_angry "Kok lu baru kepikiran sih?!"
    mcname "Y maap y."
    hide azizi_angry
    hide freya_confused
    show azizi at right:
        xpos 0.50
    show freya at left:
        xpos 0.55    
    freya "Yaudah ayo. Tadi gue ketemu toko sepatu di lantai 3."
    azizi "Lantai 4."
    freya "Lantai 3 Weh."
    hide azizi
    show azizi_angry at right:
        xpos 0.50
    azizi_angry "Lantai 4. Batu Amat."
    show freya_angry at left:
        xpos 0.55
    freya_angry "Lah, elu yang batu. Kita buktiin aja deh ayo!" with vpunch
    azizi_angry "Lah ayo!" with vpunch
    "Mereka bertiga nyari sepatu tapi perdebatan Freya dan Azizi masih berlanjut."
    stop music

    call credits3 from _call_credits3

    return

label credits3:
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

    label skip_credits3:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return