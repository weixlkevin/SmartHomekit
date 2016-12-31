 # encoding: utf-8
import sys
import os
import io
from managermentFileForqiniu import managerfile
import logging
import datetime

##log
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y %m %d  %H:%M:%S',filename='Python_main.log',filemode='a')
logging.info('\r\n')
##main
Sync_path='/home/pi/Documents/qiniuclouddir'
now=datetime.datetime.now()
strnow=now.strftime('%Y-%m-%d %H:%M:%S')
files=os.listdir(Sync_path)
if(len(files)==0):
	sys.exit()
	logging.info(strnow+"Do not find file in Sync_path.")
mf=managerfile()
ret,eof,info=mf.getfileslist(-1)
if(info.status_code!="200"):
	sys.exit()
	logging.error(strnow+"qiniucloud connect fail.statusCode:"+info.status_code)
remotefile=ret.get("items")

for localfile in files:
	exist=0
	for file in remotefile:
		if(file.get("key")==localfile):
			exist=1
			break
	if(exist==0):
		result=mf.upload(localfile,Sync_path+"/"+localfile)
		if(result.status_code==200):
			logging.info(strnow+"uplaod %s successed" % (localfile))
			
