from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Sentiment(models.Model):
    sentence = models.TextField(max_length=300, help_text='Ingresa la frase que exprese tu emoción', null=False, blank=False)

    EMOTION_STATUS = (
        (0, 'Negativo'),
        (1, 'Positivo'),        
    )

    emotion = models.IntegerField(
        null = False, 
        blank = False,
        max_length = 1,
        choices = EMOTION_STATUS,
        help_text = 'Sentiment availability'
    )

    class Meta:
        ordering = ['emotion']

    def get_absolute_url(self):
        """Returns the url to access a particular sentiment instance."""
        return reverse('sentiment-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.sentence}, {self.emotion}'
