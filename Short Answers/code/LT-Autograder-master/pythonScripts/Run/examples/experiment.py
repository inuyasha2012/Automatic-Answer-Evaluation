import collections, re

import reg1,reg2
import sys

#To read all the inputs from the file
reader = open('train.tsv', 'r' )
SET = 1
count1= 0
mat="distilled water"
counta = 0
exp = []
exp=reg1.reg()
exp2 =[]
exp2=reg2.reg()
for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	s1=int(line[2])
	s2=int(line[3])
	Id = int(line[0])
	text = line[4]
	
	if(mat in text):
		count1=count1+1
		print (Id)
		print (text)
		print('---------------------\n')
	
	
	'''for reg in exp:
		if(re.match(reg,text)):
			#print("\n")
			#print(text)
			#print("-----------------\n")
			count1=count1+1;
		
		for i in exp:					 
		if any(regex.match(text) for regex in exp):
			print('Id:\t%d' % Id)'''
		 
	#if any(regex.match(text) for regex in exp):
	#	print ('Some regex matched!')
	#	print('Id:\t%d' % Id)	
	#	print ("\n") 
	#	print ('Score:\t%d' % s1)
	#	print ("\n")
	#	print ('Text:\t%s' % text)
	#	print ("\n")'''

#if(regex.match(es) for regex in exp):
#	print("It has matched\n")
#	print(exp[regex])'''


print (count1)
print (counta)

'''SET=2
count2=0
for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	text = line[2]
	#print(Id)
	print("\n")
	for reg in exp2:
		if(re.match(reg,text)):
			#print("\n")
			#print(text)
			#print("-----------------\n")
			count2=count2+1;
print(count2)'''	