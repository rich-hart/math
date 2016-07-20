from django.db import models
from django.contrib.postgres.fields import ArrayField

class Argument(models.Model):
    statements = ArrayField(models.TextField())
    reasons = ArrayField(models.TextField())

