#!/usr/bin/python
# -*- coding: utf-8 -*-
 
 
import smtplib
import mimetypes
import poplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

 
import cStringIO
import email
import base64
 
 
def sendmail(status=True, runtime):
    sender = '************'
    receiver = '************'
    subject = ''
    if status:
        subject ='************ backup2baidupcs is OK'
    else:
        subject ='************ backup2baidupcs is Fail'
    smtpserver = '************'
    username = sender
    password = '************'
 
    msg = MIMEMultipart() 
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    txt = MIMEText("")
    txt = MIMEText("runtime is %s" %(runtime))
    msg.attach(txt) 

 
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
