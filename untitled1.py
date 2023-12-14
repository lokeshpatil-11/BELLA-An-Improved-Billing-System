'''#import re module
import re

def pr(i,s):
    j=i
    try: 
        while j!=' ':
            print(s[j], end='')
            j+=1
    except:
        print()
    
#Open the text file, and read the text file into a list
with open('test.txt') as ocr:
    Text = ocr.readlines()

for line in Text:
    ch=re.search('mrp', line)
    try:
        pr(ch.end(), line)
    except:
        print()
        
        
'''
import os
os.chdir(r"D:\spyder_programs_python\BELLA\01")



from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 


upload_file_list = ['test1.jpg']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1rkbDkxytMF3HtQPobB4eoYnBEn-MK6ae'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.
    


file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1rkbDkxytMF3HtQPobB4eoYnBEn-MK6ae')}).GetList()
for file in file_list:
	print('title: %s, id: %s' % (file['title'], file['id']))
    
