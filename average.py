#!/usr/bin/env python

import wave
import random
import sys

try:
  filename = sys.argv[1] 
except IndexError:
  filename = './test.wav'
fp = wave.open(filename)
fp2 = wave.open('./output.wav', 'w') 
fp2.setparams(fp.getparams())
wavelength = fp.getnframes()
for x in xrange(1, wavelength, wavelength/9):
  insertionpoint = random.randint(x, wavelength - 1)
  fp.setpos(insertionpoint)
  left = wavelength - insertionpoint
  cliplength = random.randint(1, left/3)
  sample = fp.readframes(cliplength)
  fp2.writeframesraw(sample)
fp2.close()
fp.close()
