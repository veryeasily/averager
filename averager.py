import wave
import random
fp = wave.open('./test.wav')
fp2 = wave.open('./output.wav', 'w')
fp2.setparams(fp.getparams())
wavelength = fp.getnframes()
for x in xrange(500):
	insertionpoint = random.randint(0, wavelength - 1)
	fp.setpos(insertionpoint)
	left = wavelength - insertionpoint
	cliplength = min(random.randint(1,7) * 1300, left)
	sample = fp.readframes(cliplength)
	"""	this is code I used to use to cut stuff in half

	cutpoint = len(sample)/2
	cutpoint = cutpoint + cutpoint % 2
	print "cliplength: " + str(cliplength)
	print "sample length: " + str(len(sample))
	print "cutpoint = " + str(cutpoint)
	sample = sample[cutpoint:] + sample[:cutpoint]
	"""
	fp2.writeframesraw(sample)
fp.close()
fp2.close()
