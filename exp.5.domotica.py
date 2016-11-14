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

SAMPLES_DIRECTORY = '/home/pere/SonicPi/samples/'

S_RAIN = SAMPLES_DIRECTORY + 'rain-03.wav'
S_WIND = SAMPLES_DIRECTORY + 'wind-01.wav'
S_WIND_LENGTH = 60
S_WIND_CHIME = SAMPLES_DIRECTORY + 'wind-chime-2.wav'
S_WIND_CHIME_LENGTH = 54.421
S_BUTTON_2 = SAMPLES_DIRECTORY + 'button-2.wav'
S_BUTTON_7 = SAMPLES_DIRECTORY + 'button-7.wav'
S_BUTTON_15 = SAMPLES_DIRECTORY + 'button-15.wav'
S_BUTTON_17 = SAMPLES_DIRECTORY + 'button-17.wav'
S_BUTTON_47 = SAMPLES_DIRECTORY + 'button-47.wav'
S_BUTTON_PHONE = SAMPLES_DIRECTORY + 'button-2.wav'
S_TELEPHONE_RING_3 = SAMPLES_DIRECTORY + 'telephone-ring-3.wav'


BEAT = 0
BEAT_TIME = 0.25


def start_thread_do(function, delay=0.0, params=[]):
    sleep(delay)
    Thread(target=function, args=params).start()


def start_thread(function, delay=0.0, params=[]):
    Thread(target=start_thread_do, args=[function, delay, params]).start()


def nature_rain_beginning():
    sample(S_RAIN, amp=2, sustain=15, release=10)
    start_thread(nature_wind_beginning, 7.55)


def nature_wind_beginning():
    use_fx(['ixi_techno'])
    sample(S_WIND, amp=2, sustain=10, release=4, finish=(14/S_WIND_LENGTH))
    use_fx([])
    start_thread(house_external_wind_chime, (5.99 - 4.625), [4.625])


def house_external_wind_chime(bit_crusher):
    bit_crusher_p = bit_crusher/S_WIND_CHIME_LENGTH
    end = 15.70
    end_p = end/S_WIND_CHIME_LENGTH
    sample(S_WIND_CHIME, amp=4, finish=bit_crusher_p)
    sleep(bit_crusher)
    use_fx(['bitcrusher', 'wobble', 'reverb'])
    sample(S_WIND_CHIME, amp=11, release=5, start=bit_crusher_p, finish=end_p)
    use_fx([])
    start_thread(director, 2.43)


def director():
    global BEAT
    while BEAT < 12*16:
        if BEAT < 1*16:
            start_thread(rhythmic_foundation, 0, [False, True])
        elif BEAT < 2*16:
            start_thread(rhythmic_foundation, 0, [True, True])
        elif BEAT < 8*16:
            start_thread(rhythmic_foundation, 0, [True, True])
            start_thread(rhythmic_support, 0, [0])
        elif BEAT < 10*16:
            start_thread(rhythmic_foundation, 0, [True, True])
            start_thread(rhythmic_support, 0, [1])
        elif BEAT < 12*16:
            start_thread(rhythmic_foundation, 0, [True, True, True])
            start_thread(rhythmic_support, 0, [1])
        # prepare next beat and sleep until then
        sleep(BEAT_TIME)
        BEAT += 1


def rhythmic_telephone_ring():
    use_fx(['reverb'])
    sample(S_TELEPHONE_RING_3, amp=2)
    use_fx([])


def rhythmic_echoed():
    use_fx(['bitcrusher', 'echo'])
    sample(S_BUTTON_7, amp=0.8, rate=0.5)
    use_fx([])


def rhythmic_happy():
    use_fx(['reverb', 'rhpf'])
    sample(S_BUTTON_2, amp=1.5, rate=1, start=0.5/1.326)
    use_fx([])


def rhythmic_foundation(telephone=False, echo=False, happy=False):
    if BEAT % 16 == 0:
        if telephone:
            start_thread(rhythmic_telephone_ring)
        if echo:
            start_thread(rhythmic_echoed, BEAT_TIME*6)
            start_thread(rhythmic_echoed, BEAT_TIME*8)
        if happy:
            start_thread(rhythmic_happy, BEAT_TIME*12)


def rhythmic_support_15():
    sample(S_BUTTON_15, amp=0.8)


def rhythmic_support_17():
    sample(S_BUTTON_17, amp=0.8)


def rhythmic_support_47():
    sample(S_BUTTON_47, amp=0.8, start=(0.10/0.17))


def rhythmic_support(p_type=0):
    if BEAT % 8 == 0:
        if p_type == 0:
            start_thread(rhythmic_support_15, BEAT_TIME*4)
            start_thread(rhythmic_support_47, BEAT_TIME*6)
        if p_type == 1:
            start_thread(rhythmic_support_15, BEAT_TIME*0)
            start_thread(rhythmic_support_17, BEAT_TIME*2)
            start_thread(rhythmic_support_15, BEAT_TIME*4)
            start_thread(rhythmic_support_47, BEAT_TIME*6)


# Main
start_thread(nature_rain_beginning)
#start_thread(director)
