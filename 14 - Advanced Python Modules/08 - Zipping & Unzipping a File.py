# slashes may need to change for MacOS or Linux
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

# slashes may need to change for MacOS or Linux
f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('new_file.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')

import shutil

dir_to_zip = '/home/osustam/extracted_content'
output_file_name = 'example'
shutil.make_archive(output_file_name, 'zip', dir_to_zip)
shutil.unpack_archive('/home/osustam/example.zip', 'final_unzip', 'zip')
