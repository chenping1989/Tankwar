'''
Function:
    用于运行某一游戏关卡
'''
import sys
import pygame
import random
from Tankwar.modules.sprites.home import *
from Tankwar.modules.sprites.tanks import *
from Tankwar.modules.sprites.scenes import *

'''用于运行某一游戏关卡'''


class GameLevel():
    def __init__(self, gamelevel, levelfilepath, sounds, is_dual_mode, cfg, **kwargs):
        # 关卡地图路径
        self.gamelevel = gamelevel
        self.levelfilepath = levelfilepath
        # 音效
        self.sounds = sounds
        # 是否为双人模式
        self.is_dual_mode = is_dual_mode
        # 地图规模参数
        self.border_len = cfg.BORDER_LEN
        self.grid_size = cfg.GRID_SIZE
        self.width, self.height = cfg.WIDTH, cfg.HEIGHT
        self.panel_width = cfg.PANEL_WIDTH
        # 图片路径
        self.scene_image_paths = cfg.SCENE_IMAGE_PATHS
        self.other_image_paths = cfg.OTHER_IMAGE_PATHS
        self.player_tank_image_paths = cfg.PLAYER_TANK_IMAGE_PATHS
        self.bullet_image_paths = cfg.BULLET_IMAGE_PATHS
        self.enemy_tank_image_paths = cfg.ENEMY_TANK_IMAGE_PATHS
        self.food_image_paths = cfg.FOOD_IMAGE_PATHS
        self.home_image_paths = cfg.HOME_IMAGE_PATHS
        # 字体
        self.font = pygame.font.Font(cfg.FONTPATH, cfg.HEIGHT // 30)
        # 关卡场景元素
        self.scene_elems = {
            'brick_group': pygame.sprite.Group(), 'iron_group': pygame.sprite.Group(),
            'ice_group': pygame.sprite.Group(), 'river_group': pygame.sprite.Group(),
            'tree_group': pygame.sprite.Group()
        }
        # 解析关卡文件
        self.__parserlevelFile()

    '''开始游戏'''

    def start(self, screen):
        screen = pygame.display.set_mode((self.width + self.panel_width, self.height))
        # 背景图片
        background_img = pygame.image.load(self.other_image_paths.get('background'))
        # 定义精灵组
        player_tanks_group = pygame.sprite.Group()
        enemy_tanks_group = pygame.sprite.Group()
        player_bullets_group = pygame.sprite.Group()
        enemy_bullets_group = pygame.sprite.Group()
        foods_group = pygame.sprite.Group()
        # 定义敌方坦克生产事件
        generate_enemies_event = pygame.constants.USEREVENT
        pygame.time.set_timer(generate_enemies_event, 20000)
        # 我方大本营
        home = Home(position=self.home_position, imagepaths=self.home_image_paths)
        # 我方坦克
        tank_player1 = PlayerTank('player1', position=self.player_tank_positions[0],
                                  player_tank_image_paths=self.player_tank_image_paths,
                                  border_len=self.border_len, screensize=[self.width, self.height],
                                  bullet_image_paths=self.bullet_image_paths,
                                  protected_mask_path=self.other_image_paths.get('protect'),
                                  boom_image_path=self.other_image_paths.get('boom_static'))
        player_bullets_group.add(tank_player1)
        if self.is_dual_mode:
            tank_player2 = PlayerTank('player2', position=self.player_tank_positions[1],
                                      player_tank_image_paths=self.player_tank_image_paths,
                                      border_len=self.border_len, screensize=[self.width, self.height],
                                      bullet_image_paths=self.bullet_image_paths,
                                      protected_mask_path=self.other_image_paths.get('protect'),
                                      boom_image_path=self.other_image_paths.get('boom_static'))
            player_bullets_group.add(tank_player2)
        # 敌方坦克
        for position in self.enemy_tank_positions:
            enemy_tanks_group.add(EnemyTank(enemy_tank_image_paths=self.enemy_tank_image_paths,
                                            appear_image_path=self.other_image_paths.get('appear'),
                                            position=position, border_len=self.border_len,
                                            screensize=[self.width, self.height],
                                            bullet_image_paths=self.bullet_image_paths,
                                            food_image_paths=self.food_image_paths,
                                            boom_image_path=self.other_image_paths.get('boom_static')))
        # 游戏开始音乐
        self.sounds['start'].play()
        clock = pygame.time.Clock()
        # 该关卡通过与否的flags
        is_win = False
        is_running = True
        # 游戏主循环
        while is_running:
            screen.fill((0, 0, 0))
            screen.blit(background_img, (0, 0))
            # --用户事件捕捉
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # --地方坦克生成
                elif event.type == generate_enemies_event:
                    if self.max_enemy_num > len(enemy_tanks_group):
                        for position in self.enemy_tank_positions:
                            if len(enemy_tanks_group) == self.total_enemy_num:
                                break
                            enemy_tank = EnemyTank(enemy_tank_image_paths=self.enemy_tank_image_paths,
                                                   appear_image_path=self.other_image_paths.get('appear'),
                                                   position=position,
                                                   border_len=self.border_len, screensize=[self.width, self.height],
                                                   bullet_image_paths=self.bullet_image_paths,
                                                   food_image_paths=self.food_image_paths,
                                                   boom_image_path=self.other_image_paths.get('boom_static'))
                            if (not pygame.sprite.spritecollide(enemy_tank, enemy_tanks_group, False, None)) and (
                                    not pygame.sprite.spritecollide(enemy_tank, player_tanks_group, False, None)):
                                enemy_tanks_group.add(enemy_tank)
            # --用户按键
            key_pressed = pygame.key.get_pressed()

    '''显示游戏面板'''

    def __showGamePanel(self, screen, tank_player1, tank_player2=None):
        return

    # 玩家一操作提示
    # 玩家二操作提示
    # 玩家一状态提示
    # 玩家二状态提示
    # 当前关卡
    # 剩余敌人数量

    '''保护大本营'''

    def __pretectHome(self):
        return

    '''解析关卡文件'''

    def __parserlevelFile(self):
        return
