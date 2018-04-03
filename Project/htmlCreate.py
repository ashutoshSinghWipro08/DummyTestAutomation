import xml.etree.ElementTree as xml
import datetime

def generateHtmlDocument(li):
	
	now = datetime.datetime.now()	
	filename=""#+str(now.month)+str(now.year)
	if now.day<10:
		filename+="0"+str(now.day)+"-"
	if now.month<10:
		filename+="0"+str(now.month)+"-"
	filename+=str(now.year)+".html"
	
	#filename = "result.xml"
	root = xml.Element("html")
	body=xml.Element("body")	
	root.append(body)
	count=0
	pas=0
	fail=0
	err=0
	for data in li:
		if data==True:
			count+=1
			pas+=1
			test=xml.SubElement(body, "h1")
			test.text ="testNo"+str(count)+" : Passed"			
		elif data==False:
			fail+=1
			count+=1
			test=xml.SubElement(body, "h1")
			test.text ="testNo"+str(count)+" : Failed"
	testpass = xml.SubElement(body,"h1")
	testpass.text ="testPassed :"+str(pas)
			
	testfail = xml.SubElement(body, "h1")
	testfail.text = "testFailed : "+str(fail)

	testerr= xml.SubElement(body,"h1")
	testerr.text = "testerror : "+str(0)	
	
	tree = xml.ElementTree(root)
	#print dir(tree)
	with open(filename, "w") as fh:
		tree.write(fh)	

if __name__=='__main__':
	generateHtmlDocument([True,True,False,True,False,True])
