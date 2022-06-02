from math import fabs
from turtle import title
from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',
        max_length=254,
    )
    description = models.TextField(
        unique= False,
    )
    is_completed = models.BooleanField(
        default=False,
    )
