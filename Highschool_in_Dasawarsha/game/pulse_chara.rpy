# Default image marsha pulse

image marsha speaking=At("images/Characters/marsha.png", pulse)
image marsha_happy speaking=At("images/Characters/marsha_happy.png", pulse)
image marsha_cry speaking=At("images/Characters/marsha_cry.png", pulse)
image marsha_angry speaking=At("images/Characters/marsha_angry.png", pulse)
image marsha_confused speaking=At("images/Characters/marsha_confused.png", pulse)
image marsha_blinded speaking=At("images/Characters/marsha_blinded.png", pulse)

# Default image azizi pulse

image azizi speaking=At("images/Characters/azizi.png", pulse)
image azizi_happy speaking=At("images/Characters/azizi_happy.png", pulse)
image azizi_angry speaking=At("images/Characters/azizi_angry.png", pulse)
image azizi_smile speaking=At("images/Characters/azizi_smile.png", pulse)
image azizi_confused speaking=At("images/Characters/azizi_confused.png", pulse)
image azizi_sad speaking=At("images/Characters/azizi_sad.png", pulse)

# Default image ashel pulse

image ashel speaking=At("images/Characters/ashel.png", pulse)
image ashel_happy speaking=At("images/Characters/ashel_happy.png", pulse)
image ashel_angry speaking=At("images/Characters/ashel_angry.png", pulse)
image ashel_shock speaking=At("images/Characters/ashel_shock.png", pulse)


# Default image atin pulse

image atin speaking=At("images/Characters/atin.png", pulse)
image atin_happy speaking=At("images/Characters/atin_happy.png", pulse)
image atin_angry speaking=At("images/Characters/atin_angry.png", pulse)
image atin_shocked speaking=At("images/Characters/atin_shocked.png", pulse)
image atin_mock speaking=At("images/Characters/atin_mock.png", pulse)

# Default image freya pulse

image freya speaking=At("images/Characters/freya.png", pulse)
image freya_happy speaking=At("images/Characters/freya_happy.png", pulse)
image freya_smile speaking=At("images/Characters/freya_smile.png", pulse)
image freya_angry speaking=At("images/Characters/freya_angry.png", pulse)
image freya_confused speaking=At("images/Characters/freya_confused.png", pulse)

# Default image jinan pulse

image jinan speaking=At("images/Characters/jinan.png", pulse)
image jinan_smile speaking=At("images/Characters/jinan_smile.png", pulse)
image jinan_happy speaking=At("images/Characters/jinan_happy.png", pulse)
image jinan_serious speaking=At("images/Characters/jinan_serious.png", pulse)

# Default image indah pulse

image indah speaking=At("images/Characters/indah.png", pulse)
image indah_smile speaking=At("images/Characters/indah_smile.png", pulse)
image indah_happy speaking=At("images/Characters/indah_happy.png", pulse)
image indah_angry speaking=At("images/Characters/indah_angry.png", pulse)

# Default image jeji pulse

image jeji speaking=At("images/Characters/jeji.png", pulse)
image jeji_smile speaking=At("images/Characters/jeji_smile.png", pulse)
image jeji_happy speaking=At("images/Characters/jeji_happy.png", pulse)
image jeji_serious speaking=At("images/Characters/jeji_serious.png", pulse)

# Default image theo pulse

image theo speaking=At("images/Characters/theo.png", pulse)
image theo_smile speaking=At("images/Characters/theo_smile.png", pulse)
image theo_speak speaking=At("images/Characters/theo_speak.png", pulse)

# Expression image chara pulse

define config.speaking_attribute = "speaking"

# Size Item

image cake:
    "cake.png"
    size(720, 720)
    yalign 0.4

image kalung:
    "kalung.png"
    size(650, 650)
    yalign 0.4

transform pulse:
    zoom 1.07
    # easein 0.2 zoom 1.05
    # easeout 0.2 zoom 1.0

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform moveright:
    linear 0.5 xpos 0.85
