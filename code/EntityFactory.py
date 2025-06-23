#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1Idle':
                return Player('Player1Idle', ((WIN_WIDTH // 5) - 128, WIN_HEIGHT - 128))  # canto inferior esquerdo
            case 'Player2Idle':
                return Player('Player2Idle', ((WIN_WIDTH // 6) - 128, WIN_HEIGHT - 128))  # mais perto do Player1
            case 'Big_bloated_idle':
                return Enemy('Big_bloated_idle', (WIN_WIDTH +10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Centipede_idle':
                return Enemy('Centipede_idle', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        return None