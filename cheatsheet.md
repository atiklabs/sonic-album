# Sonic Pi instructions cheat sheet

## C (do) D (re) E (mi) F (fa) G (sol) A (la) B (si)

```python
use_synth(SAW)  # instruments
sample(LOOP_AMEN_FULL)  # play an already made sample
play(64)    # plays E4 (Mi)
play(64.44)  # a note between 64 and 65
play(E4)    # plays E4
play(Db4)   # plays Re flat
play(D4)    # plays Re
play(Ds4)   # plays Re sharp
sleep(1)    # sleep for one beat
```

## Play defaults

* __amp__ for amplification
* __pan__ for stereo left (-1) or right (1)
* __release__ is the time for the note to fade out
* __attack__ is the time for the note to fade in
* __sustain__ is the time for the note to maintain in full amplitude

```python
play(C4, amp=1, pan=0, release=1, attack=0, sustain=0)
```

## More play defaults

* __decay__ is the time to go from attack level to sustain level
* __attack_level__ default 1 (to implement)
* __decay_level__ default is sustain_level (to implement)
* __sustain_level__ is the level of the sustain

This is called the ADSR:

1. attack - time from 0 amplitude to the attack_level,
2. decay - time to move amplitude from attack_level to decay_level,
3. sustain - time to move the amplitude from decay_level to sustain_level,
4. release - time to move amplitude from sustain_level to 0

```python
play(C4, decay=0, sustain_level=1)
```

## Sample defaults

* __rate__ the more the fastest, minus for backwards

```python
sample(LOOP_AMEN_FULL, rate=1)
sample('/home/pere/my-sound.wav')  # wav, aiff or flac
```

## Discovering new samples

* ambi
* bass
* elec
* perc
* guit
* drum
* misc
* bd

# a simple approach to communicate with Sonic Pi

```python
synthServer.run('play 60')
synthServer.run("with_fx :echo do\nplay 64\nend")
```
