import pygame

from globals import PLATFORM_WIDTH, PLATFORM_HEIGHT, ICON_DIR

pygame.font.init()
f = pygame.font.SysFont('arial', 30)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Ground(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/tile01.png" % ICON_DIR)


class Road(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/tile04.png" % ICON_DIR)


class Tree(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/obj12.png" % ICON_DIR)


class WallA(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/bd01.png" % ICON_DIR)


class WallB(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/bd04.png" % ICON_DIR)


class WallC(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/bd02.png" % ICON_DIR)


class WallD(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/bd03.png" % ICON_DIR)


class WallE(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/bd05.png" % ICON_DIR)


class WallF(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/bd06.png" % ICON_DIR)


class Water(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/tile10.png" % ICON_DIR)


class Bridge(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/tile15.png" % ICON_DIR)
