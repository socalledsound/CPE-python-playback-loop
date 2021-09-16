# this library comes with python and will pause for us
import time
# to choose a random sound and time
import random
# this library is for our cpe
from adafruit_circuitplayground import cp
# set the overall brightness
cp.pixels.brightness = 0.5
numSounds = 8
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


def playFile(filename):
    cp.play_file(filename)


def loop():
    sound = random.choice(sounds)
    print(sound)
    pause = random.uniform(0.5, 15.5)
    playFile(sound)
    cp.pixels[6] = (255, 0, 0)
    time.sleep(pause)
    cp.pixels[6] = (0, 0, 0)
    return loop()


cp.pixels[6] = (0, 0, 255)
time.sleep(1.0)
cp.pixels[6] = (0, 0, 0)
time.sleep(1.0)
cp.pixels[6] = (0, 255, 0)
time.sleep(1.0)
loop()
