import time
import os
import shutil
import fnmatch

print ("GoPro Hero 2014 Entry Level, Change Time Lapse Script")
input("Enter to continue,")
newlapse = input ("Enter New Lapse Variable ...  ")
try:
	checkinput = int(newlapse)
except ValueError:	
	print ("Error, input integer only")
	exit()

newdir = input ("Enter New Directory to save ...  ")
if not os.path.exists(newdir):
	os.makedirs(newdir)
else:
	print ("...Directory exist, using \"%s\" directory" %(newdir))	

pwd = os.getcwd()
path = '.'

list_files = sorted(os.listdir(pwd))
list_files_new =[]
for i in list_files:
	if fnmatch.fnmatch(i, '*.JPG'):
		list_files_new.append(i)

countpros = 0
for j in list_files_new:
	if (list_files_new.index(j) % checkinput ==0):
		print (j)
		shutil.copy(j, newdir)
		countpros = countpros+1
	
print ("Total Raw File ... %s" %(len(list_files_new)))
print ("Total Process File ... %s" %(countpros))
print ("First File ... %s" %(list_files_new[0]))
print ("Last File ... %s" %(list_files_new[len(list_files_new)-1]))

input("Enter to quit,")

