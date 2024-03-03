label istirahat4:
    $ renpy.block_rollback()
    $ quick_menu = True
    show atin at right
    show ashel at right:
        xpos 0.75
    show azizi at left:
        xpos 0.25
    show freya at left
    azizi "Oke, tugas udah kebagi. Nanti kita update tugas masing-masing ya."

    jump kelas3

label kelas3:
    $ renpy.block_rollback()
    stop music
    hide atin
    hide ashel
    hide azizi
    hide freya 
    scene kelas with irisin
    show ashel_angry at right:
        xpos 0.50
    with dissolve
    show atin at left:
        xpos 0.55
    with dissolve
    play music "audio/bgm/sneaking_out.mp3"
    ashel_angry "Hadeh... Kenapa gue harus kejebak sama lu berdua sih."
    hide atin
    show atin_angry at left:
        xpos 0.55
    atin_angry "Yaudah sih julid amat. Untung aja ada [mcname], kalo gak bisa gila gue dengerin lo misah-misuh."
    hide ashel_angry
    show ashel at right:
        xpos 0.50
    ashel "Jadi mau pake ruang mana? Ruang kelas aja?"
    hide atin_angry
    show atin at left:
        xpos 0.55
    atin "Ruang kelas mana? Kita kan tiap hari kelasnya pindah-pindah."
    mcname "Ruang kelas kita terakhir pas pelajaran besok aja."
    atin "Nah. Bagus tuh idenya [mcname]. Ada yang megang jadwal kelas kita seminggu gak?"
    mcname "Gue ada."
    atin "Hmm... Besok kita di lantai 2 ya."
    ashel "Eh gue belom pernah dapet kelas ini dah. [mcname] lu udah pernah belom?"
    hide ashel
    hide atin
    $ quick_menu = False
    menu:
        "Belom juga.":
            jump kelas4

label kelas4:
    $ renpy.block_rollback()
    $ quick_menu = True
    show ashel at right:
        xpos 0.50
    show atin at left:
        xpos 0.55
    ashel "Nah kan belom. Lo udah pernah Kath?"
    atin "Belom. Ini kelas baru yang abis renovasi kemarin bukan sih?"
    mcname "Kayanya iya. Mau cek dulu gak kelasnya gimana?"
    ashel "Boleh. Sekalian pulang yuk."
    hide ashel
    hide atin
    stop music
    scene lorong with squares
    show ashel at right:
        xpos 0.50
    with dissolve
    show atin at left:
        xpos 0.55
    with dissolve
    play music "audio/bgm/kelas.mp3"
    ashel "Menurut gue ok sih."
    atin "[mcname], menurut lu gimana?"
    mcname "Ok sih, kalo menurut lu?"
    hide atin
    show atin_mock at left:
        xpos 0.55
    atin_mock "KEMU NENYEA? KEMU NENYEA KELASNYA GIMANA?" with vpunch
    hide ashel
    show ashel_angry at right:
        xpos 0.50
    ashel_angry "Sumpah Kathrina gue tabok ya!!" with vpunch
    mcname "Kelasnya ok, tapi kita harus izin Bu Jinan deh kayaknya buat tektokan."
    hide ashel_angry
    hide atin_mock
    show ashel at right:
        xpos 0.50
    show atin at left:
        xpos 0.55
    ashel "Setuju. Kita harus at least ngasih tau Bu Jinan soal rencana ini."
    atin "Ngomong-ngomong rencana..."
    atin "Kayaknya kita lagi hoki banget."
    atin "Liat tuh siapa yang baru keluar dari ruang guru."
    stop music
    scene lorong with fade
    semua "BU JINAAAANNNN!!!!!" with vpunch
    hide ashel
    hide atin
    show jinan_serious with dissolve
    play music "audio/bgm/kittens.mp3"
    jinan_serious "Eh! Kaget ih. Gak usah teriak-teriak kali, ibu denger."
    show jinan_serious at right with moveinright
    show ashel at center with moveinleft
    show atin at left with moveinleft
    ashel "Ibu lagi apa? Kok masih di sekolah?"
    jinan_serious "Seharusnya ibu yang nanya gak sih kenapa kalian belom pulang? Ini udah lebih sejam dari jam pulang lho."
    ashel "Hehe... Kita ada keperluan."
    atin "Kalo ibu abis ngapain?"
    hide jinan_serious
    show jinan at right
    jinan "Abis koreksi quiz matematika kalian aja sih."
    stop music
    "[mcname] menatap curiga pada Bu Jinan."
    mcname "Bu Jinan... abis nangis ya?"
    play music "audio/bgm/regret.mp3"
    hide jinan
    show jinan_serious at right
    jinan_serious "Hah? Engg... Enggak kok."
    atin "Eh, tapi iya aku baru sadar juga mata ibu sembab. Ibu gapapa?"
    hide jinan_serious
    show jinan_smile at right
    jinan_smile "Enggak. I'm fine kids."
    hide ashel
    show ashel_happy at center
    ashel_happy "Bu Jinan, ibu kan selama ini udah jadi tempat kami cerita. Kita ga keberatan kok bu kalo ibu mau ngelakuin hal yang sama."
    atin "Bener bu! Apalagi Ashel nih, jago banget dah soal cinta-cintaan."
    hide ashel_happy
    show ashel_angry at center
    ashel_angry "Ngawur lo!" with vpunch
    hide ashel_angry
    hide jinan_smile
    show ashel
    show jinan at right
    ashel "[mcname], gimana? Lo penasaran juga kan pasti wali kelas kesayangan kita ini gimana?"
    hide ashel
    hide atin
    hide jinan
    $ quick_menu = False
    menu:
        "Yoi. Kita mau kok dengerin Bu Jinan":
            jump kelas5
        "Selesaiin urusan kita dulu aja kayaknya?":
            jump kelas6

label kelas5:
    $ renpy.block_rollback()
    $ quick_menu = True
    show jinan_smile at right
    show ashel at center
    show atin at left
    jinan_smile "Anak-anak, makasih ya. Tapi ini beneran gapapa ibu cerita?"
    hide ashel
    show ashel_happy at center
    ashel_happy "Gapapa bu."
    jinan "Yaudah. Ibu numpang curhat ya."
    hide jinan_smile
    hide ashel_happy
    hide atin
    stop music
    scene kelas with fade
    "Keesokan harinya."
    play music "audio/bgm/kelas.mp3"
    show azizi with dissolve
    azizi "Good morning~ Aku ucapkan!" with vpunch
    azizi "Hm? Kenapa ni [mcname]?"
    show freya at left with moveinleft
    freya "Dicuekin Marsha dari kemarin."
    azizi "Serius?"
    freya "Iya. Tadi aja dia pas nyamper ke bangkunya Marsha, Marsha langsung pergi keluar kelas."
    azizi "[mcname] agak dicuekin~"
    hide freya
    hide azizi
    show freya_happy at left
    show azizi_happy at center
    zeefre "Masa sih~" with vpunch
    show ashel at right with moveinright
    ashel "Waduh-waduh masih pagi aja udah lesu. Kenapa dia?"
    hide azizi_happy
    hide freya_happy
    show azizi at center
    show freya at left
    azizi "Dicuekin Marsha~ Eh btw minjem kelasnya gimana Cel? Udah belum?"
    ashel "Ah iya. itu. Kita lupa..."
    freya "Kok bisa lupa??"
    ashel "Kemarin kita udah ketemu Bu Jinan. Eh malah curhat-curhatan sampe sore hehehe..."
    hide azizi
    show azizi_sad at center
    azizi_sad "Yah terus gimana dong? Kita surprise-in dimana?"
    show azizi_sad at right:
        xpos 0.75
    with moveinright
    show freya at left:
        xpos 0.25
    with moveinleft
    show atin at left with moveinleft
    atin "Assalamualaikum warga! Eh udah ngumpul aja ni. Gimana-gimana?"
    hide azizi_sad
    show azizi at right:
        xpos 0.75
    freya "Gimana apanya. Lu kan lupa minjem ruangan buat kita suprise-in Marsha."
    hide atin
    show atin_mock at left
    atin_mock "Ashel nih curhatnya kebanyakan sampe lupa waktu."
    hide ashel at right
    show ashel_angry at right
    ashel_angry "Heh! Sadar diri ya lo curhat sampe mau nangis. Lupa lo?" with vpunch
    azizi "Udah-udah. Gausah berantem. Mending kita pikirin rencana suprise-in Marsha."
    hide atin_mock
    show atin at left
    mcname "Di rumahnya aja."
    hide ashel_angry at right
    hide atin
    hide freya
    hide azizi
    hide ashel_angry
    show ashel_shock at right
    show azizi_confused at right:
        xpos 0.75
    show freya_confused at left:
        xpos 0.25
    show atin_shocked at left
    semua "Hah?" with vpunch
    mcname "Iya, di rumah dia."
    hide atin_shocked
    hide freya_confused
    hide azizi_confused
    hide ashel_shock
    show ashel at right
    show azizi at right:
        xpos 0.75
    show freya at left:
        xpos 0.25
    show atin at left
    azizi "Tapi gimana? Kita harus bisa dateng sebelum dia pulang kan?"
    freya "Setau gue Marsha cuma tinggal sama kakaknya deh, Kak Indah. Soalnya orang tuanya kerja di luar kota dua-duanya."
    ashel "Ok tuh. Kita bisa kerjasama dengan Kak Indah. Tapi cara cegah biar Marsha gak pulang duluan gimana?"
    freya "Dipanggil Bu Jinan?"
    mcname "Gue tau."
    freya "Gimana?"
    mcname "Sini semuanya."
    mcname "{i}Fa fi fu{/i}"
    freya "Hah? Nyulik dia? Nyulik gimana?"
    mcname "{i}Was Wes{/i}"
    azizi "Lo tahan di kelas, mau minta maaf soal ulang tahunnya? Terus?"
    mcname "{i}Wus Wos{/i}"
    ashel "Oh, pinter juga. Abis itu kita ke rumahnya, nyiapin surprise. Baru lu anterin dia pulang?"
    hide atin
    show atin_happy at left
    atin_happy "Wah, gila, ga nyangka gue [mcname] bisa kepikiran. Keren lo."
    ashel "Tapi kita ke rumah Marsha naik apa?"
    atin_happy "Aman. Sama gue aja, nanti gue atur."

    jump pulang

label pulang:
    $ renpy.block_rollback()
    stop music
    hide azizi
    hide freya
    hide ashel
    hide atin_happy
    scene kelas with fade
    show marsha_angry with dissolve
    play music "audio/bgm/joy_sorrow.mp3"
    marsha_angry "Kenapa?"
    mcname "Kamu marah?"
    marsha_angry "Marah? Marah kenapa? Sama siapa?"
    mcname "Aku?"
    marsha_angry "Kamu? Ngapain aku marah ke kamu."
    mcname "Ya... Gatau. Abis dari kemarin cuek. Kamu kenapa sih?"
    marsha_angry "..."
    marsha "Aku kenapa?"
    marsha_angry "Pikir aja sendiri."
    mcname "Sha..."
    mcname "Aku bukan orang pinter."
    mcname "Kalau kamu gak cerita, aku gak tau kamu kenapa Sha."
    marsha_angry "Oh? Nyadar ya?"
    marsha_angry "Kalo kamu tuh bego?"
    stop music
    play music "audio/sfx/bego.mp3" noloop
    marsha_angry "BEGO!" with vpunch
    hide marsha_angry
    play music "audio/sfx/kursi.mp3" noloop
    "Marsha menggeser kursinya"
    show marsha_angry
    marsha_angry "Udah ah. Buang-buang waktuku aja."
    mcname "Tunggu!"
    play music "audio/bgm/joy_sorrow.mp3"
    "[mcname] berdiri lalu menahan tangan Marsha"
    marsha_angry "Apa lagi sih?!"
    mcname "Aku mau ngomong. Ikut aku ya."
    marsha_angry "..."
    marsha_angry "Ke mana?"
    hide marsha_angry
    $ quick_menu = False
    menu:
        "Aku anterin pulang, nanti aku jelasin.":
            jump pulang1
        "Ikut dulu aja.":
            jump pulang2

label pulang1:
    $ renpy.block_rollback()
    $ quick_menu = True
    show marsha_angry
    marsha_angry "Gausah. Aku bisa pulang sendiri."
    mcname "Enggak. Ikut aku dulu."
    marsha_angry "Apasih. Aku tuh gak suka dipaksa-paksa."
    stop music
    mcname "Caca!" with vpunch
    marsha_angry "...."
    mcname "Please. Ya?"
    "Marsha terdiam sejenak."
    play music "audio/bgm/joy_sorrow.mp3"
    marsha_angry "Oke."
    mcname "Tapi, tutup mata dulu deh."
    "Marsha menatap bingung, tapi dia tetap mengikuti arahan dari [mcname]."
    hide marsha_angry
    jump kejutan

label kejutan:
    $ renpy.block_rollback()
    stop music
    scene kelas with fade
    "Setelah beberapa lama."
    show marsha_blinded with dissolve
    marsha_blinded "Udah boleh buka?"
    mcname "Hm."
    hide marsha_blinded
    "Marsha membuka penutup matanya dan terkejut dengan apa yang berada di hadapannya."
    show marsha_confused
    marsha "Ini kan?"
    hide marsha_confused
    play music "audio/bgm/beautiful_sunrise.mp3"
    show cake with dissolve
    mcname "Happy Birthday, Marsha Lenathea Lapian."
    marsha3 "[mcname]? Kamu inget?"
    hide cake
    show marsha_confused
    mcname "Mana mungkin aku lupa."
    marsha_confused "Tapi kan kemaren..."
    mcname "Hehe..." 
    mcname "Sengaja. Biar gak dicurigain."
    "Marsha membuka hadiah yang diberikan oleh [mcname]."
    hide marsha_confused
    show kalung with dissolve
    marsha1 "Kalung bulan..." 
    marsha1 "Dan ada inisial M-nya..."
    hide kalung
    show marsha_happy at center, bounce
    marsha_happy "SUKA!" with vpunch
    marsha_happy "AKU SUKA BANGET!!" with vpunch
    hide marsha_happy
    show marsha_happy
    mcname "Hahaha."
    # mcname "Tada!"
    # hide marsha
    # show marsha_happy
    # marsha_happy "My favorite cheesecake?"
    mcname "Heem. Ayo. Make a wish."
    marsha_happy "I wish..."
    hide marsha_happy
    show marsha
    "Marsha mulai meniupkan lilinnya."
    "Setelahnya Marsha memeluk [mcname]."
    marsha "Makasih ya..."
    marsha "Walaupun ulang tahunnya kemarin, but..."
    hide marsha
    show marsha_happy
    marsha_happy "This is the best day ever!" with vpunch
    mcname "Hahaha, Gimana? Jadi pulang gak?"
    hide marsha_happy
    show marsha
    marsha "Enggak ah. Di sini dulu aja boleh gak?"
    mcname "Boleh dong, masa gaboleh."
    "Marsha mulai mendekatkan diri ke [mcname]."
    "Mereka berdua menikmati perayaan ulang tahun Marsha di kelas tersebut."
    marsha "Eum... [mcname]?"
    mcname "Ya?"
    stop music
    hide marsha
    marsha "{i}*cup*{/i}"
    "[mcname] terkejut tiba-tiba marsha memberikan sebuah ciuman singkat ke arah pipinya."
    play music "audio/bgm/beautiful_sunrise.mp3"
    show marsha
    mcname "C-Ca?"
    hide marsha
    show marsha_happy
    marsha_happy "Anggap saja itu hukuman karena telat ucapin ulang tahun aku."
    stop music

    # "Marsha mendekatkan bibirnya yang merah merona ke [mcname]. Kedua bibir itu saling bertemu."
    # "Marsha benar-benar merasa senang dan tidak akan melupakan kejadian hari itu."
    # "Sebuah penutup hari yang sangat indah."\

    call credits4 from _call_credits4

    return

label credits4:
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

    label skip_credit4:

        pass

    ## Re-enable the quick screen as the credits are over
    $ quick_menu = True

    #This ends the game
    return