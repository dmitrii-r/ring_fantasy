import pygame

from blocks import Platform, ICON_DIR


class Object(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.ready_to_use = False
        self.used = False
        self.call_msg = False

    def update(self, hero, left, right, up, down):
        self.action()
        if left and not (right or up or down) and self.rect.x + 48 == hero.rect.x and self.rect.y == hero.rect.y:
            self.ready_to_use = True
        elif right and not (left or up or down) and self.rect.x - 48 == hero.rect.x and self.rect.y == hero.rect.y:
            self.ready_to_use = True
        elif up and not (right or left or down) and self.rect.x == hero.rect.x and self.rect.y + 48 == hero.rect.y:
            self.ready_to_use = True
        elif down and not (right or up or left) and self.rect.x == hero.rect.x and self.rect.y - 48 == hero.rect.y:
            self.ready_to_use = True

    def action(self):
        self.call_msg = False
        if self.ready_to_use and not self.used:
            self.ready_to_use = False
            self.call_msg = True


class Chest(Object):
    def __init__(self, x, y, msg, coins):
        Object.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/tile23.png" % ICON_DIR)
        self.chest_open = pygame.image.load("%s/images/tile24.png" % ICON_DIR)
        self.msg = msg
        self.coins = coins

    def action(self):
        self.call_msg = False
        if self.used:
            self.image.blit(self.chest_open, (0, 0))
        if self.ready_to_use and not self.used:
            self.image.blit(self.chest_open, (0, 0))
            self.used = True
            self.call_msg = True
            self.ready_to_use = False


class Stairs(Object):
    def __init__(self, x, y, msg, coins):
        Object.__init__(self, x, y)
        self.image = pygame.image.load("%s/images/tile19.png" % ICON_DIR)
        self.msg = msg
        self.coins = coins
