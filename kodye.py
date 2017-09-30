from record import *
from midi_fixer import fix
from translate import midi_to_brainfrick, brainfrick_to_midi
from subprocess import call

import os, sys

try:
    # Amount of time to listen for program
    seconds = int(sys.argv[1])
    # Name of program
    name = sys.argv[2]
except e:
    print("Usage: python kodye.py [duration] [name]")
    print(e)
    exit()
    
# Get sounds from user
audio_in = recordAudio(seconds)

writeWav(audio_in, name + ".wav")

try:
    os.remove(name + '.mid')
except:
    pass

call(["./lib/sonic_annotator/sonic-annotator.exe",
     "-d",
     "vamp:mtg-melodia:melodia:melody",
     "./" + name + ".wav",
     "-w",
     "midi"])

fix(name + ".mid", name + "_fixed.mid")

print(midi_to_brainfrick(name + "_fixed.mid"))
