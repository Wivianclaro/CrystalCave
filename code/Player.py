#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.AnimatedEntity import AnimatedEntity
from code.Const import PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_WIDTH

class Player(AnimatedEntity):
    def __init__(self, name: str, position: tuple):
        # Cada frame tem 128x128, e a sprite tem 7 frames
        super().__init__(name, position, frame_size=(128, 128), num_frames=7)
        self.speed = 4

    def move(self):
        keys = pygame.key.get_pressed()

        # Move só para os lados, respeitando os limites da tela
        if keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed

        super().move()  # Atualiza o frame da animação







# from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
#     PLAYER_KEY_RIGHT
# from code.Entity import Entity
#
#
# class Player(Entity):
#     def __init__(self, name: str, position: tuple):
#         super().__init__(name, position)
#
#     def move(self, ):
#         pressed_key = pygame.key.get_pressed()
#         if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
#             self.rect.centery -= ENTITY_SPEED[self.name]
#         if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
#             self.rect.centery += ENTITY_SPEED[self.name]
#         if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
#             self.rect.centerx -= ENTITY_SPEED[self.name]
#         if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
#             self.rect.centerx += ENTITY_SPEED[self.name]
#         pass
