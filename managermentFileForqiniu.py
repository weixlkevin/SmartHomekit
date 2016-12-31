# encoding:'utf-8'
from qiniu import Auth, put_file, etag, urlsafe_base64_encode,BucketManager
import qiniu.config
import requests

class managerfile:
	def __init__(self):
		self.access_key='jfPxDEq31sT7lx8indvCAtjXH6PyUXZARn0Cr6-6'
		self.secret_key='Hfh6063CzsY24qPQCeFtdbsGf5VdisL_5koUbkha'
		self.bucket_name='weixlkevin-cloud'
		self.bucket_domain='oigm0qwlo.bkt.clouddn.com'
		self.q=Auth(self.access_key,self.secret_key)

	def uploadfile(self,fileName,filePath):
		token=self.q.upload_token(self.bucket_name,fileName,3600)
		ret,info=put_file(token,fileName,filePath)
		return info

	def downloadfile(self,fileName):
		base_url='http://%s/%s' %(self.bucket_domain,fileName)
		private_url=self.q.private_download_url(base_url,expires=3600)
		r=requests.get(private_url)
		if(r.status_code==200):
			return r.text
		else:
			return "download fail."

	def getfileinfo(self,fileName):
		bucket=BucketManager(self.q)
		ret,info=bucket.stat(self.bucket_name,fileName)
		return ret,info

	def getfileslist(self,count):
		bucket=BucketManager(self.q)
		if(count==-1):
			limit=None
		else:
			limit=count
		ret,eof,info=bucket.list(self.bucket_name,None,None,limit,None)
		return ret,eof,info		
