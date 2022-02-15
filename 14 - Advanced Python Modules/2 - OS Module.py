f = open('/home/oben/Udemy-Complete-Python-3-Bootcamp/14 - Advanced Python Modules/practice.txt','w+')
f.writelines('text file')
f.close()

print()

import os

print(os.getcwd())
print(os.listdir('/home/oben/Udemy-Complete-Python-3-Bootcamp'))

print()

import shutil
shutil.move('/home/oben/Udemy-Complete-Python-3-Bootcamp/14 - Advanced Python Modules/practice.txt', '/home/oben/ML')

print()

# Delete file but not permanently
import send2trash
send2trash.send2trash('/home/oben/ML/practice.txt')

print()

for folder , sub_folders , files in os.walk("/home/oben/Udemy-Complete-Python-3-Bootcamp/14 - Advanced Python Modules"): 
    print("Currently looking at folder: "+ folder)
    print('\n')

    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')


