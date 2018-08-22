from os import listdir
from os.path import isfile, join
folderPath = 'D:\Testing\JSProj\skAlgoDataStructure'


def getFiles(folderPath,currentLevel, finalLevel):
	if currentLevel >= finalLevel:
		return

	currentLevel +=1
	
	for i in listdir(folderPath):   
		if isfile(join(folderPath,i)): 
			print('File name:',i)
		else:
			fd_name = join(folderPath,i)
			print ('Folder Name:',fd_name)   
			getFiles(fd_name,currentLevel, finalLevel)
				

getFiles(folderPath,0,2)