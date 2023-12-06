import sys, os, shutil

def main():

	#Check argument
	if len(sys.argv) < 2:
		print('You forgot to specify a day number.')
		exit()
	daynum = sys.argv[1]
	if not isinstance (int(daynum), int) or (int(daynum) < 0) or (int(daynum) > 25):
		print('Argument is not a valid day number')
		exit()
	
	daydir = 'day' + daynum
	
	#Create python codes from template, and replace with day number in input lines
	os.mkdir(daydir)
	codefiles = []
	codefiles.append('./'+daydir+'/aoc2023_solution_'+daynum+'_1_v1.py')
	codefiles.append('./'+daydir+'/aoc2023_solution_'+daynum+'_2_v1.py')
	for file in codefiles:
		shutil.copy('./template.py', file)
		with open(file, 'r+') as f:
			old = f.read()
			new =  old.replace('_dayx_','_day'+daynum+'_')
			f.seek(0) #rewind to file start
			f.write(new) #overwrite
	
	#Create empty text files (inputs, logs)
	emptyfiles = []
	emptyfiles.append('./'+daydir+'/aoc2023_day'+daynum+'_input.txt')
	emptyfiles.append('./'+daydir+'/aoc2023_day'+daynum+'_testinput.txt')
	emptyfiles.append('./'+daydir+'/log_'+daynum+'_1_v1.txt')
	emptyfiles.append('./'+daydir+'/log_'+daynum+'_2_v1.txt')
	for file in emptyfiles:
		open(file, 'a').close()

main()