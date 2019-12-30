from plane_sorites import *
import pygame


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 调用私有方法,精灵和精灵组创建
        self.__create_sprites()

        # 0.5s发射子弹   创建敌机 1架/s
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        """创建精灵组"""
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组

        self.enemy_group = pygame.sprite.Group()

        # 创建英雄机精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("开始游戏 ")

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 时间监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新精灵组
            self.__update_sprites()

            # 刷新屏幕
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # elif event.type ==HERO_FIRE_EVENT:
            #     self.hero.fire()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
                self.hero.fire()

        # 获取用户按键
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_UP]:
            self.hero.speedy = -2
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speedy = 2
        else:
            self.hero.speed = 0
            self.hero.speedy = 0



    def __check_collide(self):
        """碰撞检测"""

        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表时候有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束"""
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()
