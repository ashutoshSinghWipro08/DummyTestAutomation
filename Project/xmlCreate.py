import xml.etree.ElementTree as xml
import datetime

def generateXmlDocument(li):
	
	now = datetime.datetime.now()	
	filename=""#+str(now.month)+str(now.year)
	if now.day<10:
		filename+="0"+str(now.day)+"-"
	if now.month<10:
		filename+="0"+str(now.month)+"-"
	filename+=str(now.year)+".xml"
	
	#filename = "result.xml"
	root = xml.Element("testresult")
	count=0
	pas=0
	fail=0
	err=0
	for data in li:
		if data==True:
			count+=1
			pas+=1
			test = xml.SubElement(root, "testNo"+str(count))
			test.text = "Passed"			
		elif data==False:
			fail+=1
			count+=1
			test = xml.SubElement(root, "testNo"+str(count))
			test.text = "Failed"
	testpass = xml.SubElement(root, "testPassed")
	testpass.text = str(pas)
			
	testfail = xml.SubElement(root, "testFailed")
	testfail.text = str(fail)

	testerr= xml.SubElement(root, "testerror")
	testerr.text = str(0)	
	
	tree = xml.ElementTree(root)
	#print dir(tree)
	with open(filename, "w") as fh:
		tree.write(fh)	

if __name__=='__main__':
	generateXmlDocument([True,True,False,True,False,True])


#userelement = xml.Element("user")
#root.append(userelement)

"""test = xml.SubElement(root, "testNo"+"0")
test.text = "Passed"

test1 = xml.SubElement(root, "testNo"+"1")
test1.text = "Passed"

testpass = xml.SubElement(root, "testPassed")
testpass.text = "2"

tree = xml.ElementTree(root)
with open(filename, "w") as fh:
    tree.write(fh)
"""

"""<testresult>
		<testno1>Passed</testno1>
		<testno2>Passed</testno2>
<testno3>Failed</testno3>
<testpassed>2</testpassed>
<testfailed>1</testfailed>
<testerror>0</testerror>
</testresult>
"""
