# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Review(models.Model):
	author = models.CharField(max_length=50)
	rating = models.DecimalField(max_digits=2, decimal_places=1)
	reviewText = models.TextField()
	date = models.DateTimeField(default=timezone.now())	

	def __str__(self):
		return "{} gave {} stars".format(self.author, self.rating)

class Order(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.IntegerField()
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50, default="Yerevan")
	bedroomNumber = models.IntegerField(
		validators=[
			MinValueValidator(1),
			MaxValueValidator(6)
		]
	)
	bathroomNumber = models.IntegerField(
		validators=[
			MinValueValidator(1),
			MaxValueValidator(6)
		]
	)
	extras = models.CharField(max_length=50, blank=True)
	dateOfService = models.DateTimeField()
	cost = models.CharField(max_length=20, default='')
	#howOften = models.CharField(max_length=100)

	def __str__(self):
		return "{} {}".format(self.firstName, self.lastName)

class Contact(models.Model):
	contactReason = models.CharField(max_length=100)
	text = models.TextField()
	email = models.EmailField()

	def __str__(self):
		return self.email