import pygame

from globals import PLAYER_WIDTH, PLAYER_HEIGHT, ICON_DIR, PLAYER_STEP


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.yvel = 0
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = pygame.image.load('%s/images/obj40.png' % ICON_DIR)
        self.stepUp = pygame.image.load('%s/images/obj40.png' % ICON_DIR)
        self.stepLeft = pygame.image.load('%s/images/obj41.png' % ICON_DIR)
        self.stepRight = pygame.image.load('%s/images/obj42.png' % ICON_DIR)
        self.stepDown = pygame.image.load('%s/images/obj43.png' % ICON_DIR)

    def update(self, left, right, up, down, platforms, menu_open):
        if up and not(right or left or down) and not menu_open:
            self.yvel = -PLAYER_STEP
            self.xvel = 0
            self.image.blit(self.stepUp, (0, 0))
        if left and not(up or right or down) and not menu_open:
            self.xvel = -PLAYER_STEP
            self.yvel = 0
            self.image.blit(self.stepLeft, (0, 0))
        if right and not (up or left or down) and not menu_open:
            self.xvel = PLAYER_STEP
            self.yvel = 0
            self.image.blit(self.stepRight, (0, 0))
        if down and not (right or left or up) and not menu_open:
            self.yvel = PLAYER_STEP
            self.xvel = 0
            self.image.blit(self.stepDown, (0, 0))
        if not (left or right or up or down):
            self.xvel = 0
            self.yvel = 0
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                if yvel < 0:
                    self.rect.top = p.rect.bottom
