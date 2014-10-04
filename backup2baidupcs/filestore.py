#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

class filestore:
     resultfile = []
     files = []
     localpath = None

     def __init__(self,localpath=os.getcwd()):
          self.files = os.listdir(localpath)
          self.localpath = localpath


     def removefile(self,filename):
          os.remove(filename)


     def list_files(self):
          for ff in self.files:
	      if os.path.splitext(ff)[1] == '.gz':
                   self.resultfile.append(ff)

