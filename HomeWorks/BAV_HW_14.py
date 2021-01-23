# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.


class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self._strength = 1
        self._agility = 1
        self._intellect = 1
        self._skill_up = 1

    def __repr__(self):
        return f"Имя: {self.name}, Клан: {self.clan}, Здоровье: {self.is_live()} \n Навыки: \n " \
               f"Интелект - {self.intellect}, Ловкость - {self.agility}, Сила - {self.strength}"

    def is_live(self):
        """ Проверяем живой или нет, функция пказывает количество зоровья """
        if self.health > 0:
            return self.health
        else:
            return f"{self.name} You died (тут типа играет музыка из Minecraft~а)"

    def reduce_health(self, amount):
        """ Функция уменьшения здоровья, параметр получает колчество урона от оружия"""
        if self.is_live():
            self.health -= amount

    def increase_health(self, amount=10):
        """ Функция повышения здоровья """
        self.health += amount
        if self.health > 100:
            self.health = 100

    @property
    def intellect(self):
        return self._intellect

    @property
    def agility(self):
        return self._agility

    @property
    def strength(self):
        return self._strength

    def base_skill_up(self):
        if self._skill_up < 10:
            self._skill_up += 1


class Mage(Unit):
    def __init__(self, name, clan, magic):
        super().__init__(name, clan)
        self.magic = magic

    @property
    def intellect(self):
        return self._skill_up

    @property
    def magic_weapon(self):
        """ Функция получает вид магии (air, water, fire) """
        if self.magic.lower() == "air":
            damage = 10
        elif self.magic.lower() == "water":
            damage = 15
        elif self.magic.lower() == "fire":
            damage = 20
        return damage


class Knight(Unit):
    def __init__(self, name, clan, weapon):
        super().__init__(name, clan)
        self.weapon = weapon

    @property
    def intellect(self):
        return self._skill_up

    @property
    def steel_arms(self):
        """ Функция получает вид оружия (sword, axe, lance) """
        if self.weapon.lower() == "sword":
            damage = 10
        elif self.weapon.lower() == "axe":
            damage = 20
        elif self.weapon.lower() == "lance":
            damage = 15
        return damage


class Archer(Unit):
    def __init__(self, name, clan, weapon):
        super().__init__(name, clan)
        self.weapon = weapon

    @property
    def agility(self):
        return self._skill_up

    @property
    def arrows_weapon(self):
        """ Функция получает вид оружия (bow, crossbow) """
        if self.weapon.lower() == "bow":
            damage = 10
        elif self.weapon.lower() == "crossbow":
            damage = 15
        return damage


mage_unit = Mage("Dumbledore", "Archmage", "Water")
knight_unit = Knight("Arthur", "Humanity", "Axe")
archer_unit = Archer("Quendi", "Pixie", "Bow")


for _ in range(2):
    knight_unit.reduce_health(mage_unit.magic_weapon)  # Маг наносит урон Рыцарю

for _ in range(15):
    mage_unit.reduce_health(archer_unit.arrows_weapon)  # Лучник убил Мага

for _ in range(2):
    mage_unit.base_skill_up()

for _ in range(1):
    mage_unit.increase_health()

for _ in range(1):
    archer_unit.base_skill_up()

for _ in range(1):
    knight_unit.increase_health()


print(mage_unit, "\n")
print(knight_unit, "\n")
print(archer_unit)
