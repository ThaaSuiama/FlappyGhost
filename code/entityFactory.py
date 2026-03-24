#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import PLAYER_X, PLAYER_START_Y, WIN_WIDTH
from code.background import Background
from code.pipe import Pipe
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                return Player('Player', (PLAYER_X, PLAYER_START_Y))

            case 'PipeTop':
                return Pipe('PipeTop', position)

            case 'PipeBottom':
                return Pipe('PipeBottom', position)