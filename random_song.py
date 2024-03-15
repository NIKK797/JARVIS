import os
import webbrowser
import random

def rndm():
    ramulo_a = "https://www.youtube.com/watch?v=Bg8Yb9zGYyA"
    #butab_a = "https://www.youtube.com/watch?v=2mDCVzruYzQ"
    ncho_ncho = "https://www.youtube.com/watch?v=sAzlWScHTc4"
    lst_ride = "https://www.youtube.com/watch?v=6xoB4ZiKKn0"
    arbic_kthu = "https://www.youtube.com/watch?v=KUN5Uf9mObQ"
    scam1992 = "https://www.youtube.com/watch?v=BLeOcCeqsfI"
    believer = "https://www.youtube.com/watch?v=7wtfhZwyrcc"
    #despacito = "https://www.youtube.com/watch?v=gm3-m2CFVWM"
    clubyoko = "https://www.youtube.com/watch?v=qcAb0XH5Pdg"
    play = "https://www.youtube.com/watch?v=xhaI-lLiUFA"
    sigma = "https://www.youtube.com/watch?v=LN7e69hGRS8"


    songs = [ramulo_a, ncho_ncho, lst_ride, arbic_kthu, scam1992,believer,clubyoko,play,sigma]
    random_selector = random.choice(songs)
    webbrowser.open(random_selector)


