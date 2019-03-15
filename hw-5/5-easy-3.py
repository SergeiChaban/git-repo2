# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import inspect,shutil,os
from shutil import copyfile
shutil.copy((inspect.getfile(inspect.currentframe())), 'new_file_v1.py')
copyfile((inspect.getfile(inspect.currentframe())), 'new_file_v2.py')

