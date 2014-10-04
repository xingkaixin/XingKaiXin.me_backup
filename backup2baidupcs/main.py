#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import os

start = time.clock()
srcpath = '/home/wwwroot/default/wp-content/uploads/backwpup/'
targetpath = '/root/************/app/backup_wp'

os.system('mv %s/*.tar.gz %s' %(srcpath,targetpath))


from filestore import filestore

f = filestore()
f.list_files()
print f.resultfile


from pcs import baidupcsbak
from mail import sendmail
bd = baidupcsbak('************')
bd.connPCS()
for ff in f.resultfile:
  bd.upload_file(ff,'/apps/************/%s' %(ff))
  f.removefile(ff)
  print bd.pcsflag, bd.filesize
  end = time.clock()
  runtimer = end - start
  if bd.pcsflag:
    sendmail(True, runtimer)
  else:
    sendmail(False, runtimer)
