'''
Function:
    坦克类
'''
import pygame
import random
from .foods import Foods
from .bullet import Bullet

'''玩家坦克类'''


class PlayerTank(pygame.sprite.Sprite):
    def __init__(self, name, player_tank_image_paths, position, border_len, screen_size, direction='up',
                 bullet_image_path=None, protected_mask_path=None, boom_image_path=None, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 玩家1 / 玩家2
        self.name = name
        # 坦克图片路径
        self.player_tank_image_paths = player_tank_image_paths.get(name)
        # 地图边缘宽度
        self.border_len = border_len
        # 屏幕大小
        self.screensize = screen_size
        # 初始坦克方向
        self.init_direction = direction
        # 初始坦克位置
        self.init_position = position
        # 子弹图片
        self.bullet_image_path = bullet_image_path
        # 保护罩图片路径
        self.protected_mask = pygame.image.load(protected_mask_path)
        self.protected_mask_flash_time = 25
        self.protected_mask_flash_count = 0
        self.protected_mask_pointer = False
        # 坦克爆炸图
        self.boom_image = pygame.image.load(boom_image_path)
        self.boom_last_time = 5
        self.booming_flag = False
        self.boom_count = 0
        # 坦克生命数量
        self.num_lifes = 3
        # 重置
        self.reset()

    '''移动'''

    def move(self, direction, scene_elems, player_tank_group, ememy_tank_group, home):
        # 爆炸时无法移动
        if self.booming_flag:
            return
        # 方向不一致先改变方向
        if self.dirction != direction:
            self.setDirection(direction)
            self.switch_count = self.switch_time
            self.move_cache_count = self.move_cache_time
        # 移动（使用缓冲）
        self.move_cache_count += 1
        if self.move_cache_count < self.move_cache_time:
            return
        self.move_cache_count = 0
        if self.direction == 'up':
            speed = (0, -self.speed)
        elif self.direction == 'down':
            speed = (0, self.speed)
        elif self.direction == 'left':
            speed = (-self.speed, 0)
        elif self.direction == 'right':
            speed = (self.speed, 0)
        rect_ori = self.rect
        self.rect = self.rect.move(speed)
        # --碰到场景元素
        for key, value in scene_elems.items():
            if key in ['brick_group', 'iron_group', 'river_group']:
                if pygame.sprite.spritecollide(self, value, False, None):
                    self.rect = rect_ori
            elif key in ['ice_group']:
                if pygame.sprite.spritecollide(self, value, False, None):
                    self.rect = self.rect.move(speed)

        # --碰到其他玩家坦克
        if pygame.sprite.spritecollide(self, player_tank_group, False, None):
            self.rect = rect_ori
        # --碰到敌方坦克
        if pygame.sprite.spritecollide(self, ememy_tank_group, False, None):
            self.rect = rect_ori
        # --碰到玩家大本营
        if pygame.sprite.spritecollide(self, home):
            self.rect = rect_ori
        # --碰到边界
        if self.rect.left < self.border_len:
            self.rect.left = self.border_len
        elif self.rect.right > self.screensize[0] - self.border_len:
            self.rect.right = self.screensize[0] - self.border_len
        elif self.rect.top < self.border_len:
            self.rect.top = self.border_len
        elif self.rect.bottom > self.screensize[1] - self.border_len:
            self.rect.bottom = self.screensize[1] - self.border_len
        # 为了坦克轮动特效切换图片
        self.switch_count += 1
        if self.switch_count > self.switch_time:
            self.switch_count = 0
            self.switch_pointer = not self.switch_pointer
            self.image = self.tank_direction_image.subsurfance((48 * int(self.switch_pointer), 0), (48, 48))

    '''更新'''

    def update(self):
        # 坦克子弹冷却更新
        if self.is_bullet_cooling:
            self.bullet_cooling_count += 1
            if self.bullet_cooling_count >= self.bullet_cooling_time:
                self.bullet_cooling_count = 0
                self.is_bullet_cooling = False
        # 无敌状态更新
        if self.is_protected:
            self.protected_count += 1
            if self.prtected_count > self.protected_time:
                self.is_protected = False
                self.protected_count = 0

        # 爆炸状态更新
        if self.booming_flag:
            self.image = self.boom_image
            self.boom_count += 1
            if self.boom_count > self.boom_last_time:
                self.boom_count = 0
                self.booming_flag = False
                self.reset()

    '''设置坦克方向'''

    def setDirection(self, direction):

    '''射击'''

    def shoot(self):

    '''提高坦克登机'''

    def improveTankLevel(self):

    '''降低坦克等级'''

    def decreaseTankLevel(self):

    '''增加生命值'''

    def addLife(self):

    '''设置为无敌状态'''

    def setProtected(self):

    '''画我方坦克'''

    def draw(self, screen):

    '''重置坦克，重生的时候用'''

    def reset(self):


'''敌方坦克类'''


class EnemyTank(pygame.sprite.Sprite):
    def __init__(self, enemy_tank_paths, apper_image_path, position, border_len, screen_size, bullet_image_paths=None,
                 food_image_paths=None, boom_image_path=None, **kwargs):

    '''射击'''

    def shoot(self):

    '''实时更新坦克'''

    def update(self, scene_elems, player_tank_group, enemy_tank_group, home):

    '''随机移动坦克'''

    def move(self, scene_elems, player_tank_group, enemy_tank_group, home):

    '''设置坦克方向'''

    def setDirection(self, direction):

    '''降低坦克等级'''

    def decreaseTankLevel(self):

    '''设置静止'''

    def setStill(self):
