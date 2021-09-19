import glob

def resolve():
	files = glob.glob('./**/*.txt', recursive = True)
	with open('all.txt', 'a') as ff:
		for file in files:
			with open(file, 'r') as f:
				ff.write(file + ' => ' + f.read() + '\n')
				
resolve()
