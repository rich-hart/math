from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.conf import settings


# Make a temp book model for file uploads.  Make
# make staff only and not that this will be depricated.

#class Citation(models.Model):
#    bibtex

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    definitions = models.FileField(upload_to=settings.MEDIA_ROOT)
    axioms = models.FileField(upload_to=settings.MEDIA_ROOT)
    theorems = models.FileField(upload_to=settings.MEDIA_ROOT)
    proofs = models.FileField(upload_to=settings.MEDIA_ROOT,null=True)
    citation = models.FileField(upload_to=settings.MEDIA_ROOT)


class Statement(models.Model):
    LABEL_CHOICES = (
       ('DE', 'Definition'),
       ('AX', 'Axiom'),
#       ('LE', 'Lemma'),
       ('TH', 'Theorem'),
#       ('CO', 'Corollary'),
    )
    label = models.CharField(
        max_length=2,
        choices=LABEL_CHOICES,
        default=None,
        null = True,
    )
    name = models.CharField(max_length=255)
    statement = models.CharField(max_length=255)
    citation = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

class Argument(models.Model):
    statement = models.ForeignKey(Statement)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    given = models.CharField(max_length=255)
    prove = models.CharField(max_length=255)
    diagram = models.FileField(upload_to=settings.MEDIA_ROOT,
                               null=True,)
    note = models.TextField(null=True)
    paragraph = models.TextField(null=True)
    statements = ArrayField(models.CharField(max_length=255),
                                             null=True)
    reasons = ArrayField(models.CharField(max_length=255),
                                          null=True)
    # graph = link lists. 

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
    diagram = models.FileField(upload_to=settings.MEDIA_ROOT,
                               null=True,)
    plan = models.TextField() # change with note. 
    # statements and reseasons should be replaced with argument.
    statements = ArrayField(models.TextField())
    reasons = ArrayField(models.TextField())

