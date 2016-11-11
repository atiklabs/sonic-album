# Coded by Pere Garcia

from psonic import *
from threading import Thread


def base():
    while True:
        sample(BD_SONE, rate=-0.8, amp=3)
        sleep(0.5)
        sample(BD_SONE, amp=3)
        sleep(0.5)


def play_hoover(note, sleep_time):
    use_synth(HOOVER)
    play(note, sustain=2, attack=0.5, release=0.5, amp=0.2)
    sleep(sleep_time)


def synthesis():
    while True:
        use_synth(HOOVER)
        play_hoover([Ds5, C5], 3)
        play_hoover(C5, 3)


def clapping_hands():
    clapping = [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]  # 12 ***_**_*_**_
    while True:
        for item in clapping:
            if item == 1:
                sample(DRUM_SNARE_SOFT, amp=3)
            sleep(0.25)


def long_piano():
    while True:
        use_synth(SAW)
        play(C5, attack=1, release=1, pan=0.5, amp=0.1)
        sleep(6)


def industrial():
    while True:
        sample(LOOP_INDUSTRIAL)
        sleep(3)


# Main thread
time.sleep(1 - time.time() % 1)
Thread(target=base).start()
Thread(target=synthesis).start()
Thread(target=clapping_hands).start()
Thread(target=industrial).start()
Thread(target=long_piano).start()
