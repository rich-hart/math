from django.db import models
from django.contrib.postgres.fields import ArrayField

class Proof(models.Model):
    title = models.TextField()
    given = models.TextField()
    prove = models.TextField()
    diagram = models.FileField(null=True)
    plan = models.TextField()
    statements = ArrayField(models.TextField())
    reasons = ArrayField(models.TextField())

