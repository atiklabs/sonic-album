# Inspired by Steve Reich Clapping Music

from psonic import *

clapping = [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

for i in range(13):
    for j in range(4):
        for k in range(12):
            if clapping[k] == 1:
                sample(DRUM_SNARE_SOFT, pan=-0.5)
            if clapping[(i + k) % 12] == 1:
                sample(DRUM_HEAVY_KICK, pan=0.5)
            sleep(0.25)
