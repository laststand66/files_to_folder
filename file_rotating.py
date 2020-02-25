import os
import shutil
import re

print('Hello! This program can move all files with same type into new created directory')

directory = os.path.abspath('')
directory_list = os.listdir(directory)

# print(directory_list)
# print(len(directory_list))

ext = str(input('Enter file extension that you want to move (without dot):'))


# for i in directory_list:
#     x = re.findall('.'+ext+'$', i)
#     if x:
#         print(i)
#     else:
#         pass


print('Create new dir and move files?')
a = str(input('y/n?'))
if a == 'y':
    folder_name = str(input('Enter folder name:'))
    os.mkdir(directory+('\\'+folder_name))
    for i in directory_list:
        scan_files = re.findall('.'+ext+'$', i)
        if scan_files:
            shutil.move(directory+'\\'+i, directory+'\\'+folder_name)
        else:
            pass
else:
    pass
