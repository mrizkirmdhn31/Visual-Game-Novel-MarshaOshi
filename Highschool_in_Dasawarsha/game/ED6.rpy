label kelas6:
    $ renpy.block_rollback()
    $ quick_menu = True
    stop music
    show jinan at right
    show ashel at center
    show atin at left
    play music "audio/bgm/kittens.mp3"
    mcname "Oh iya! Bu kita mau izin buat pake ruangan kelas 211 besok siang boleh gak bu?"
    jinan "Hm? Buat apa memang?"
    atin "Kita mau surprise-in Marsha bu. Hari ini dia ulang tahun, tapi kita sepakat gak ucapin sekarang jadi sekalian besok. Gimana? Boleh gak bu?"
    jinan "Hmmm? Gimana ya?"
    jinan "Gak boleh sih."
    hide atin
    hide ashel
    show atin_shocked at left
    show ashel_shock at center
    ashel_shock "Yah bu..."
    hide jinan
    show jinan_smile at right
    jinan_smile "Hehe, saya juga mau dong ikut surprise-in Marsha."
    hide atin_shocked
    hide ashel_shock
    show atin_happy at left
    show ashel_happy at center
    atin_happy "Wah boleh banget bu. Kalo gitu besok siang pulang sekolah ya bu?"
    hide jinan_smile
    show jinan at right
    jinan "Ok deh. Yaudah gih kalian pulang sana, gak balik di sekolah kesorean."
    ashel_happy "Aman bu. Makasih ya Bu Jinan. Kami pamit pulang dulu."
    hide jinan
    hide ashel_happy
    hide atin_happy
    stop music
    scene kelas with fade
    "Jam istirahat"
    play music "audio/bgm/kelas.mp3"
    show atin at right
    show ashel at right:
        xpos 0.75
    show azizi at left:
        xpos 0.25
    show freya at left
    azizi "Gimana? Ruangan aman?"
    ashel "Aman. Kado gimana Zee?"
    azizi "Aman. Berarti tinggal gimana caranya nahan Marsha di sekolah sambil kita nyiapin ya? Ada yang punya ide?"
    azizi "[mcname]?"
    mcname "Jangan gue. Gue aja didiemin dari kemarin."
    azizi "Pantes lu surem seharian ini. Terus gimana? Yang lain?"
    freya "Bu Jinan mau ikutan kan? Kita minta tolong Bu Jinan aja."
    azizi "Caranya?"
    freya "Kita minta Bu Jinan buat manggil Marsha ke dia. Nanti selama Marsha menghadap Bu Jinan, kita eksekusi rencana deh."
    azizi "Tapi bakal aneh gak sih? Masalahnya kan dia ga ngapa-ngapain."
    mcname "Bu Jesslyn."
    mcname "Kita minta Bu Jesslyn panggil Marsha ke ruang guru. Minta Bu Jinan ikut juga. Selama mereka di sana, kita siapin kelasnya."
    azizi "Boleh tuh. Bisa bisa."
    azizi "Siapa yang mau ngomong ke Bu Jesslyn?"
    mcname "Gue aja. Nanti gue pura-pura nemenin dia ke sana."
    azizi "Oke deh. Berarti pada udah tau tugas masing-masing ya?"
    azizi "Sip, kalo gitu tos dulu."
    hide azizi
    show azizi_smile at left:
        xpos 0.25
    azizi_smile "Marsha birthday party..."
    hide freya
    hide ashel
    hide atin
    show freya_happy at left
    show atin_happy at right
    show ashel_happy at right:
        xpos 0.75
    semua "Gaas!" with vpunch
    hide azizi
    hide freya
    hide ashel
    stop music
    scene kelas with fade
    show marsha with dissolve
    play music "audio/bgm/beautiful_sunrise.mp3"
    marsha "Duluan ya semua."
    mcname "Tunggu Sha."
    hide marsha
    show marsha_angry
    marsha_angry "Kenapa?"
    mcname "Kamu kenapa sih? Dari kemarin ngediemin aku?"
    marsha_angry "Gak, ah. Emang kamu ngerasa didiemin?"
    mcname "Sha, serius. Kamu kenapa?"
    marsha_angry "Aku gapapa. Udah ya, aku mau pulang."
    play music "audio/sfx/knock.mp3" noloop
    hide marsha_angry
    "Tiba-tiba terdengar suara ketukan pintu"
    show jinan with dissolve
    play music "audio/bgm/kittens.mp3"
    jinan "Ah, pas banget kalian masih ada. Marsha sama [mcname]." 
    jinan "Ikut saya ayo ke ruang guru. Ada yang mau dibicarakan dengan Bu Jesslyn."
    show jinan at left:
        xpos 0.17
    with moveinright
    show marsha_confused at right:
        xpos 0.87
    with moveinright
    marsha_confused "Perihal apa ya bu? Soalnya kemarin pagi saya udah ke ruangan Bu Jesslyn juga."
    jinan "Saya gak tau. Jadi ikut aja dulu ya. Kamu juga [mcname]."
    hide marsha_confused
    show marsha at right:
        xpos 0.87
    marsha "Baik bu."
    hide marsha
    hide jinan
    stop music
    scene kepsek with fade
    show jeji at right with dissolve
    show jinan at center with dissolve
    show marsha at left with dissolve
    play music "audio/bgm/autumn_fall.mp3"
    jeji "Duduk Marsha, [mcname]. Untung saja kalian belum pulang ya."
    marsha "Maaf bu, tapi perihal apa ya memanggil kami ke sini?"
    hide jeji
    hide jinan
    show jinan_serious at center
    show jeji_serious at right
    jeji_serious "Nilai." 
    jeji_serious "Saya baru cek raport kalian dari kelas 10 sampai terakhir kemarin. Saya jujur agak gimana gitu sama nilai rapot kamu Marsha."
    hide marsha
    show marsha_confused at left
    marsha_confused "Maksudnya bu?"
    jeji_serious "Kamu tau kan nilai rapot minimal yang harus kamu punya untuk diterima di PTN yang kamu mau itu cukup tinggi? Nilaimu masih jauh dari angka tersebut, Marsha."
    jinan_serious "Saya liat juga kamu banyak bengong 2 hari ini di kelas. Ada apa Marsha? Apa yang menganggumu?"
    hide marsha_confused
    show marsha_cry at left
    "Marsha melihat ke arah [mcname]."
    mcname "{i}Ampun kenapa malah liatin gue.{/i}"
    marsha_cry "Maaf bu. Saya tidak akan ulangi kembali. Untuk nilai saya, saya janji akan rajin belajar di semester ini supaya bisa mendaftar ke PTN yang saya incar."
    jeji_serious "Kalo kamu [mcname], ke mana kemarin sepulang sekolah? Kita sudah janjian kan untuk melanjutkan obrolan soal pilihan universitas dan jurusanmu."
    mcname "Err... Anu. Saya kemarin ada keperluan."
    jeji_serious "Jangan diulangi. Tidak sopan melanggar janji yang sudah dibuat. Apalagi sama guru sendiri."
    hide marsha_cry
    hide jinan_serious
    hide jeji_serious
    $ quick_menu = False

    menu:
        "Maaf bu. Tidak akan saya ulangi lagi.":
            jump kelas7

label kelas7:
    $ renpy.block_rollback()
    $ quick_menu = True
    show jeji at right
    show jinan at center
    show marsha_cry at left
    jinan "Ya sudah. Kalian sudah boleh pulang. Jangan lupa ambil tas kalian di kelas ya."
    stop music
    hide jeji
    hide jinan
    hide marsha_cry
    scene lorong with fade
    show marsha_cry with dissolve
    play music "audio/bgm/beautiful_sunrise.mp3"
    marsha_cry "Maafin aku ya ngediemin kamu dari kemarin. Aku gak nyangka imbasnya bakal ke konsentrasi aku juga di kelas."
    mcname "Sama. Aku minta maaf juga ya."
    hide marsha_cry
    show marsha
    marsha "Kamu ke mana hari ini? Mau makan dulu gak?"
    hide marsha
    show marsha_happy at center, bounce
    marsha_happy "Traktiran aku."
    hide marsha_happy
    show marsha
    mcname "Aku udah ada rencana."
    marsha "Ohh gitu. Oke deh."
    mcname "Eh tapi kan sama kamu juga."
    hide marsha
    show marsha_confused
    marsha_confused "Maksudnya? Kapan kita janjian?"
    mcname "Hmm... Gak ada janjian, sih."
    stop music
    mcname "Tapi kita mau rayain ulang tahun kamu kan."
    mcname "Selamat ulang tahun ya, Marsha Lenathea."
    hide marsha_confused
    play music "audio/sfx/open.mp3" noloop
    "[mcname] membuka pintu ruang kelas"
    hide marsha_confused
    show atin_happy at right with dissolve
    show ashel_happy at right:
        xpos 0.75
    with dissolve
    show azizi_smile at left:
        xpos 0.25
    with dissolve
    show freya_happy at left with dissolve
    play music "audio/sfx/confetti.mp3" noloop
    semua "HAPPY BIRTHDAY MARSHA!!!" with vpunch
    hide atin_happy
    hide ashel_happy
    hide freya_happy
    hide azizi_smile
    show cake with dissolve
    play music "audio/bgm/happy.mp3"
    azizi1 "Yeay!" with vpunch
    azizi1 "Selamat ulang tahun Marsha! I love you!"
    freya1 "Selamat ulang tahun Ca! Wish you all the best!"
    ashel1 "Uuuuu happy birthday bestiiieeee! Muach muach."
    atin1"Habede yak. Keren dah lu."
    hide cake
    $ quick_menu = False
    menu:
        "Eum... Selamat ulang tahun ya. Aku gak lupa kok hehehe.":
            jump kejutan1

label kejutan1:
    $ renpy.block_rollback()
    $ quick_menu = True
    hide azizi
    hide freya
    hide ashel
    hide atin
    show marsha_cry
    marsha_cry "Eung..."
    marsha_cry "Temen-temen makasih ya."
    mcname "Jiah dia nangis..."
    hide marsha_cry
    show jinan at left:
        xpos 0.55
    with moveinleft
    show jeji at right:
        xpos 0.45
    with moveinleft
    jinan "Wah ada apa nih rame-rame kok ibu gak diajak."
    semua "Bu Jinan! Bu Jesslyn!" with vpunch
    hide jinan
    show jinan_happy at left:
        xpos 0.55
    jinan_happy "Selamat ulang tahun ya, Marsha."
    jinan_happy "Maaf ibu emang sekongkolan sama temen-temen yang lain."
    jinan_happy "Pokoknya sehat terus dan panjang umur!"
    marsha2 "Huhuh, Bu Jinan terima kasih."
    marsha2 "Aku udah takut banget tadi kirain beneran."
    hide jeji
    hide jinan_happy
    show jeji_happy at right:
        xpos 0.45
    show jinan at left:
        xpos 0.55
    jeji_happy "Hahaha. Yang tadi bohongan kok, Sha."
    jeji_happy "Selamat ulang tahun ya. Ibu doakan kesuksesan dan kebahagiaan selalu mengikuti di mana pun kamu berada."
    hide jeji_happy
    hide jinan
    show marsha_happy
    marsha_happy "Terima kasih Bu Jesslyn."
    azizi1 "Eh ayo tiup lilin sama potong kue dulu dong."
    marsha_happy "Ok!"
    marsha_happy "Gue pikir kalian ngelupain ulang tahun gue."
    marsha_happy "Gue udah suudzon banget kemaren seharian."
    hide marsha_happy
    show marsha_happy at center, bounce
    marsha_happy "Pokoknya sayang kalian banyak-banyak, maengs!"
    hide marsha_happy
    "Mereka merayakan bersama-sama di kelas."
    stop music

    call credits6 from _call_credits6

    return

label credits6:
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

    label skip_credits6:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return