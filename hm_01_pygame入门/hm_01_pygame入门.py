import pygame

pygame.init()

hero_rect = pygame.Rect(100, 500, 120, 126)
print("坐标原点  %d  %d" % (hero_rect.x, hero_rect.y))
print("英雄大小  %d  %d" % (hero_rect.width, hero_rect.height))
# hero_rect.size=(hero_rect.width, hero_rect.height)
print("英雄大小 %d  %d " % hero_rect.size)

# 创建游戏窗口
screen = pygame.display.set_mode((400, 700))

# 加载背景图片
bg = pygame.image.load("./images/background.png")

# 绘制
screen.blit(bg, (0, 0))

# 加载英雄鸡
hero = pygame.image.load("./images/me1.png")

# 绘制
screen.blit(hero, (200, 500))

# 更新显示
pygame.display.update()

# 创建游戏时钟对象
clock = pygame.time.Clock()
i = 0

# 指定英雄的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)


import plane_main
# 游戏循环不退出
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)

    # 上移1个单位
    hero_rect.y -= 1
    # 限制飞机移动上顶 下底范围
    if hero_rect.y <= 0:
        hero_rect.y = 0
    if hero_rect.y + hero_rect.height >= 700:
        hero_rect.y = 700 - hero_rect.height

    # 绘制背景图片英雄图片
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 更新显示
    pygame.display.update()

pygame.quit()
