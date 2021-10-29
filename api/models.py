from django.db import models


class LibrarySet(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
