import pygame
import random
import sys

pygame.init()

# Define constants
WIDTH, HEIGHT = 640, 480
HANGMAN_IMGS = [pygame.image.load(f"./assets/hangman{i}.png") for i in range(7)]
HANGMAN_RECT = HANGMAN_IMGS[0].get_rect(center=(WIDTH / 2, HEIGHT / 2))
WORDS = ["python", "programming", "hangman", "game"]
FONT = pygame.font.Font(None, 48)


class Hangman:
    def __init__(self, word, max_misses=6):
        self.word = word
        self.guessed_letters = set()
        self.misses = 0
        self.max_misses = max_misses

    def guess_letter(self, letter):
        self.guessed_letters.add(letter.lower())
        if letter.lower() not in self.word:
            self.misses += 1

    def get_correct_guess(self):
        correct = [c if c in self.guessed_letters else "_" for c in self.word]
        return "".join(correct)

    def get_current_state(self):
        correct_guess = self.get_correct_guess()
        if "_" not in correct_guess:
            return "WIN"
        elif self.misses >= self.max_misses:
            return "LOSE"
        else:
            return "ONGOING"


class Game:
    def __init__(self):
        self.hangman = Hangman(random.choice(WORDS))
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hangman Game")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.unicode.isalpha():
                self.hangman.guess_letter(event.unicode)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(HANGMAN_IMGS[self.hangman.misses], HANGMAN_RECT)
        text = FONT.render(self.hangman.get_correct_guess(), True, (255, 255, 255))
        self.screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT * 3 / 4))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            if self.hangman.get_current_state() == "WIN":
                print("You win!")
                break
            elif self.hangman.get_current_state() == "LOSE":
                print("You lose!")
                break
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
