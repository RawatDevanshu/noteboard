import pygame
from pyo import *


qwert ={'z': 1, 's': 2, 'x': 3, 'd': 4, 'c': 5, 'v': 6, 'g': 7, 'b': 8, 'h': 9, 'n': 10, 'j': 11, 'm': 12, ',': 13}


def freqval(char):
    try:
        n = qwert[char]
    except:
        return 0
    a = 1.05946309436
    return 261*(a**n)  #base freq ==261HZ Note = "C4"

s = Server(sr = 48000).boot()
s.start()

pygame.init()
screen = pygame.display.set_mode((400,300))

lst = [];adsr = Adsr(decay=1,sustain=-70);freql=[]

while True:
    for event in pygame.event.get():
        if event.type == pygame.TEXTINPUT:
            frequency = freqval(event.text)
            if event.text not in lst and frequency:
                lst.append(event.text)
                for i in range(len(lst)):
                    freql.append(frequency)
                a = Sine(freq=freql,mul = adsr).out()
                freql = []
                adsr.play()

        elif event.type == pygame.KEYUP and frequency:
            lst.remove(event.unicode)
            if len(lst) == 0:
                continue

        elif event.type == pygame.QUIT:
            s.stop()
            pygame.quit()
               
        print(lst)


            
    