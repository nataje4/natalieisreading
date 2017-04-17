from django.db import models

# Create your models here.
class Post(models.Model): 
	pub_date=models.DateTimeField()
	general_notes=models.TextField(null=True, blank=True)
	

	def __str__(self): 
		return (self.general_notes)

class Blurb(models.Model): 
	pub_date = models.DateTimeField()
	text = models.TextField(null=True)
	book = models.ForeignKey('Book')
	post = models.ForeignKey('Post')
	reading = models.BooleanField(default=False)

	def __str__(self): 
		return (self.text)

class Book(models.Model):
	title = models.CharField(max_length=300)
	author = models.ForeignKey('Author')
	general_notes=models.TextField(null=True, blank=True)

	def __str__(self): 
		return self.title

class Author(models.Model): 
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	general_notes=models.TextField(null=True, blank=True)

	def __str__(self): 
		return (self.first_name +" "+ self.last_name)