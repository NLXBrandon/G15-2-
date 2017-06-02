import music
from microbit import *
while True:
    majulah_singapura = ("C5:2","F5:2","G5:2","A5:4","A5:4","A5:2","G5:2","F5:2","E5:2","F5:4","F5:4","F5:2","E5:2","D5:2","C5:2","D5:4","C5:4","R:2","F5:2","G5:2","F5:2","E5:8","R:2","C5:2","E5:2","F5:2","G5:4","E5:4","F5:4","G5:4","A5:3","D6:1","C6:12","A5:3","A5:1","C5:6","C5:2","E5:2","G5:2","F5:12","F5:3","F5:1")
    majulah_singapura2 = ("A#5:4","D6:4","D6:4","C6:3","B5:1","C6:8","R:2","C5:2","E5,2","F5:2","G5:4","E5:4","F5:4","G5:4","A5:12","F5:3","F5:1","A#5:4","D6:4","D6:4","C6:3","B5:1","C6:16","A5:3","G5:1","F5:6","F5:2","A5:2","A#5:2","C6:16")
    repeat1 = ("C6:3","D6:1","C6:6","A#5:2","A5:2","G5:2","F5:12","F5:3","F5:1")
    repeat2 = ("C6:3","D6:1","C6:6","A#5:2","A5:2","G5:2","F5:12","R:4")

    if button_a.is_pressed():
        music.play(majulah_singapura + majulah_singapura2 + repeat1 + majulah_singapura2 + repeat2)
    if button_b.is_pressed():
        display.scroll("SG 52")



    
