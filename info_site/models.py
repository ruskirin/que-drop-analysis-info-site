from django.db import models


class Article(models.Model):
    pass


class Contributors(models.Model):
    POSITIONS = (
        ('LR', 'Lead Researcher'),
        ('SA', 'Student Assistant'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    school = models.CharField(max_length=100)
    bio = models.CharField(
        max_length=500,
        blank=True,
    )

    is_prof = models.BooleanField(default=False)
    position = models.CharField(
        max_length=2,
        choices=POSITIONS,
    )

    articles = models.ManyToManyField(
        Article
    )

    def __str__(self):
        return f'{"Dr. " if self.is_prof else ""}{self.first_name} {self.last_name}'

    class Meta:
        pass