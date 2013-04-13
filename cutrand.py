import wave
import random
fp = wave.open('./test.wav')
fp2 = wave.open('./test15.wav', 'w')
fp2.setparams(fp.getparams())
wavelength = fp.getnframes()
left = wavelength - fp.tell()
while left > 0:
	cliplength = min(random.randint(1,100000), left)
	sample = fp.readframes(cliplength)
	cutpoint = len(sample)/2
	cutpoint = cutpoint + cutpoint % 2
	print "cliplength: " + str(cliplength)
	print "sample length: " + str(len(sample))
	print "cutpoint = " + str(cutpoint)
	sample = sample[cutpoint:] + sample[:cutpoint]
	fp2.writeframesraw(sample)
	left = wavelength - fp.tell()
fp.close()
fp2.close()
