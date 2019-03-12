
# создать папку

def dev_dir():
        if os.path.exists(f'{i}'):
            print('Папка уже существует')
        else:
            os.mkdir(f'{i}')
            print ('Папка'{i}'успешно создана')

# перейти в папку

def ch_dir():

    try:
        os.chdir(dirs)
        print('Успешно перешел.')
    except FileExistsError:
        print(f'Невозможно перейти. Папки {dirs} не существует.')

# посмотреть содержимое папки

def list_dir():
    for i in os.listdir():
    print(i)

# удалить папку

def remove_dir(dirs):
    import shutil
    try:
        shutil.rmtree(dirs)
        print('Успешно удалил.')
    except FileExistsError:
        print(f'Невозможно удалить. Папки {dirs} не существует.')




