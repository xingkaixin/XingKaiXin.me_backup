#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import time
from baidupcs import PCS,InvalidToken

class baidupcsbak:

     verify = False
     baidu_accesstoken = None
     pcs = None
     pcsflag = False
     filesize = None

     filetimestamp = None

     local_path = os.getcwd()


     def __init__(self,token):
          files = os.listdir(self.local_path)
          self.baidu_accesstoken = token
          self.filetimestamp = time.strftime("%Y%m%d")

     def connPCS(self):
          try:
               pcs = PCS(self.baidu_accesstoken)
               reponse = pcs.info()
               if reponse.ok:
                    self.pcsflag = True
                    self.pcs = pcs
               else:
                    self.pcsflag = False
          except InvalidToken, ex:
               print InvalidToken,":",ex
          except Exception, ex:
               self.pcsflag = False
               print Exception,":",ex


     def download_file(self, remotepath, localpath):
          with open(localpath,'wb') as f:
               reponse = self.pcs.download(remotepath, verify=self.verify)
               f.write(reponse.content)
               if reponse.ok:
                    self.pcsflag = True
               else:
                    self.pcsflag = False


     def upload_file(self, localpath, remotepath):
          with open(localpath,'rb') as f:
               reponse = self.pcs.upload(remotepath, f, ondup='overwrite', verify=self.verify)
               if reponse.ok:
                    self.pcsflag = True
                    filesize = reponse.json()['size']/1024
                    if filesize > 1024:
                         self.filesize = str(reponse.json()['size']/1024/1024) + ' MB'
                    else:
                         self.filesize = str(filesize) + ' KB'
               else:
                    self.pcsflag = False


