# How to recursively delete a Directory in Python

import shutil
import os

path_to_directory = './my-directory'

# 👇️ True
print(os.path.isdir(path_to_directory))

shutil.rmtree(path_to_directory)

# 👇️ False
print(os.path.isdir(path_to_directory))

print('Directory deleted successfully')
