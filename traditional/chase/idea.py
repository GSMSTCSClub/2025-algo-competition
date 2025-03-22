"""
A simple pygame simulation of Pac Man and the ghost.

Controls:
- WASD for the ghost (white square)
- Arrow keys for pac man (yellow square)
- The number on the ghost is the speed of it
    - Increase/decrease speed with =/-
- The number on pac man is how many unique cells it visited
    - Clear visited cells by pressing SPACE

Pac man to move, how many tiles can it reach?
2...5
ABCDE
.FGHI
..JKL
...MN
....O
A, B, C, D, E = 1, 5, 6, 6, 6
F, G, H, I    = 5, 6, 6, 6
J, K, L       = 6, 6, 7
M, N          = 7, 7
O             = 7

"""


import pygame
import sys


pygame.init()


screen = pygame.display.set_mode([500, 500])
BLOCK_SIZE = 25
ghost_pos = [0, 0]
speed = 2
ghost_motion = {
    pygame.K_a: [-BLOCK_SIZE, 0],
    pygame.K_d: [BLOCK_SIZE, 0],
    pygame.K_w: [0, -BLOCK_SIZE],
    pygame.K_s: [0, BLOCK_SIZE],
}
ghost_time = 0
pacman_pos = [BLOCK_SIZE, BLOCK_SIZE]
pacman_motion = {
    pygame.K_LEFT: [-BLOCK_SIZE, 0],
    pygame.K_RIGHT: [BLOCK_SIZE, 0],
    pygame.K_UP: [0, -BLOCK_SIZE],
    pygame.K_DOWN: [0, BLOCK_SIZE],
}
pacman_time = 0
visited = set()
visited.add(tuple(pacman_pos))
FPS = 60
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 25)



def main():
    global pacman_pos, ghost_pos, speed, visited
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in ghost_motion:
                    ghost_pos = ghost_pos[0] + speed * ghost_motion[event.key][0], ghost_pos[1] + speed * ghost_motion[event.key][1]
                if event.key in pacman_motion:
                    pacman_pos = pacman_pos[0] + pacman_motion[event.key][0], pacman_pos[1] + pacman_motion[event.key][1]
                    visited.add(tuple(pacman_pos))
                if event.key == pygame.K_SPACE:
                    visited = set()
                    visited.add(tuple(pacman_pos))
                if event.key == pygame.K_EQUALS:
                    speed += 1
                if event.key == pygame.K_MINUS:
                    speed -= 1
        draw()


def draw_grid(start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x + 1, BLOCK_SIZE): 
        pygame.draw.line(screen, "black", [x, start_y], [x, end_y])
    for y in range(start_y, end_y + 1, BLOCK_SIZE): 
        pygame.draw.line(screen, "black", [start_x, y], [end_x, y])


def draw():
    screen.fill("light gray")
    for pos in visited:
        rect = pygame.rect.Rect(pos, [BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(screen, "black", rect)
    # pac man
    pac_rect = pygame.rect.Rect(pacman_pos, [BLOCK_SIZE, BLOCK_SIZE])
    pygame.draw.rect(screen, "yellow", pac_rect)

    # ghost
    ghost_rect = pygame.rect.Rect(ghost_pos, [BLOCK_SIZE, BLOCK_SIZE])
    pygame.draw.rect(screen, "white", ghost_rect)

    # text
    surf = FONT.render(f"{speed}", False, 'black')
    screen.blit(surf, (ghost_rect.centerx - surf.get_width() / 2, ghost_rect.centery - surf.get_height() / 2))

    surf = FONT.render(f"{len(visited)}", False, 'black')
    screen.blit(surf, (pac_rect.centerx - surf.get_width() / 2, pac_rect.centery - surf.get_height() / 2))

    # grid
    draw_grid(0, 0, 500, 500)
    pygame.display.flip()
    CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
