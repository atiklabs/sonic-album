# Experiment 4: Domotica Lights
# Coded by Atik
#
# Part 0: Some nature sound will sound, then the house will be
# situated to the listener by joining this nature sounds with some
# typical exterior house sound
# Part 1: The listener enters in the house by listening a couple of
# typical house sounds somehow rhythmical, the electrified air
# invades the normal sounds
# Part 2: Some weird sound will happen, and the lights of the house will
# start to get crazy, some button sounds interpreting the lights
# and waves of electricity and lights
# Part 3: Some electric failure will happen and the domotica will gain
# some voice, followed by ups and downs and experimental sounds
# Part 4: Some big up, like music gone crazy for the final closure, and
# some human voices appear


from psonic import *
from threading import Thread

SAMPLES_DIRECTORY = '/home/pere/SonicPi/sonic-album/samples/'

S_RAIN = SAMPLES_DIRECTORY + 'rain-03.wav'
S_WIND = SAMPLES_DIRECTORY + 'wind-01.wav'
S_WIND_LENGTH = 60
S_WIND_CHIME = SAMPLES_DIRECTORY + 'wind-chime-2.wav'
S_WIND_CHIME_LENGTH = 54.421
S_BUTTON_15 = SAMPLES_DIRECTORY + 'button-15.wav'
S_BUTTON_17 = SAMPLES_DIRECTORY + 'button-17.wav'
S_BUTTON_47 = SAMPLES_DIRECTORY + 'button-47.wav'
S_BUTTON_2 = SAMPLES_DIRECTORY + 'button-2.wav'


TICK = 0
TICK_TIME = 0.5


def start_thread_do(function, delay=0.0, params=[]):
    sleep(delay)
    Thread(target=function, args=params).start()


def start_thread(function, delay=0.0, params=[]):
    Thread(target=start_thread_do, args=[function, delay, params]).start()


def nature_rain_beginning():
    sample(S_RAIN, amp=2, sustain=15, release=5)
    start_thread(nature_wind_beginning, 3.59)


def nature_wind_beginning():
    use_fx(['ixi_techno'])
    sample(S_WIND, amp=2, sustain=10, release=10, finish=(20/S_WIND_LENGTH))
    use_fx([])
    start_thread(house_external_wind_chime, (5.99 - 4.625), [4.625])


def house_external_wind_chime(bit_crusher):
    bit_crusher_p = bit_crusher/S_WIND_CHIME_LENGTH
    end = 10.56
    end_p = end/S_WIND_CHIME_LENGTH
    start_thread(main_loop, 7.537)
    sample(S_WIND_CHIME, amp=4, finish=bit_crusher_p)
    sleep(bit_crusher)
    use_fx(['bitcrusher'])
    sample(S_WIND_CHIME, amp=11, start=bit_crusher_p, finish=end_p)
    use_fx([])


def main_loop():
    global TICK
    while TICK < 64:
        start_thread(buttons)
        sleep(TICK_TIME)
        TICK += 1


def buttons():
    if TICK < 12:
        start_thread(buttons_rhythmic, 0, [1])
    else:
        start_thread(buttons_rhythmic, 0, [2])
    if TICK == 16:
        start_thread(buttons_awakening, 0.5)


def buttons_rhythmic(p_type=0):
    if p_type == 1:
        if TICK % 4 == 0:
            sample(S_BUTTON_15, amp=0.8)
        if TICK % 4 == 2:
            sample(S_BUTTON_47, amp=0.8, start=(0.10/0.17))
    elif p_type == 2:
        if TICK % 4 == 0:
            sample(S_BUTTON_15, amp=0.8)
        if TICK % 4 == 1:
            sample(S_BUTTON_17, amp=0.8)
        if TICK % 4 == 2:
            sample(S_BUTTON_15, amp=0.8)
        if TICK % 4 == 3:
            sample(S_BUTTON_47, amp=0.8, start=(0.10/0.17))


def buttons_awakening():
    sample(S_BUTTON_2, amp=2, rate=0.8)


# Main
# start_thread(nature_rain_beginning)
TICK = 12
start_thread(main_loop)
