'''
Function:
    子弹类
'''
import pygame

'''子弹'''


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_image_paths, screensize, direction, position, border_len, is_stronger=False, speed=8,
                 **kwargs):

    def move(self):
        return False
