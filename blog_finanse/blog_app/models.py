from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Roboczy'),
    ('published', 'Opublikowany'),
    )
    title = models.CharField(max_length = 250, default='tytuł')

    #slug do tworzenia URL
    slug = models.SlugField(max_length = 250, unique_for_date = 'publish')

    #autoryzacja na podstawie wbudowanego systemu User,
    author = models.ForeignKey(User, related_name = 'blog_posts', on_delete = models.CASCADE)

    #tresc wpisu
    body = models.TextField(default='tekst postu',)

    # data publikacji posta
    publish = models.DateTimeField(default=timezone.now)

    #data utworzenia posta
    created = models.DateTimeField(default=timezone.now)

    #status/stan posta  wybor z krotki STATUS_CHOICES
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')


    #sortowanie wynikow zapytania z bazy danych wzgledem daty publikacji
    class Meta:
        ordering = ('-publish',)

        #reprezentacja obiektu
        def __str__(self):
            return self.title
