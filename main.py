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
            if pygame.mouse.get_pressed()[0]:
                if slider.collidepoint(pygame.mouse.get_pos()):
                    mouse_y = pygame.mouse.get_pos()
                elif hole.collidepoint(pygame.mouse.get_pos()):
                    hole_coords = pygame.mouse.get_pos()

        # DRAW WINDOW

        WIN.fill((189, 174, 174))
        # tube
        pygame.draw.rect(WIN, black, (20, 20, 220, 540))
        # ground
        pygame.draw.rect(WIN, black, (20, 550, 780, 10))
        # water
        pygame.draw.rect(WIN, blue, (30, mouse_y[1], 200, 550 - mouse_y[1]))
        # slider
        slider = pygame.draw.rect(WIN, brown, (110, mouse_y[1] - 20, 50, 40))
        hole = pygame.draw.rect(WIN, brown, (210, hole_coords[1] - 20, 40, 40))
        difference = (hole_coords[1] - mouse_y[1]) / 400
        hole_height = (550 - hole_coords[1]) / 400 * 30
        try:
            vi = round(math.sqrt(2 * gravity * difference * 30), 3)
        except:
            vi = 0
        # MATH
        time_ = math.sqrt(2 * hole_height / 100 / gravity)
        displacement = round(vi * time_ * 10, 3)
        if difference <= 0:
            difference = 0
        WIN.blit(
            FONT.render(
                f"Displacement:",
                False,
                (0, 0, 0),
            ),
            (480, 300),
        )
        WIN.blit(
            FONT.render(
                f"{displacement} cm ({round(displacement/100,3)} m)",
                False,
                (0, 0, 0),
            ),
            (480, 325),
        )
        WIN.blit(
            FONT.render(
                f"Height of hole:",
                False,
                (0, 0, 0),
            ),
            (480, 200),
        )
        WIN.blit(
            FONT.render(
                f"{round(hole_height,3)} cm ({round(hole_height/100,3)} m)",
                False,
                (0, 0, 0),
            ),
            (480, 225),
        )
        WIN.blit(
            FONT.render(
                f"Height above hole:",
                False,
                (0, 0, 0),
            ),
            (480, 0),
        )
        WIN.blit(
            FONT.render(
                f"{round(difference * 30,3)} cm ({round(difference * 30/100,3)} m)",
                False,
                (0, 0, 0),
            ),
            (480, 25),
        )
        WIN.blit(
            FONT.render(
                f"Velocity coming out:",
                False,
                (0, 0, 0),
            ),
            (480, 100),
        )
        WIN.blit(
            FONT.render(
                f"{vi} cm/s ({round(vi/100,3)}) m/s)",
                False,
                (0, 0, 0),
            ),
            (480, 125),
        )

        # # DO MATH
        # WIN.blit(
        #     FONT.render(
        #         "Distance travelled: " + str(difference * 30), False, (0, 0, 0)
        #     ),
        #     (450, 100),
        # )

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
        # factor of 400
        pygame.display.update()


if __name__ == "__main__":
    play()
