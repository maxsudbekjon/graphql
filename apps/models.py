from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE


# Create your models here.
class Author(Model):
    name = CharField(max_length=100)
class Book(Model):
    title=CharField(max_length=100)
    author=ForeignKey('apps.Author',CASCADE,related_name='books')
