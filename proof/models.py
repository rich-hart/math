from django.db import models
from django.contrib.postgres.fields import ArrayField

class Theorem(models.Model):
    statement = models.TextField()
    proof = models.ForeignKey('Proof')

class Axiom(models.Model):
    statement = models.TextField()

class Definition(models.Model):
    term = models.TextField()
    statement = models.TextField()

class Proof(models.Model):
    title = models.TextField()
    given = models.TextField()
    prove = models.TextField()
    diagram = models.FileField(null=True)
    plan = models.TextField()
    statements = ArrayField(models.TextField())
    reasons = ArrayField(models.TextField())

