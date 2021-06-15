# import glob
#
# file_list = glob.glob("subdirs/**/*.py", recursive=True)
# print(len(file_list))
#

import glob
file_list = glob.glob("subdirs.zip/**/*.py", recursive=True)
print(len(file_list))