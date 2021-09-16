# this library comes with python and will pause for us
import time
# to choose a random sound and time
import random

sounds = [
    "bird-0.wav",
    "bird-1.wav",
    "bird-2.wav",
    "bird-3.wav",
    "bird-4.wav",
    "bird-5.wav",
    "bird-6.wav",
    "bird-7.wav",
]


def loop():
    sound = random.choice(sounds)
    print(sound)
    pause = random.uniform(0.5, 5.5)
    print(pause)
    time.sleep(pause)
    loop()


sound = random.choice(sounds)
print(sound)

loop()
