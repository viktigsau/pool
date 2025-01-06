import pygame
from stuff import *
import speed
import time
from threading import Thread


class Ball:
    def __init__(self, pos: Vec2, r: int, flags: dict={}):
        self.pos = pos
        self.r = r
        self.flags = flags
    
    def get_colition(self, other):
        collition_vector = (self.pos - other.pos).norm()
        colliding = self.pos.dist(other.pos) <= self.r + other.r # determen if the to balls colide or not
        # colliding will be true if the distance between the to balld is less the the sum of the radia        

        return (collition_vector, colliding)
    
    def update(self, balls):
        if "static" in self.flags and self.flags["static"]:
            self.pos = Vec2(*pygame.mouse.get_pos()) - Vec2(*pygame.display.get_window_size()) / 2

        for ball in balls:
            self.collide(ball)
    
    def collide(self, other):
        direction, colliding = self.get_colition(other)
        if not colliding:
            return

        overlap = abs(self.pos.dist(other.pos) - self.r - other.r)

        if "static" in other.flags and other.flags["static"]:
            other.pos += direction * 0.5 * overlap

        if "static" in self.flags and self.flags["static"]:
            self.pos -= direction * 0.5 * overlap

class Pool:
    def __init__(self, window: pygame.surface.SurfaceType):
        self.balls: list[Ball] = [
            Ball(Vec2(0, 0), 50),
            Ball(Vec2(50 ,50), 50, flags={"static":True})
        ]

        self.window = window

        self.update_thread = Thread(target=self.start_update_cycle, args=(25,))
        self.update_thread.start()

    def start_update_cycle(self, ups: int):
        delay = 1/ups
        while True:
            speed.thread(self.balls, lambda ball: ball.update(self.balls), use_threads=True)
            time.sleep(delay)

    def render(self):
        offset = Vec2(*self.window.get_size()) / 2
        for ball in self.balls:
            pygame.draw.circle(self.window, (255, 0, 0), (ball.pos + offset).tuple(), ball.r)
        