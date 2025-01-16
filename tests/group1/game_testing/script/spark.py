import math
import pygame

class Spark:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    def render(self, surface, offset=[0,0]):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle+math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[1]),
        ]
        pygame.draw.polygon(surface, (255, 255, 255), render_points)

class Flame:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    def render(self, surface, offset=[0,0]):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle+math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[1]),
        ]
        pygame.draw.polygon(surface, (255, 0, 0), render_points)


class Gold_Flame:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    def render(self, surface, offset=[0,0]):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle+math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[1]),
        ]
        pygame.draw.polygon(surface, (255, 255, 0), render_points)

class Ice_Flame:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    def render(self, surface, offset=[0,0]):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle+math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[1]),
        ]
        pygame.draw.polygon(surface, (0, 255, 255), render_points)

class Dark_Blue_Flame:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    def render(self, surface, offset=[0,0]):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle+math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[1]),
        ]
        pygame.draw.polygon(surface, (0, 0, 139), render_points)

class Flexible_Spark:
    def __init__(self, pos, angle, speed, color_code):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
        self.color_code = color_code
    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    def render(self, surface, offset=[0,0]):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle+math.pi*0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle+math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle+math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle-math.pi*0.5) * self.speed * 0.5 - offset[1]),
        ]
        pygame.draw.polygon(surface, self.color_code, render_points)
