# Sonic Pi instructions cheat sheet

from psonic import *

# C (do) D (re) E (mi) F (fa) G (sol) A (la) B (si)

use_synth(SAW)  # instruments
sample(LOOP_AMEN_FULL)  # play an already made sample
play(64)    # plays E4 (Mi)
play(64.44)  # a note between 64 and 65
play(E4)    # plays E4
play(Db4)   # plays Re flat
play(D4)    # plays Re
play(Ds4)   # plays Re sharp
sleep(1)    # sleep for one beat

# defaults play
# amp for amplification
# pan for stereo left (-1) or right (1)
# release is the time for the note to fade out
# attack is the time for the note to fade in
# sustain is the time for the note to maintain in full amplitude
play(C4, amp=1, pan=0, release=1, attack=0, sustain=0)

# more defaults
# decay is the time to go from attack level to sustain level
# attack_level default 1 (to implement)
# decay_level default is sustain_level (to implement)
# sustain_level is the level of the sustain
# 1. attack - time from 0 amplitude to the attack_level,
# 2. decay - time to move amplitude from attack_level to decay_level,
# 3. sustain - time to move the amplitude from decay_level to sustain_level,
# 4. release - time to move amplitude from sustain_level to 0
play(C4, decay=0, sustain_level=1)

# defaults sample
# rate the more the fastest, minus for backwards
sample(LOOP_AMEN_FULL, rate=1)
sample('/home/pere/my-sound.wav')  # wav, aiff or flac

# discovering samples
# ambi_
# bass_
# elec_
# perc_
# guit_
# drum_
# misc_
# bd_

# a simple approach to communicate with Sonic Pi
synthServer.run('play 60')
synthServer.run("with_fx :echo do\nplay 64\nend")
