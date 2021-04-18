import pygame

pygame.init()
pygame.font.init()


WIN_WIDTH, WIN_HEIGHT = 1920, 1080
GRID_X, GRID_Y = 60, 60

# Game IMG's
path_grass = pygame.transform.scale(pygame.image.load("./assets/path_grassland.png"), (60, 60)) # can fit 48 on x, 27 on y
knight_img = pygame.transform.scale(pygame.image.load("./assets/knight_idle.png"), (19, 38))


def knight():
    playerx = 600
    playery = 300

    WIN.blit(knight_img, (playerx, playery))


def draw_grid():
    for x in range(WIN_WIDTH):
        for y in range(WIN_HEIGHT):
            grid_block = pygame.Rect(x*GRID_X, y*GRID_Y, GRID_X, GRID_Y)
            pygame.draw.rect(WIN, (200, 200, 200), grid_block, 1)

def main():
    global WIN
    # Create window
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    icon = pygame.image.load("./assets/path_grassland.png")
    pygame.display.set_caption("Dark Loop")
    pygame.display.set_icon(icon)

    # Draws grid guide
    draw_grid()
    
    run = True
    while run:
        # Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Background filler
        knight()
        pygame.display.update()

main()