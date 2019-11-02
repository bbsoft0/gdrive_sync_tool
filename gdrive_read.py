#! /usr/bin/env python
"""
Created on  Nov  1 2019
@author: bbsoft0
"""

import os

os.chdir("/home/barbu/anaconda3/lib/python3.6/site-packages/")

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)


os.chdir("/home/barbu/Notebooks/Startup/")
"""
file_list = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()
"""
#Folder Computers > Notebooks > Startup
fileList = drive.ListFile({'q': "'1VH-16kcYSqo7LxBxiIfLJ7nfEBHDxgE6' in parents and trashed=false"}).GetList()
for file in fileList:
   # Download all files in folder Notebooks > Startup
  print('Read title: %s, ID: %s' % (file['title'], file['id']))
  
  isFile = os.path.isfile(file['title']) 
  if isFile:
    file_obj = drive.CreateFile({'id': file['id']})
    file_obj.GetContentFile('/home/barbu/Notebooks/Startup/' +file['title'], mimetype='text')

print ("Program completed !")

