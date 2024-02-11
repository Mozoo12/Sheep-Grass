import pygame
import sys
import random

grass_list = []
sheep_list = []


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Sheep&Grass")
        self.init()

    @classmethod
    def event(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def init(self):

        x = 0
        y = 0

        pygame.draw.rect(self.screen, (34, 139, 34), pygame.Rect(x, y, 10, 10))
        for k in range(20):
            sheep_list.append(Sheep())

        for n in range(80):
            grass_list.append([])
            for c in range(120):
                grass_list[-1].append(Grass(x, y))
                x += 10
            x = 0
            y += 10

    def update(self):
        for a in grass_list:
            for f in a:
                f.life()
                pygame.draw.rect(self.screen, f.colour, pygame.Rect(f.x, f.y, 10, 10))
        for i in sheep_list:
            i.life()
            pygame.draw.circle(surface=self.screen, color=(0, 0, 0), center=(i.x, i.y), radius=5)

    def run(self):
        while True:
            self.event()
            self.screen.fill((225, 255, 255))
            self.update()
            pygame.display.update()


class Sheep:
    def __init__(self):
        self.energy = 80
        self.x = random.randint(0, 1200)
        self.y = random.randint(0, 800)

    def walk(self):
        self.x += random.choice([-1, -2, 0, 1, 2])
        self.y += random.choice([-1, -2, 0, 1, 2])
        self.energy -= 1

    def eat(self):
        patch_x = int(int(self.x) / 10 + 1)
        patch_y = int(int(self.y) / 10 + 1)

        if patch_y > 80 or patch_x > 120:
            patch_y = 80
            patch_x = 120

        if grass_list[patch_y - 1][patch_x - 1].eatable:
            self.energy += 20
            grass_list[patch_y - 1][patch_x - 1].eatable = False

    def reproduction(self):
        if self.energy >= 80:
            sheep_list.append(Sheep())
            self.energy = 5

    def die(self):
        if self.energy == 0:
            sheep_list.remove(self)

    def life(self):
        self.walk()
        self.eat()
        self.reproduction()
        self.die()


class Grass:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.eatable = True
        self.colour = (34, 139, 34)
        self.energy = 0

    def eaten(self):
        if not self.eatable:
            self.colour = (160, 82, 45)

    def new(self):
        if random.randint(0, 100) == 6:
            self.eatable = True
            self.colour = (34, 139, 34)

    def life(self):
        self.eaten()
        self.new()


if __name__ == "__main__":
    game = Game()
    game.run()
