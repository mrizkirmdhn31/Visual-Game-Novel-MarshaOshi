label gerbang1:
    $ renpy.block_rollback()
    $quick_menu = True
    show marsha_happy at bounce, center
    marsha_happy "Hehe..."
    hide marsha_happy
    show marsha_happy
    marsha_happy "Yaudah ayuk kita ke kelas, nanti keburu guru dateng."
    hide marsha_happy with moveoutright
    mcname "{i}Ada apaan ya hari ini?{/i}"
    mcname "{i}Gue iya-iya aja biar ga nangis soalnya.{/i}"
    mcname "{i}Yaudah inget-inget nanti aja deh.{/i}"

    jump kelas

label kelas:
    $ renpy.block_rollback()
    stop music
    scene kelas with blinds
    show marsha_happy with dissolve
    play music "audio/bgm/kelas.mp3"
    marsha_happy "Morning All!" with vpunch
    show marsha_happy at right:
        xpos 0.50
    with moveinright
    show azizi at left:
        xpos 0.55
    with moveinright
    azizi "Wah pagi-pagi udah sumringah aja. Kenapa lu?"
    marsha_happy "Hm? Gapapa, lagi seneng aja karena seseorang hehe."
    hide marsha_happy
    hide azizi
    show ashel_happy at center with dissolve
    show atin_happy at right with dissolve
    sheltin "Pagi semuaaaaaaa!" with vpunch
    show ashel_happy at right:
        xpos 0.75
    with moveinright
    show marsha at left:
        xpos 0.25
    with moveinleft
    show azizi at left with moveinleft
    marsha "Pagi Kath, pagi Cel."
    azizi "Wah ini dia dua harbatah dateng. Lu berdua emang gapernah misah ya?"
    hide ashel_happy
    show ashel_angry at right:
        xpos 0.75
    ashel_angry "Ish. Apasih. Emang Kathrina aja yang ikutin gue terus."
    hide atin_happy
    show atin_angry at right
    atin_angry "Aneh lu. Orang kita sekelas, masa jalannya beda. Kocak lu emang."
    azizi "Udah udah masih pagi udah berantem. Kompak emang."
    hide ashel_angry
    hide atin_angry
    hide marsha
    hide azizi
    show freya_smile with dissolve
    freya_smile "Pagi semuaaaaa!" with vpunch
    hide freya_smile
    show freya
    freya "Eh iya Sha, lu dicariin Bu Jesslyn tuh, disuruh ke ruangannya."
    show freya at left:
        xpos 0.20
    with moveinleft
    show marsha at right:
        xpos 0.85
    with moveinright
    marsha "Eh? Gue? Kenapa?"
    freya "Emm... Gatau. Dateng dulu aja."
    marsha "Hmm ok deh."
    marsha "[mcname], mau nemenin aku gak?"
    hide marsha
    hide freya
    $quick_menu = False
    menu:
        "Boleh":
            jump kelas1
        "Aku di kelas aja":
            jump kelas2
        
label kelas1:
    $ renpy.block_rollback()
    $quick_menu = True
    show freya at left:
        xpos 0.20
    show marsha at right:
        xpos 0.85
    marsha "Nanti kalo ada guru tolong bilangin ya kita dipanggil Bu Jesslyn."
    hide freya
    hide marsha

    jump koridor

label koridor:
    $ renpy.block_rollback()
    stop music
    scene lorong with irisin
    show marsha with dissolve
    play music "audio/bgm/beautiful_sunrise.mp3"
    marsha "Kira-kira Bu Jesslyn kenapa nyariin kita ya?"
    mcname "Kamu. Aku kan cuma ikut."
    marsha "Kan kita terhitung sepasang."
    mcname "Hah?"
    hide marsha
    show marsha_happy at center, bounce
    marsha_happy "Becanda-becanda. Udah ayuk. jangan diem aja."
    hide marsha_happy
    stop music
    "Tiba-tiba mereka bertemu kepala sekolah tercinta."
    show theo with dissolve
    play music "audio/bgm/sneaking_out.mp3"
    theo "Eh nak Marsha, nak [mcname]. Sehat kalian?"
    hide theo
    $ quick_menu = False
    menu:
        "Sehat pak. Bapak sedang apa?":
            jump coridor2

label coridor2:
    $ renpy.block_rollback()
    $ quick_menu = True
    hide theo
    show theo_smile
    theo_smile "Ah, ini. Saya habis masang poster tapi kok bentuknya jadi aneh ya."
    show theo_smile at left:
        xpos 0.20
    with moveinleft
    show marsha at right:
        xpos 0.85
    with moveinright
    marsha "...."
    marsha "Pak, ini posternya kebalik."
    hide theo_smile
    show theo_speak at left:
        xpos 0.20
    theo_speak "Oalah pantesan hehehe."
    hide theo_speak
    show theo_smile at left:
        xpos 0.20
    theo_smile "Kalian sendiri kok gak di kelas? Ini udah mau bel masuk lho."
    marsha "Kami mau ke ruangan guru pak. Dicari bu Jesslyn."
    theo_smile "Penting?"
    marsha "Eum... Belum tau sih pak."
    hide theo_smile
    show theo_speak at left:
        xpos 0.20
    theo_speak "Kalau bantuin saya dulu mau gak?"
    hide theo_speak
    show theo_smile at left:
        xpos 0.20
    hide marsha
    show marsha_confused at right:
        xpos 0.85
    marsha_confused "Hmm... [mcname]?"
    mcname "{i}Ampun kenapa ngorbanin gue.{/i}"
    hide marsha_confused
    hide theo_smile
    $ quick_menu = False
    menu:
        "Apa yang bisa kami bantu pak?":
            jump koridor3

label koridor3:
    $ renpy.block_rollback()
    $ quick_menu = True
    show theo_smile at left:
        xpos 0.20
    show marsha at right:
        xpos 0.85
    theo_smile "Sebetulnya bisa benerin poster ini sendiri."
    theo_smile  "Hanya saja kehadiran saya sudah ditunggu sama ibu ketua komite di ruang rapat. Saya boleh minta tolong kalian benerin ini?"
    hide marsha
    show marsha_happy at right, bounce:
        xpos 0.85
    marsha_happy "Bisa bisa pak. Serahkan pada kami!"
    show marsha_happy at right:
        xpos 0.85
    theo_smile "Hahaha, baiklah. Ada gunting dan lakban di atas meja kerja saya, diambil saja nanti. jangan lupa dikembalikan."
    hide theo_smile
    hide marsha_happy

    jump kepsek

label kepsek:
    $ renpy.block_rollback()
    stop music
    scene kepsek with pixellate
    show marsha with dissolve
    play music "audio/bgm/sneaking_out.mp3"
    marsha "Nah ini gunting sama lakbannya udah ketemu."
    marsha "Ayo, biar Bu Jesslyn gak kelamaan nunggu."
    mcname "Bentar deh Sha."
    hide marsha
    show marsha_angry
    marsha_angry "Ehh, ayo ih! Gak sopan ah ini ruangan Pak Theo lho."
    mcname "Bentar, kamu gak penasaran apa?"
    marsha_angry "Apa? Rahasia Pak Theo? Emang Pak Theo nyembunyiin apa sih?"
    mcname "Nih liat"
    hide marsha_angry
    show marsha_confused
    marsha_confused "Hah?!" with hpunch
    marsha_confused "Ini kan..."
    stop music
    mcname "Eh ada yang dateng."
    hide marsha_confused
    show theo with dissolve
    play music "audio/bgm/sneaking_out.mp3"
    theo "Lho kalian masih disini?"
    show theo at right:
        xpos 0.87
    with moveinright
    show marsha at left:
        xpos 0.25
    with moveinleft
    marsha "Eh iya pak, baru ketemu gunting sama lakbannya. Hehe."
    hide theo
    show theo_smile at right:
        xpos 0.87
    theo_smile "Oh iya. Yasudah. Saya cuma mau ambil beberapa berkas yang ketinggalan."
    stop music
    hide marsha
    hide theo_smile
    play music "audio/sfx/search.mp3" noloop
    "Pak Theo mencari berkas yang berada di lemarinya."
    show theo_speak at right:
        xpos 0.87
    show marsha at left:
        xpos 0.25
    play music "audio/bgm/sneaking_out.mp3"
    theo_speak "Kalau udah langsung balik ke kelas ya kalian."
    hide theo_speak
    show theo at right:
        xpos 0.87
    marsha "Baik pak."
    hide theo
    hide marsha
    stop music

    jump koridor4

label koridor4:
    $ renpy.block_rollback()
    scene lorong with irisin
    play music "audio/bgm/sneaking_out.mp3"
    show marsha at center
    hide marsha
    show marsha_confused
    marsha_confused "Kertas yang tadi, diambil ya?"
    mcname "Iya."
    hide marsha_confused
    show marsha_angry
    marsha_angry "Abaikan dulu aja. Kita kerjain ini terus ke Bu Jesslyn dulu, aku gak enak udah kelamaan."
    hide marsha_angry
    
    jump bk 

label bk:
    $ renpy.block_rollback()
    stop music
    scene kepsek with squares
    play music "audio/sfx/knock.mp3" noloop
    "Marsha mengetuk pintu."
    show marsha
    marsha "Permisi Bu Jesslyn. Ibu mencari saya?"
    hide marsha
    show jeji with dissolve
    play music "audio/bgm/autumn_fall.mp3"
    jeji "Ah, iya. Masuk Marsha."
    jeji "Oh, ada [mcname] juga. Baguslah, lebih banyak orang lebih mudah dikerjakan."
    show jeji at left:
        xpos 0.17
    with moveinleft
    show marsha at right:
        xpos 0.87
    with moveinright
    jeji "Jadi, maksud saya memanggil kamu itu saya mau minta tolong lengkapi data-data anak kelas kalian."
    jeji "Kalian kan sudah kelas 12, akan sibuk ujian sekolah dan ujian masuk perguruan tinggi. Nah ibu mau buat survey peminatan untuk kelas kalian."
    hide marsha
    show marsha_happy at right:
        xpos 0.87
    marsha_happy "Wah, seru nih. Kamu mau kuliah dimana [mcname]?"
    hide marsha_happy
    show marsha at right:
        xpos 0.87
    mcname "Hm? Gak tau."
    hide marsha
    show marsha_angry at right:
        xpos 0.87
    marsha_angry "Masa udah kelas 12 masih gatau mau kuliah dimana ckckck."
    mcname "Kayak kamu udah tau aja."
    hide marsha_angry
    show marsha_happy at bounce, right:
        xpos 0.87
    marsha_happy "Udah dong! Wlee!"
    hide marsha_happy
    show marsha at right:
        xpos 0.87
    jeji "Emang Marsha mau kuliah dimana jurusan apa?"
    hide marsha
    show marsha_happy at right:
        xpos 0.87
    marsha_happy "Aku mau masuk DKV bu. Di kampus X, katanya DKVnya bagus."
    hide jeji
    show jeji_smile at left:
        xpos 0.17
    jeji_smile "Wah, keren banget. Ibu seneng deh kamu udah tau sama passionmu."
    hide jeji_smile
    show jeji at left:
        xpos 0.17
    hide marsha_happy
    show marsha at right:
        xpos 0.87
    jeji "Kalau [mcname] kenapa masih bingung?"
    mcname "Saya masih belum tau minat saya ke mana aja sih bu."
    jeji "Hmm, masih ada waktu 15 menit sampai bel pertama. Gimana kalau kalian di sini dulu dan konsultasi sama saya?"
    hide marsha
    show marsha_happy at right, bounce:
        xpos 0.87
    marsha_happy "Mau bu. Kalo Kamu gimana [mcname]?"
    hide jeji
    hide marsha_happy
    $ quick_menu = False
    menu optional_name:
        "Mau.":
            jump bk1
        
label bk1:
    $ renpy.block_rollback()
    $ quick_menu = True
    hide jeji
    hide marsha
    show jeji_smile at left:
        xpos 0.17
    show marsha_happy at right:
        xpos 0.87
    "Marsha, [mcname], Bu Jesslyn ngobrol bareng di ruang guru."
    stop music

    call credits2 from _call_credits2

    return

label credits2:
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

    label skip_credits2:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return
