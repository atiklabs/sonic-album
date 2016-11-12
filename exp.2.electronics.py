# Experiment 2: Electronics
# Coded by Atik

from psonic import *
from threading import Thread


def background(n):
    """In total 1"""
    for i in range(n):
        use_fx(['echo'])
        sample(BD_KLUB, amp=0.7)
        sleep(1)


def tick_tack(n):
    """In total 1"""
    for i in range(n):
        sleep(0.5)
        use_fx(['reverb'])
        sample(BD_PURE, rate=-1, amp=6)
        sleep(0.5)
        use_fx(['reverb'])
        sample(ELEC_TICK)


def melody(n, note1, note2):
    """In total 8"""
    for i in range(n):
        use_synth(TB303)
        use_fx(['echo', 'reverb'])
        play(note1, release=0.5, amp=0.2)
        sleep(4)
        use_fx(['echo', 'reverb'])
        play(note2, release=0.5, amp=0.2)
        sleep(4)


# Main
print("Part 1")
Thread(target=tick_tack, args=[12]).start()
sleep(4)
Thread(target=background, args=[8]).start()
Thread(target=melody, args=[1, A2, E3]).start()

print("Part 2")
