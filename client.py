#coding:utf8
import os
from time import sleep
#inf = os.popen('cd checkpoint&&git clone git@github.com:CAIZI12138/test.git').read()

cmd = "dir"
files = []
new = []
while True:
	
	inf = os.popen(cmd).read()
	print("files: \n",inf)
	for i in inf.split('\n'):
		if i and (i not in files):
			files.append(i)
			new.append(i)

	if new:
		cmd_push = "git add"
		for a in new:
			cmd_push += ' '+a
			print("new:",a)
		cmd_push += '&&git commit -m "new"'
		cmd_push += "&&git push origin master"
		print(os.popen(cmd_push).read())
	sleep(60*60*1)



		



