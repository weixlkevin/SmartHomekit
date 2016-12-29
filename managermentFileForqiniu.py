# encoding:'utf-8'
from qiniu import Auth, put_file, etag, urlsafe_base64_encode,BucketManager
import qiniu.config
import requests

classs managerfile:
	def __init__(self):
		access_key='jfPxDEq31sT7lx8indvCAtjXH6PyUXZARn0Cr6-6'
		secret_key='Hfh6063CzsY24qPQCeFtdbsGf5VdisL_5koUbkha'
		bucket_name='weixlkevin-cloud'
		bucket_domain='oigm0qwlo.bkt.clouddn.com'
		q=Auth(access_key,secret_key)

	def uploadfile(self,fileName,filePath):
		token=self.q.upload_token(self.bucket_name,fileName,3600)
		ret,info=put_file(token,fileName,filePath)

	def downloadfile(self,fileName):
		base_url='http://%s/%s' %(self.bucket_domain,fileName)
		private_url=q.private_download_url(base_url,expires=3600)
		r=requests.get(private_url)
		if(r.status_code==200):
			return r.text
		else:
			return "download fail."

	def getfileinfo(self,fileName):
		bucket=BucketManager(self.q)
		ret,info=bucket.stat(bucket_name,fileName)
		return info

	def getfileslist(self,count):
		bucket=BucketManager(self.q)
		if(count==-1):
			limit=0
		else:
			limit=count
		ret,eof,info=bucket.list(bucket_name,None,None,limit,None)
		return info		
