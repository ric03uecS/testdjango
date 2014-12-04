from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date = models.DateTimeField('date publishedddd')


class Choice(models.Model):
    question = models.ForeignKey(Post)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
