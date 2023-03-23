import pygame

from blocks import ICON_DIR
from objects import Object


class Monster(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/obj10.png" % ICON_DIR)
        self.attack = False
        self.attacked = False
        self.guard = False


class MonsterBat(Monster):
    def __init__(self, x, y):
        Monster.__init__(self, x, y)
        self.mon_HP = 10
        self.mon_name = 'Летучая мышь'
        self.mon_image = "%s/images/mon01.png" % ICON_DIR
        self.msg = 'Летучая мышь (HP:' + str(self.mon_HP) + ')?'
        self.mon_coin = 50
        self.mon_exp = 50


class MonsterSlime(Monster):
    def __init__(self, x, y):
        Monster.__init__(self, x, y)
        self.mon_HP = 20
        self.mon_name = 'Вонючая слизь'
        self.mon_image = "%s/images/mon02.png" % ICON_DIR
        self.msg = 'Вонючая слизь (HP:' + str(self.mon_HP) + ')?'
        self.mon_coin = 70
        self.mon_exp = 70


class MonsterWolf(Monster):
    def __init__(self, x, y):
        Monster.__init__(self, x, y)
        self.mon_HP = 30
        self.mon_name = 'Волк'
        self.mon_image = "%s/images/mon04.png" % ICON_DIR
        self.msg = 'Волк (HP:' + str(self.mon_HP) + ')?'
        self.mon_coin = 100
        self.mon_exp = 100


class GuardBat(MonsterBat):
    def __init__(self, x, y):
        MonsterBat.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/obj11.png" % ICON_DIR)
        self.guard = True


class GuardSlime(MonsterSlime):
    def __init__(self, x, y):
        MonsterSlime.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/obj11.png" % ICON_DIR)
        self.guard = True


class GuardWolf(MonsterWolf):
    def __init__(self, x, y):
        MonsterWolf.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/obj11.png" % ICON_DIR)
        self.guard = True
