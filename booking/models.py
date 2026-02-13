

# Create your models here.
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='games/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    player_name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.player_name} - {self.game.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


