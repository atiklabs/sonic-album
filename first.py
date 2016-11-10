# Coded by Pere Garcia

from psonic import *
from threading import Thread

# Notes: C#, F#


def accompaniment_1():
    for i in range(8):
        play(G3, sustain=2)
        sleep(3)
        play(D3, sustain=2)
        sleep(3)


def accompaniment_2():
    for i in range(8):
        sleep(1)
        play([B3, D4, Fs4], sustain=2)
        sleep(2 + 1)
        play([A3, Cs4, Fs4], sustain=2)
        sleep(2)


def melody():
    play(Fs5, amp=0.8)
    sleep(1)
    play(A5, amp=0.9)
    sleep(1)
    play(G5, amp=1)
    sleep(1)
    play(Fs5, amp=1.1)
    sleep(1)
    play(Cs5, amp=1.2)
    sleep(1)
    play(B4, amp=1.3)
    sleep(1)
    play(Cs5, amp=1.4)
    sleep(1)
    play(D5, amp=1.5)
    sleep(1)


def after_melody():
    play(A4, sustain=3, amp=1.3)
    sleep(3)
    for i in range(4):
        play(Fs4, sustain=3, amp=0.8)
        sleep(3)


# get threads
t_accompaniment_1 = Thread(target=accompaniment_1)
t_accompaniment_1.start()

t_accompaniment_2 = Thread(target=accompaniment_2)
t_accompaniment_2.start()

sleep(12 + 1)
t_melody = Thread(target=melody)
t_melody.start()

sleep(8)
t_after_melody = Thread(target=after_melody)
t_after_melody.start()

sleep(15 + 1)
t_melody = Thread(target=melody)
t_melody.start()
