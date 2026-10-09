import pygame

from utils import Vector3, Camera
from projection import project_point_to_screen
from formulas import aspect_to_pos

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def draw_line(screen, pos1, pos2):

    point1 = ((pos1.x + 1) / 2 * SCREEN_WIDTH,
              (pos1.y + 1) / 2 * SCREEN_HEIGHT)

    point2 = ((pos2.x + 1) / 2 * SCREEN_WIDTH,
              (pos2.y + 1) / 2 * SCREEN_HEIGHT)

    pygame.draw.line(screen, "green", point1, point2, 3)
    pygame.draw.circle(screen, "blue", point1, 5)
    pygame.draw.circle(screen, "yellow", point2, 5)



def main():
    pygame.init()

    print("\n\n")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    camera = Camera(60, 10, (SCREEN_WIDTH, SCREEN_HEIGHT))
    point1 = Vector3(0, 2, 5)
    point2 = Vector3(2, 1, 5)

    aspect1 : tuple[float, float] = project_point_to_screen(point1, camera)
    aspect2 : tuple[float, float] = project_point_to_screen(point2, camera)

    print(aspect_to_pos(aspect1, ((SCREEN_WIDTH, SCREEN_HEIGHT))))

    pygame.draw.line(screen, "green",
        aspect_to_pos(aspect1, ((SCREEN_WIDTH, SCREEN_HEIGHT))),
        aspect_to_pos(aspect2, ((SCREEN_WIDTH, SCREEN_HEIGHT))),
        3)



    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        #running = False

    print("\nexited")

if __name__ == "__main__":
    main()
