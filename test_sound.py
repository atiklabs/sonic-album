from psonic import *

SAMPLES_DIRECTORY = '/home/pere/SonicPi/sonic-album/samples/'

S_BUTTON_2 = SAMPLES_DIRECTORY + 'button-2.wav'
S_BUTTON_15 = SAMPLES_DIRECTORY + 'button-15.wav'
S_BUTTON_17 = SAMPLES_DIRECTORY + 'button-17.wav'
S_BUTTON_18 = SAMPLES_DIRECTORY + 'button-18.wav'
S_BUTTON_20 = SAMPLES_DIRECTORY + 'button-20.wav'
S_BUTTON_47 = SAMPLES_DIRECTORY + 'button-47.wav'
S_TELEPHONE_3 = SAMPLES_DIRECTORY + 'telephone-ring-3.wav'

use_fx(['reverb'])
sample(S_BUTTON_2, amp=2, rate=0.8)
use_fx([])
sleep(0.5)
sample(S_TELEPHONE_3, amp=2, rate=0.8)

