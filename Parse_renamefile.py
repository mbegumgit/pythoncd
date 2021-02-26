import os
os.chdir("D:/umrah photos")
print(os.getcwd())
for f in os.listdir():
    file_name,  file_ext = os.path.splitext(f)
    if file_ext == '.JPG':
        f_type, f_no = file_name.split('_')
        f_no = f_no[1:].zfill(3)
        new_name  = f'{f_no}-Umrah-{f_type}{file_ext}'
        os.rename(f,new_name)
    print(f)

