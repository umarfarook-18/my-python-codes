import pygame
import random
import math

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Igris Shadow Animation")

clock = pygame.time.Clock()

# Load image
igris = pygame.image.load("igris.png")
igris = pygame.transform.scale(igris, (300, 400))

# Particle class
class Particle:
    def __init__(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(150, 450)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.size)

particles = [Particle() for _ in range(100)]

# Glow effect
def draw_glow(x, y, radius):
    for i in range(radius, 0, -10):
        alpha = int(255 * (i / radius))
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(surface, (255, 0, 0, alpha), (x, y), i)
        screen.blit(surface, (0, 0))

# Main loop
running = True
t = 0

while running:
    screen.fill((10, 10, 20))  # dark background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Floating effect (up-down motion)
    y_offset = int(10 * math.sin(t))

    # Glow behind Igris
    draw_glow(WIDTH//2, HEIGHT//2, 200)

    # Draw particles
    for p in particles:
        p.move()
        p.draw()

    # Draw Igris
    screen.blit(igris, (WIDTH//2 - 150, HEIGHT//2 - 200 + y_offset))

    pygame.display.update()
    clock.tick(60)
    t += 0.05

pygame.quit()
