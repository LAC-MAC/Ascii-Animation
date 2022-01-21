import os, time


choosenDir = '/Users/lachlanmackay/Desktop/animate/rrAscii/'
filePaths = os.listdir(choosenDir)

#filePaths.remove(".DS_Store")

filePaths.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))


def animator(filePaths, repeatNum, delay):

	frames = []
	for path in filePaths:
		path = choosenDir+path
		with open (path,"r",encoding="utf8") as f:
			frames.append(f.readlines())
	for i in range(repeatNum):
		for frame in frames:
			print("".join(frame))
			time.sleep(delay)
			os.system('clear')
		
animator(filePaths ,delay = 0.02,  repeatNum = 1)



