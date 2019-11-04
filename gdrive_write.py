#! /usr/bin/env python
"""
Created on  Nov  1 2019
@author: bbsoft0
"""

import glob, os

os.chdir("/home/barbu/anaconda3/lib/python3.6/site-packages/")

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#os.chdir("/home/barbu/Python/")
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

"""
file_list = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()
"""
#Folder Computers > Notebooks > Startup
os.chdir("/home/barbu/Notebooks/StartupGlobal/")
for file in glob.glob("*.txt"):
    with open(file,"r") as f:
        fn = os.path.basename(f.name)
        #TODO Improve file_list so it founds only one file
    #    file_list = drive.ListFile({'q': "'1VH-16kcYSqo7LxBxiIfLJ7nfEBHDxgE6' in parents"}).GetList()
        stuff ="title='%s' and ('13apW5qYwNNX6wMDB803PZ5kmJOjxs48z' in parents) and trashed=false" % (f.name)
        file_list = drive.ListFile({'q': stuff}).GetList()

       # for file1 in file_list:
        file1=file_list[0]
        print('title: %s, id: %s' % (file1['title'], file1['id']))
        updated_content = f.read()
        file1.SetContentString(updated_content)
        file1.Upload()

print ("Program completed !")
