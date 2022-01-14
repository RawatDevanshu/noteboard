import pygame
from pyo import *
s = Server(sr = 48000).boot()
s.start()

qwert ={'z': 1, 's': 2, 'x': 3, 'd': 4, 'c': 5, 'v': 6, 'g': 7, 'b': 8, 'h': 9, 'n': 10, 'j': 11, 'm': 12, ',': 13}

def freqval(char):
    n = qwert[char]
    a = 1.05946309436
    return 261*(a**n)  #base freq ==261HZ Note = "C4"
pygame.init()
screen = pygame.display.set_mode((400,300))
lst = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.TEXTINPUT:
            if event.text not in lst:
                lst.append(event.text)
        elif event.type == pygame.KEYUP:
            lst.remove(event.unicode)
            fr = freqval(event.unicode)
            a.stop()
        elif event.type == pygame.QUIT:
            s.stop()
            pygame.quit()
        for i in lst:
            fr = freqval(i)
            a = Sine(freq=fr)
            if a.out():
                pass
            else:
                a.out()            



            
    