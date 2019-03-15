import os
for i in range(1, 10):
    if os.path.exists(f'dir_{i}'):
        os.removedirs(f'dir_{i}')
    else:
        print('Такой директории не существует')

