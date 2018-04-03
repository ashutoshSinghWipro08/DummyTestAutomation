from xmlCreate import generateXmlDocument
from showXmlContent import readXmlDocument
from readXmlFileList import readXmlList
from htmlCreate import generateHtmlDocument

class BasicFunction(object):
	#def __init__(self):
	#	print "created"
	def checkPrime(self,number):
		for i in range(2,number/2):
			if number%i==0:
				return False
		return True
	def checkSubstring(self,mainstr,substr):	
		mainstr=mainstr.lower()
		substr=substr.lower()
		ret=mainstr.find(substr,0,len(mainstr))
		if ret==-1:
			return False
		else:
			return True
	def checkOdd(self,number):
		if number%2==0:
			return False
		else:
			return True
	def checkEven(self,number):
		if number%2!=0:
			return False
		else:
			return True	
class Operation(object):
	def __init__(self):
		self.basic=BasicFunction()
		self.result=[]
		self.filelist=[]	
	def defineOperation(self):
		try:
			while True:			
				print "press 1 to test function "
				print "press 2 to list test runs  "
				print "press 3 to show test result "
				print "press 4 to generate html result "
				print "press 5 to exit "
			
				ch=int(raw_input())
				if ch==1:
					num=raw_input("Enter a Number (0,99) to check Prime")
					self.result.append(self.basic.checkPrime(int(num)))
					
					mainstr=raw_input("Enter a main string ")
					substr=raw_input("Enter a substring ")
					self.result.append(self.basic.checkSubstring(mainstr,substr))
				
					num=raw_input("Enter a number to check odd ")
					self.result.append(self.basic.checkOdd(int(num))) 				
				
					num=raw_input("Enter a number to check even ")
					self.result.append(self.basic.checkEven(int(num)))
					generateXmlDocument(self.result)
				
				elif ch==2:
					self.filelist=readXmlList()
					if len(self.filelist)==0:
						print "No Test performed "
				elif ch==3:
					if len(self.filelist)!=0:
						filename=raw_input("Enter the file name")
						showXmlContent(filename)
					else:
						print "No Test performed "
				elif ch==4:
					if len(self.filelist)==0:
						print "No Test performed "
					else:
						generateHtmlDocument(self.result)
				else:
					print "Exiting function "
					break
		except Exception as e:
			print e
if __name__=='__main__':
	obj=Operation()
	obj.defineOperation()
		
