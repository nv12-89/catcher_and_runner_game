import pgzrun
import random

# Game Window
WIDTH = 800
HEIGHT = 600

# Load characters
positive = Actor("positive_alien")  # Replace with an actual image
negative = Actor("negative_alien")  # Replace with an actual image

# Initial positions
positive.pos = (WIDTH // 2, HEIGHT // 2)
negative.pos = (WIDTH // 3, HEIGHT // 3)

# Game Variables
score = 0
message = "Click on the right character!"

def draw():
    screen.clear()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    screen.draw.text(message, (10, 50), fontsize=25, color="yellow")
    positive.draw()
    negative.draw()

def on_mouse_down(pos):
    global score, message

    if positive.collidepoint(pos):
        score += 1
        message = "You hit the correct one!"
        print("Hit Positive!")  # Debugging log
    elif negative.collidepoint(pos):
        score -= 1
        message = "Oops! Wrong one!"
        print("Hit Negative!")  # Debugging log
    else:
        message = "You missed!"

    # Move characters to new random positions
    positive.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    negative.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

pgzrun.go()
