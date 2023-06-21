import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Shooter")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Alien properties
alien_width = 50
alien_height = 50
alien_x = random.randint(0, screen_width - alien_width)
alien_y = 50
alien_speed = 3

# Bullet properties
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = player_y
bullet_speed = 5
bullet_state = "ready"

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + player_width // 2 - bullet_width // 2
                    bullet_state = "fire"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Update bullet position
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"
            bullet_y = player_y

    # Check for collision
    if bullet_y < alien_y + alien_height and bullet_state == "fire":
        if bullet_x > alien_x and bullet_x < alien_x + alien_width:
            bullet_state = "ready"
            bullet_y = player_y
            alien_x = random.randint(0, screen_width - alien_width)
            alien_y = 50

    # Update alien position
    alien_x += alien_speed
    if alien_x >= screen_width - alien_width or alien_x <= 0:
        alien_speed *= -1

    # Clear the screen
    screen.fill(black)

    # Draw the player
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    # Draw the bullet
    if bullet_state == "fire":
        pygame.draw.rect(screen, white, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Draw the alien
    pygame.draw.rect(screen, white, (alien_x, alien_y, alien_width, alien_height))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
