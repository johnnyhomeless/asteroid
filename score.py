import pygame

class Score:
    def __init__(self):
        self.points = 0
        self.multiplier = 1
    
    def add_points(self, value):
        self.points += value * self.multiplier

    def reset(self):
        self.points = 0
        self.multiplier = 1