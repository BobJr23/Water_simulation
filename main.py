import pygame, random, math

# INITIALIZE
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics!")
white = (255, 255, 255)
green = (50, 168, 82)
black = (0, 0, 0)
red = (200, 0, 0)
grey = (189, 174, 174)

blue = (55, 112, 153)
brown = (133, 64, 65)
FPS = 120
FONT = pygame.font.Font(None, 40)


class water:
    def __init__(self, x, y, vel, acc):
        self.x = x
        self.y = y
        self.acc = acc
        self.vel = vel


# GAME LOOP
def play():
    gravity = 10
    mouse_y = (0, 300)
    water_drops = []
    hole_coords = (0, 500)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        # DRAW WINDOW

        WIN.fill((189, 174, 174))
        # tube
        pygame.draw.rect(WIN, black, (20, 20, 220, 540))
        # ground
        pygame.draw.rect(WIN, black, (20, 550, 780, 10))
        # water
        pygame.draw.rect(WIN, blue, (30, mouse_y[1], 200, 550 - mouse_y[1]))
        hole = pygame.draw.rect(WIN, brown, (210, hole_coords[1] - 20, 40, 40))
        difference = (hole_coords[1] - mouse_y[1]) / 400
        try:
            vi = round(math.sqrt(2 * gravity * difference * 30), 3)
        except:
            vi = 0
        # MATH
        if difference <= 0:
            difference = 0

        for x in range(1):
            water_drops.append(
                water(
                    hole.x + random.randint(-5, 5),
                    hole.y + random.randint(-5, 5),
                    math.sqrt(difference * 2 * gravity),
                    0,
                )
            )
        for drop in water_drops:
            drop.acc -= 1
            drop.y -= drop.acc / 10
            drop.x += drop.vel
            if drop.y > 550:
                water_drops.remove(drop)
                del drop
            else:
                pygame.draw.circle(WIN, blue, (drop.x + 10, drop.y + 10), 4)
        pygame.display.update()


if __name__ == "__main__":
    play()
