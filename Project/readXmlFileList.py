import glob, os

def readXmlList(): 
	li=[]
	for file in glob.glob("*.xml"):
		print(file)
		li.append(file)
	return li

