#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Crystal import Crystal
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1Idle':
                return Player('Player1Idle', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2Idle':
                return Player('Player2Idle', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Crystal':
                return Crystal('Crystal', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        return None
