# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import inspect, sys, os

print (sys.path[0])
print(os.getcwd())
print (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))