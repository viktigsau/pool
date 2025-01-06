from math import sqrt
import pygame
import speed


class Vec2:
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Vec2(self.x-other.x, self.y-other.y)

    def __mul__(self, amount: int | float):
        return Vec2(self.x*amount, self.y*amount)
    
    def __truediv__(self, amount: int | float):
        return Vec2(self.x/amount, self.y/amount)

    def norm(self):
        try:
            return self / max(self.x, self.y)
        except ZeroDivisionError:
            return Vec2(1, 0)
    
    def dist(self, other):
        return abs((self - other).__len__())
    
    def __len__(self):
        return sqrt(self.x + self.y)
    
    def tuple(self):
        return (self.x, self.y)
    
    def render(self, origin, window, color=(0, 255, 0)):
        offset = Vec2(*window.get_size()) / 2
        pygame.draw.line(window, color, (self + offset).tuple(), (origin + offset).tuple())