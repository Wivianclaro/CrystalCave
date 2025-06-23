#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity

class AnimatedEntity(Entity):
    def __init__(self, name: str, position: tuple, frame_size: tuple, num_frames: int, frame_delay: int = 6):
        self.frames = []
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = frame_delay

        sprite_sheet = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        print(f"Carregando sprite sheet: ./asset/{name}.png")
        print(f"Tamanho da imagem: {sprite_sheet.get_width()}x{sprite_sheet.get_height()}")

        frame_width, frame_height = frame_size
        for i in range(num_frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)

        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(topleft=position)
        self.name = name
        self.speed = 0

    def move(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.surf = self.frames[self.current_frame]

