#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMEGE, ENTITY_SCORE

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() #<- trata a imagem png de forma mais otimizada.
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.helth = ENTITY_HEALTH[self.name]
        self.damege = ENTITY_DAMEGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'none'
    
    @abstractmethod
    def move(self, ):
        pass
