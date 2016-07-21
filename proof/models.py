from django.db import models
from django.contrib.postgres.fields import ArrayField


class Axiom(models.Model):
    name = models.TextField()
    statement = models.TextField()

class Definition(models.Model):
    name = models.TextField()
    statement = models.TextField()

# Lemmas? Corrlaries?

# argument has three types (list, graph, paragraph).
# a use case should be a user can do it these there ways
 

class Theorem(models.Model): 
    name = models.TextField()
    statement = models.TextField()
    given = models.TextField()
    prove = models.TextField()
    diagram = models.FileField(null=True)
    plan = models.TextField() # change with note. 
    # statements and reseasons should be replaced with argument.
    statements = ArrayField(models.TextField())
    reasons = ArrayField(models.TextField())

