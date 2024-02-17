import pygame
import Job_Listing

pygame.init()


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("We Regret to Inform You")
clock = pygame.time.Clock()
running = True

# starting location of rectangle
x = 100
y = 100
height = 100
width = 200
vel = 3


# game CYCLE / LOOP
while running:
    # sets each loop to run every 1/10 of a second
    pygame.time.delay(10)

    # starts the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    # find keys that are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_ESCAPE]:
        running = False


# after the main loop
pygame.quit()
