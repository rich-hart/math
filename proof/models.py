from django.db import models
from django.contrib.postgres.fields import ArrayField


class Axiom(models.Model):
    name = models.TextField()
    statement = models.TextField()

class Definition(models.Model):
    name = models.TextField()
    statement = models.TextField()

class Theorem(models.Model):
    name = models.TextField()
    statement = models.TextField()
    given = models.TextField()
    prove = models.TextField()
    diagram = models.FileField(null=True)
    plan = models.TextField()
    statements = ArrayField(models.TextField())
    reasons = ArrayField(models.TextField())

