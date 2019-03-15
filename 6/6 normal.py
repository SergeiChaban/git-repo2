# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
class Person:
    def init(self, name, health, damage, armor):
    self.name = name
    self.health = health
    self.damage = damage
    self.armor = armor

    def unit_name (self):
    self.name = input('Введите имя: ')

    def unit_health (self):
    self.health = 100
    print(self.health)

    def unit_damage (self):
    self.damage = 50
    print (self.damage)

    def unit_armor (self):
    self.armor = 50
    print (self.armor)

Class Enemy(Person):
    def attack (self):
    print(f'Характеристика игрока {self.name}: Здоровье {self.health}, Урон {self.damage}, Защита {self.armor}')

Class Player(Person)
    def attack (self):
    print(f'Характеристика игрока {self.name}: Здоровье {self.health}, Урон {self.damage}, Защита {self.armor}')

