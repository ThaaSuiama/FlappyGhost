#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT, JUMP_STRENGTH, GRAVITY
from code.entity import Entity



class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf = pygame.transform.flip(self.surf, True, False)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.vel_y = 0

    def jump(self):
        self.vel_y = JUMP_STRENGTH

    def move(self):
        self.vel_y += GRAVITY
        self.rect.y += int(self.vel_y)

        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

    def is_out(self):
        return self.rect.bottom >= WIN_HEIGHT
