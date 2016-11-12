# Experiment 4: Day 3
# Coded by Atik

from psonic import *
from threading import Thread

TICK = 0
TICK_TIME = 0.5


def drums_heartbeat():
    if TICK % 4 == 0:
        use_fx(['echo, phase:0.25, decay: 4'])
        sample(BD_HAUS)
        use_fx([])


# Drum main rhythm
# *_*_ STRONG
# _*__ LOW
def drum_main_rhythm():
    sample(BD_KLUB, amp=4)
    if TICK % 2 == 0:
        sleep(0.25)
        use_fx(['reverb'])
        sample(BD_TEK, amp=0.5)
        use_fx([])


# Play chord
def play_chord(note, tick):
    if TICK == tick:
        use_synth(TB303)
        use_fx(['reverb'])
        play(note, amp=0.8)
        use_fx([])


# Play a melody note
def play_melody(note, tick):
    if TICK == tick:
        use_synth(TB303)
        use_fx(['echo, phase: 0.25', 'reverb'])
        play(note, amp=0.8, release=0.27)
        use_fx([])


# Drums controller
def drums():
    Thread(target=drums_heartbeat).start()
    if TICK < 24:
        pass
    else:
        drum_main_rhythm()


# Cords controller
def chords():
    if TICK < 16:
        pass
    else:
        start_tick = ((TICK // 16) * 16)
        play_chord([C3, E3, A3], start_tick + 0)
        # silence 1
        play_chord([C3, E3, A3], start_tick + 2)
        play_chord([C3, E3, A3], start_tick + 3)
        play_chord([C3, E3, G3], start_tick + 4)
        # silence 5-7
        play_chord([C3, E3, G3], start_tick + 8)
        # silence 8
        play_chord([C3, E3, G3], start_tick + 10)
        play_chord([C3, E3, G3], start_tick + 11)
        play_chord([C3, E3, A3], start_tick + 12)
        # silence 12-15


# Melody controller
def melody():
    start_tick = 32
    # silence 0-1
    play_melody(D4, start_tick + 2)
    play_melody(E4, start_tick + 3)
    play_melody(C4, start_tick + 4)
    # silence 5-9
    play_melody(C4, start_tick + 10)
    play_melody(D4, start_tick + 11)
    play_melody(E4, start_tick + 12)
    # silence 13-17
    play_melody(D4, start_tick + 18)
    play_melody(E4, start_tick + 19)
    play_melody(C4, start_tick + 20)
    # silence 21-25
    play_melody(C4, start_tick + 26)
    play_melody(D4, start_tick + 27)
    play_melody(C4, start_tick + 28)
    # silence 29-31


# Main loop
while TICK < 64:
    Thread(target=drums).start()
    Thread(target=chords).start()
    Thread(target=melody).start()
    sleep(TICK_TIME)
    TICK += 1
