import xml.etree.ElementTree as et

def readXmlDocument(filename):
	st=filename.split(".")[0]
	print "--------------------------------------------------------------"
	print "Test Result %s "%(st)
	print "--------------------------------------------------------------"
		
		
	tree = et.parse(filename)
	
	root = tree.getroot()
	count=0
	for child in root:
		count+=1
		if count<=4:		
			print child.tag,
			print "-",
			print child.text
		else:
			print child.tag,
			print ":",
			print child.text 
		if count==4:
			print "--------------------------------------------------------------"
		
if __name__=='__main__':
	readXmlDocument("result.xml")
		
