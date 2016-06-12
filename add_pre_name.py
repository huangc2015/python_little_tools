import os
import os.path

path = raw_input("PATH:")
pre = raw_input("PRE_NAME:")


for files in os.walk(path):
	for f in files[2]:
		os.rename(files[0]+"\\"+f,files[0]+"\\"+pre+"_"+f)
		#print files[0]+"\\"+pre+"_"+f



print "RENAME DONE."