from django.db import models

# Create your models here.
class Game(models.Model,):

    class Status(models.TextChoices):
        IN_PROGRESS = 'InProgress', 'In Progress'
        LOST = 'Lost', 'Lost'
        WON = 'Won', 'Won'

    word = models.CharField(max_length=100)
    guessed_letters = models.CharField(max_length=30, blank=True)
    incorrect_guesses = models.IntegerField(default=0)
    max_incorrect_guesses = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.IN_PROGRESS)

    def get_display_word(self):
        return ''.join([letter if letter.lower() in self.guessed_letters else '_' for letter in self.word])

    def get_incorrect_guesses_left(self):
        return self.max_incorrect_guesses - self.incorrect_guesses

    def check_game_status(self):
        if self.get_incorrect_guesses_left() <= 0:
            self.status = self.Status.LOST
        elif '_' not in self.get_display_word():
            self.status = self.Status.WON
        else:
            self.status = self.Status.IN_PROGRESS
        self.save()
