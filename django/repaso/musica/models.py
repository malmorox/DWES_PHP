from django.db import models


class Musica(models.Model):
    nombre = models.CharField(max_length=2,unique=True)
    TIPOS_MUSICA = [
        ('rock', 'ROCK'),
        ('pop', 'POP'),
        ('jazz', 'JAZZ'),
        ('electronica', 'ELECTRÓNICA'),
        ('clasica', 'CLÁSICA'),
    ]
    fichero = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.nombre