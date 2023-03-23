from blocks import *
from objects import *
from monsters import *
from player import *


def level01():
    entities = pygame.sprite.Group()  # все отрисовываемые предметы
    platforms = []  # все предметы которые блокируют путь
    objects = pygame.sprite.Group()  # Все объекты с которыми можно взаимодействовать
    monsters = pygame.sprite.Group()  # Все монстры с которыми можно взаимодействовать

    level = [
        "l____________j",
        "I tttttttttttI",
        "Irrt++++++++tI",
        "Itrr+tttttt+tI",
        "Ittt+t++++t+tI",
        "I  t+tttt+t+ I",
        "It t+t++t+t+tI",
        "I   +tt+t+t+ I",
        "Ittt++++t+t+tI",
        "Iwww+tttt+t+ I",
        "I bb+t tt+t+tI",
        "I ww+   t+++ I",
        "I ww+tt tttttI",
        "L____________J"]

    level_w = len(level[0])
    level_h = len(level)
    x = y = 0

    for row in level:
        for col in row:
            pf = Ground(x, y)
            entities.add(pf)
            if col == "l":
                pf = WallA(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "_":
                pf = WallB(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "j":
                pf = WallC(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "I":
                pf = WallD(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "L":
                pf = WallE(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "J":
                pf = WallF(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "+":
                pf = Road(x, y)
                entities.add(pf)
            if col == "t":
                pf = Tree(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "r":  # скрытый путь между деревьями
                pf = Tree(x, y)
                entities.add(pf)
            if col == "w":
                pf = Water(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "b":
                pf = Bridge(x, y)
                entities.add(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    def add_obj(obj):
        entities.add(obj)
        platforms.append(obj)
        objects.add(obj)

    def add_mon(obj):
        entities.add(obj)
        platforms.append(obj)
        monsters.add(obj)

    obj = [
        Chest(48, 576, 'Ты нашёл: 100 монет', 100),
        Chest(288, 288, 'Ты нашёл: 300 монет', 300),
        Chest(48, 48, 'Ты нашёл: 500 монет', 500),
        Stairs(288, 192, 'У меня еще есть дела наверху', 0),
    ]

    for i in obj:
        add_obj(i)

    mon = [
        MonsterBat(288, 480),
        MonsterBat(336, 576),
        MonsterSlime(48, 336),
        MonsterSlime(48, 240),
        MonsterWolf(576, 240),
        MonsterWolf(576, 336),
        MonsterWolf(576, 432),
        MonsterWolf(576, 528),
        GuardBat(432, 480),
        GuardSlime(432, 336),
        GuardWolf(432, 192),
    ]

    for i in mon:
        add_mon(i)

    hero = Player(192, 576)  # начальные координаты игрока
    entities.add(hero)  # добавляем героя в массив отрисовки

    return entities, platforms, objects, monsters, hero, level_w, level_h
