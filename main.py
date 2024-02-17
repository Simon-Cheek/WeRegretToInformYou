import pygame

pygame.init()


screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True


# game CYCLE / LOOP
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # RENDER THE GAME HERE

    pygame.display.flip()

    clock.tick(60)

pygame.quit()