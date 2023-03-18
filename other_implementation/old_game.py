import pygame
import random
import sys

# Set up game window
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load hangman graphics
hangman_imgs = [pygame.image.load(f"./assets/hangman{i}.png") for i in range(7)]
hangman_rect = hangman_imgs[0].get_rect(center=(WIDTH / 2, HEIGHT / 2))


# Define game logic functions
def get_word():
    # Select a random word from a list
    words = ["python", "programming", "hangman", "game"]
    return random.choice(words)


def check_guess(word, guessed_letters):
    # Check if guessed letters are in word
    correct = [c if c in guessed_letters else "_" for c in word]
    return "".join(correct)


# Set up game state
word = get_word()
guessed_letters = set()
misses = 0

# Create main game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.unicode.isalpha():
            # Process letter input
            letter = event.unicode.lower()
            guessed_letters.add(letter)
            if letter not in word:
                misses += 1

    # Update game state
    correct_guess = check_guess(word, guessed_letters)
    if "_" not in correct_guess:
        # Game won
        print("You win!")
        break
    elif misses == len(hangman_imgs):
        # Game lost
        print("You lose!")
        break

    # Draw screen
    screen.fill((0, 0, 0))
    screen.blit(hangman_imgs[misses], hangman_rect)
    font = pygame.font.Font(None, 48)
    text = font.render(correct_guess, True, (255, 255, 255))
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT * 3 / 4))
    pygame.display.flip()
    clock.tick(60)
