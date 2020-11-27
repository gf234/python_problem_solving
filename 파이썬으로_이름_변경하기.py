import os

file_path = os.getcwd()
file_names = os.listdir(file_path)

for name in file_names:
    src = os.path.join(file_path, name)
    dst = name.replace(' ', '_')
    dst = os.path.join(file_path, dst)
    if src != dst:
        os.rename(src,dst)