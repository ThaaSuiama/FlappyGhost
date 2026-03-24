#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.Const import ENTITY_SPEED


class Pipe(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (80, 500))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.passed = False

    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]

    def off_screen(self):
        return self.rect.right < 0