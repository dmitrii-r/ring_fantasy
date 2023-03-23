import random

from globals import *
from levels import level01
from menus import *


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)


def main():
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('Ring Fantasy')
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    left = right = False
    up = down = False
    info_open = False

    menu = pygame.sprite.Group()  # все меню

    timer = pygame.time.Clock()

    entities, platforms, objects, monsters, hero, level_w, level_h = level01()   # загружаем первый уровень

    total_level_width = level_w * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = level_h * PLATFORM_HEIGHT  # Высчитываем фактическую высоту уровня

    camera = Camera(camera_configure, total_level_width, total_level_height)

    def menu_player():  # вызов меню игрока
        global menu_open
        if menu_open:
            menu.empty()
            menu_open = False
        else:
            mn = MenuPlayer(LEVEL, EXP, ATT, DEF, HP, HP_player, COINS, weapon)
            menu.add(mn)
            butt = Button(WIN_WIDTH / 2 - 150 / 2, 422, 'Назад', menu_close)
            menu.add(butt)
            menu_open = True

    def menu_close():
        global menu_open
        menu.empty()
        menu_open = False

    def run_away():
        global menu_open
        menu.empty()
        menu_open = False
        for p in monsters:
            if p.attack:
                p.attack = False

    def menu_battle():
        global menu_open
        menu.empty()
        used = False

        def healing():
            global HP_player
            HP_player += 20
            if HP_player > HP:
                HP_player = HP
            mn.p_HP = HP_player
            w = 324 - int(324 - (324 / HP) * mn.p_HP)
            mn.p_HP_rect = (136, 192, w, 28)
            mn.upd = True
            mn.update()
            menu.draw(screen)
            pygame.display.update()

        def battle_win():
            global menu_open
            global COINS
            global EXP

            menu_open = True
            msg = 'опыт +' + str(mon_exp) + ', монеты +' + str(mon_coin)
            info = MsgBlockWin(msg)
            menu.add(info)
            menu.draw(screen)
            pygame.display.update()
            COINS += mon_coin
            EXP -= mon_exp
            for p in monsters:
                if p.attacked:
                    # p.used = True     # запрет повторного нападения на монстров
                    p.attacked = False
                    if p.guard:
                        monsters.remove(p)
                        entities.remove(p)
                        platforms.remove(p)

            pygame.time.wait(1000)
            menu.empty()
            menu_open = False

        def battle():
            global HP
            global HP_player
            global ATT
            global DEF
            p_dmg = ATT - mon_HP
            crit = random.choice([False, True])
            p_dmg = random.choice([p_dmg, p_dmg + 1, p_dmg + 2, p_dmg + 3])
            if p_dmg < 2:
                p_dmg = 2
                mn.mes_2 = 'наносишь урон ' + str(p_dmg)
            elif crit:
                p_dmg = p_dmg * 2
                mn.mes_2 = 'наносишь критический урон ' + str(p_dmg)
            else:
                mn.mes_2 = 'наносишь урон ' + str(p_dmg)

            mn.mon_HP = mn.mon_HP - p_dmg
            z = int(324 - (324/mon_HP)*mn.mon_HP)
            x = 20 + z
            w = 324 - z
            mn.mon_HP_rect = (x, 68, w, 28)
            mn.p_rect_color = (0, 0, 255)
            mn.text_rect_color = (0, 0, 255)
            mn.mon_rect_color = (255, 255, 255)
            if mn.mon_HP <= 0:
                mn.mon_HP = 0

            mn.mes_1 = 'Ты атакуешь:'
            mn.upd = True
            mn.update()
            menu.draw(screen)
            pygame.display.update()
            pygame.time.wait(1500)

            if mn.mon_HP == 0:
                menu.empty()
                display_update()
                battle_win()
                return

            # ход монстра
            m_dmg = mon_HP - DEF
            crit = random.choice([False, True])
            m_dmg = random.choice([m_dmg, m_dmg + 1, m_dmg + 2, m_dmg + 3])
            if m_dmg < 1:
                m_dmg = 1
                mn.mes_2 = 'наносит урон ' + str(m_dmg)
            elif crit:
                m_dmg = int(m_dmg * 1.5)
                mn.mes_2 = 'наносит критический урон ' + str(m_dmg)
            else:
                mn.mes_2 = 'наносит урон ' + str(m_dmg)

            HP_player = HP_player - m_dmg
            if HP_player <= 0:
                HP_player = 0
            mn.p_HP = HP_player
            w = 324 - int(324 - (324 / HP) * mn.p_HP)
            mn.p_HP_rect = (136, 192, w, 28)
            mn.p_rect_color = (255, 255, 255)
            mn.text_rect_color = (255, 0, 0)
            mn.mon_rect_color = (255, 0, 0)
            mn.mes_1 = 'Противник атакует:'
            mn.upd = True
            mn.update()
            menu.draw(screen)
            pygame.display.update()
            pygame.time.wait(1500)
            if mn.p_HP <= 0:
                menu_close()
            # выбор действия
            mn.mes_1 = 'Ты готов к атаке'
            mn.mes_2 = 'выбери действие:'
            mn.p_rect_color = (0, 0, 255)
            mn.text_rect_color = (0, 0, 255)
            mn.mon_rect_color = (255, 255, 255)
            mn.upd = True
            mn.update()
            menu.draw(screen)
            pygame.display.update()

        for p in monsters:
            if p.attack:
                mon_HP = p.mon_HP
                mon_exp = p.mon_exp
                mon_coin = p.mon_coin
                mon_image = p.mon_image
                p_HP = HP_player
                p.attack = False
                p.attacked = True
            elif used:
                p.used = True


        mn = MenuBattle(mon_HP, HP, p_HP, mon_image)
        menu.add(mn)
        butt = Button(88, 356, 'Атаковать', battle)
        menu.add(butt)
        butt = Button(242, 356, 'Лечиться', healing)
        menu.add(butt)
        butt = Button(88, 400, 'Магия')
        menu.add(butt)
        butt = Button(242, 400, 'Сбежать', run_away)
        menu.add(butt)

    def info_battle(p):
        global menu_open
        menu_open = True
        info = MsgBlockMon(p.msg)
        menu.add(info)
        button1 = Button(88, 50, 'Напасть', menu_battle)
        menu.add(button1)
        button = Button(242, 50, 'Сбежать', run_away)
        menu.add(button)
        p.attack = True

    run = True
    while(run):
        timer.tick(10)

        global menu_open
        global EXP
        global COINS
        global LEVEL
        global ATT
        global DEF
        global HP
        global HP_player
        global MP
        global weapon

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                up = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                down = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                menu_player()

            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                up = False
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = False
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                down = False

        for p in objects:   # сообщение при взаимодействии с объектом
            if p.call_msg and not info_open:
                COINS += p.coins
                info_open = True
                info = MsgBlock(p.msg)
                menu.add(info)
                i = 0
                break
            elif info_open and i == 0:
                pygame.time.wait(500)
                i = 1
                break
            elif info_open and (left or right or up or down):
                menu.empty()
                info_open = False

        for p in monsters:   # сообщение при взаимодействии с монстром
            if p.call_msg and not menu_open:
                info_battle(p)

        if EXP <= 0:
            LEVEL += 1
            EXP = startEXP + 200
            ATT += 2
            DEF += 2
            HP += 8
            MP += 4

        def display_update():
            global menu_open
            screen.blit(bg, (0, 0))      # Каждую итерацию необходимо всё перерисовывать
            camera.update(hero)      # центрируем камеру относительно персонажа
            objects.update(hero, left, right, up, down)     # апдейт предметов
            monsters.update(hero, left, right, up, down)    # апдейт предметов
            hero.update(left, right, up, down, platforms, menu_open)     # апдейт игрока
            entities.draw(screen)   # Расстановка объектов

            for e in entities:
                screen.blit(e.image, camera.apply(e))
                menu.draw(screen)
                menu.update()
            pygame.display.update()

        display_update()
    pygame.quit()


main()
