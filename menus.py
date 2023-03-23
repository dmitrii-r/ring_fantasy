import pygame

from blocks import f, ICON_DIR


class MsgBlock(pygame.sprite.Sprite):
    def __init__(self, msg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((480, 48))
        self.image.fill(pygame.Color('white'))
        self.rect = pygame.Rect(0, 0, 480, 48)
        pygame.draw.rect(self.image, (0, 0, 0), (2, 2, 476, 44), 2)
        t_msg = str(msg)
        text = f.render(t_msg, True, (0, 0, 0))
        pos = text.get_rect(center=(240, 24))
        self.image.blit(text, pos)


class MsgBlockMon(pygame.sprite.Sprite):
    def __init__(self, msg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((480, 96))
        self.image.fill(pygame.Color('white'))
        self.rect = pygame.Rect(0, 0, 480, 96)
        pygame.draw.rect(self.image, (0, 0, 0), (2, 2, 476, 92), 2)
        t_msg = 'Напасть на ' + str(msg)
        text = f.render(t_msg, True, (0, 0, 0))
        pos = text.get_rect(center=(240, 24))
        self.image.blit(text, pos)


class MsgBlockWin(pygame.sprite.Sprite):
    def __init__(self, msg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((480, 96))
        self.image.fill(pygame.Color('white'))
        self.rect = pygame.Rect(0, 0, 480, 96)
        pygame.draw.rect(self.image, (0, 0, 0), (2, 2, 476, 92), 2)
        t_msg_1 = 'Ты победил'
        t_msg_2 = str(msg)
        text_1 = f.render(t_msg_1, True, (0, 0, 0))
        pos = text_1.get_rect(center=(240, 24))
        self.image.blit(text_1, pos)
        text_2 = f.render(t_msg_2, True, (0, 0, 0))
        pos = text_2.get_rect(center=(240, 72))
        self.image.blit(text_2, pos)


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, msg, action=None):
        pygame.sprite.Sprite.__init__(self)
        self.btn_action = action
        self.w = 150
        self.h = 40
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(pygame.Color('white'))
        self.rect = pygame.Rect(x, y, self.w, self.h)
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, self.w, self.h-2), 1)
        text = f.render(msg, True, (0, 0, 0))
        pos = text.get_rect(center=(self.w/2, self.h/2-2))
        self.image.blit(text, pos)
        self.i = True

    def update(self):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x < cursor[0] < self.rect.x+self.w and self.rect.y < cursor[1] < self.rect.y+self.h:
            pygame.draw.rect(self.image, (0, 0, 0), (2, 2, self.w-4, self.h-6), 2)
            if self.btn_action is not None:
                if click[0] == 1 and self.i:
                    self.btn_action()
                    self.i = False
                elif click[0] == 0:
                    self.i = True
        else:
            pygame.draw.rect(self.image, (255, 255, 255), (2, 2, self.w-4, self.h-6), 2)


class MenuPlayer(pygame.sprite.Sprite):
    def __init__(self, LEVEL, EXP, ATT, DEF, HP, HP_player, COINS, weapon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((480, 480))
        self.image.fill(pygame.Color('white'))
        self.rect = pygame.Rect(0, 0, 480, 480)
        pygame.draw.rect(self.image, (0, 0, 0), (2, 2, 476, 476), 2)
        step = 38
        self.image.blit(f.render(('Уровень: ' + str(LEVEL)), True, (0, 0, 0)), (48, step))
        self.image.blit(f.render(('До следующего уровня: ' + str(EXP)), True, (0, 0, 0)), (48, step*2))
        self.image.blit(f.render(('Атака: ' + str(ATT)), True, (0, 0, 0)), (48, step*3))
        self.image.blit(f.render(('Защита: ' + str(DEF)), True, (0, 0, 0)), (48, step*4))
        self.image.blit(f.render(('Здоровье: ' + str(HP_player) + '/' + str(HP)), True, (0, 0, 0)), (48, step*5))
        self.image.blit(f.render(('Монеты: ' + str(COINS)), True, (0, 0, 0)), (48, step*6))
        self.image.blit(f.render(('Оружие: ' + str(weapon)), True, (0, 0, 0)), (48, step*7))


class MenuBattle(pygame.sprite.Sprite):
    def __init__(self, mon_HP, HP, p_HP, mon_image):
        pygame.sprite.Sprite.__init__(self)
        self.pl_HP = None
        self.mon_HP = mon_HP
        self.p_HP = p_HP
        self.mes_1 = 'Ты готов к атаке'
        self.mes_2 = 'выбери действие:'
        self.image = pygame.Surface((480, 480))
        self.image.fill(pygame.Color('white'))
        self.rect = pygame.Rect(0, 0, 480, 480)
        self.upd = True
        self.mon_image = mon_image
        self.mon_HP_rect = (20, 68, 324, 28)
        w = 324 - int(324 - (324 / HP) * p_HP)
        self.p_HP_rect = (136, 192, w, 28)
        self.p_rect_color = (0, 0, 255)
        self.mon_rect_color = (255, 255, 255)
        self.text_rect_color = (0, 0, 255)

    def update(self):
        if self.upd:
            self.upd = False
            self.image.fill(pygame.Color('white'))
            pygame.draw.rect(self.image, (0, 0, 0), (2, 2, 476, 476), 2)
            self.image.blit(pygame.image.load(self.mon_image), (364, 68, 96, 96))  # картинка с монстром
            self.image.blit(pygame.image.load("%s/images/mon18.png" % ICON_DIR), (20, 124, 96, 96))  # картинка с игроком
            pygame.draw.rect(self.image, self.mon_rect_color, (364, 68, 96, 96), 4)   # рамка монстра
            pygame.draw.rect(self.image, self.p_rect_color, (20, 124, 96, 96), 4)   # рамка игрока
            pygame.draw.rect(self.image, (255, 0, 0), (20, 68, 324, 28))   # HP монстра
            pygame.draw.rect(self.image, (255, 0, 0), (136, 192, 324, 28))     # HP игрока
            pygame.draw.rect(self.image, (0, 255, 0), self.mon_HP_rect)   # текущий HP монстра
            pygame.draw.rect(self.image, (0, 255, 0), self.p_HP_rect)     # текущий HP игрока
            pygame.draw.rect(self.image, self.text_rect_color, (20, 240, 440, 96), 4)   # рамка текста
            self.image.blit(f.render(('HP:' + str(self.mon_HP)), True, (0, 0, 0)), (270, 108))
            self.pl_HP = 'HP:' + str(self.p_HP)  # + '/' + '10'

            self.image.blit(f.render(self.pl_HP, True, (0, 0, 0)), (136, 152))
            self.image.blit(f.render(self.mes_1, True, (0, 0, 0)), (40, 249))
            self.image.blit(f.render(self.mes_2, True, (0, 0, 0)), (40, 287))
