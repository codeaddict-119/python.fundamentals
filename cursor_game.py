# Made with the help of A.I
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Cursor Creature")

clock = pygame.time.Clock()

# Creature settings
segment_count = 40
segment_length = 15
segments = [(WIDTH//2, HEIGHT//2) for _ in range(segment_count)]

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # First segment smoothly follows mouse
    head_x, head_y = segments[0]
    head_x += (mouse_x - head_x) * 0.2
    head_y += (mouse_y - head_y) * 0.2
    segments[0] = (head_x, head_y)

    # Other segments follow previous one
    for i in range(1, segment_count):
        prev_x, prev_y = segments[i - 1]
        curr_x, curr_y = segments[i]

        dx = prev_x - curr_x
        dy = prev_y - curr_y
        angle = math.atan2(dy, dx)

        new_x = prev_x - math.cos(angle) * segment_length
        new_y = prev_y - math.sin(angle) * segment_length
        segments[i] = (new_x, new_y)

    # Draw spine
    pygame.draw.lines(screen, (255, 255, 255), False, segments, 2)

    pygame.display.flip()

pygame.quit()