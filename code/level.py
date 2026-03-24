#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.entityFactory import EntityFactory
from code.Const import COLOR_WHITE, WIN_HEIGHT, PIPE_GAP, WIN_WIDTH, PIPE_SPAWN_TIME
from code.entity import Entity
from code.pipe import Pipe


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        self.player = EntityFactory.get_entity('Player')
        self.entity_list.append(self.player)

        self.score = 0
        self.spawn_timer = 0
        self.timeout = 20000  #20 sec

        self.jump_sound = pygame.mixer.Sound('./asset/button_04.mp3')

    def create_pipe_pair(self):
        pipe_height = 500
        gap_y = random.randint(240, 400)

        pipe_top = EntityFactory.get_entity('PipeTop', (WIN_WIDTH, gap_y - pipe_height))
        pipe_bottom = EntityFactory.get_entity('PipeBottom', (WIN_WIDTH, gap_y + PIPE_GAP))

        self.entity_list.append(pipe_top)
        self.entity_list.append(pipe_bottom)

    def clean_entities(self):
        self.entity_list = [
            ent for ent in self.entity_list
            if not (isinstance(ent, Pipe) and ent.off_screen())
        ]

    def check_collision(self):
        if self.player.is_out():
            return True

        for ent in self.entity_list:
            if isinstance(ent, Pipe):
                if self.player.rect.colliderect(ent.rect):
                    return True
        return False

    def update_score(self):
        for ent in self.entity_list:
            if isinstance(ent, Pipe) and ent.name == 'PipeTop':
                if not ent.passed and ent.rect.centerx < self.player.rect.centerx:
                    ent.passed = True
                    self.score += 1
                    print(ent.name, ent.rect.centerx, self.player.rect.centerx, ent.passed)


    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60)
            self.spawn_timer += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self.player.jump()
                        self.jump_sound.play()

            if self.spawn_timer >= PIPE_SPAWN_TIME:
                self.create_pipe_pair()
                self.spawn_timer = 0

                self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()

            self.clean_entities()
            self.update_score()

            if self.check_collision():
                return 'GAME OVER'

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)


                    # printed text
            self.level_text(18, f'Score: {self.score}', COLOR_WHITE, (10, 5))
            self.level_text(14, f'{self.name}', COLOR_WHITE, (10, 30))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
