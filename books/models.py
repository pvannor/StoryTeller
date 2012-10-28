"""
Books : Models

Representation of each story written by the community.

Book - Entry point into a story
Chapter - A story segment belonging to a single book, each chapter follows one parent chapter. 
	Note: a chapter can have many children resulting in a branching story

todo: Flesh out ownership, privacy, rating, statistics, etc

"""
from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	tagline = models.CharField(max_length=200)

	def __unicode__(self):
	        return self.title

class Chapter(models.Model):
	book = models.ForeignKey(Book)	
	parentChapter = models.ForeignKey("self", blank=True, null=True)
	title = models.CharField(max_length=200)
	story = models.TextField()

	def __unicode__(self):
	        return self.book.title + ": " + self.title