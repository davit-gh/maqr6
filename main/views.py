# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import ReviewForm, OrderForm, ContactForm
from models import Review
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def index(request):
	reviews = Review.objects.all()
	context = {
		'reviews': reviews,
		'pageHeader': {
			'title': 'Maqr6',
			'strapline': 'Shine like your house will!'
		}
	}
	return render(request, 'main/index.html', context)

def processForm(request, FormClass, message, redirectViewName, tplName, strapline):
	if request.method == 'POST':
		sampleForm = FormClass(request.POST)
		if sampleForm.is_valid():
			sampleForm.save()
			messages.success(request, message)
			return redirect(reverse(redirectViewName))
	else:
		sampleForm = FormClass()

	context = {
		'form': sampleForm,
		'pageHeader': {
			'title': 'Maqr6',
			'strapline': strapline
		}
	}

	return render(request, tplName, context)

def rate(request):
	
   	return processForm(
   					request,
   					ReviewForm,
   					"Your review has been saved, thank you!",
   					"index",
   					"main/rate.html",
   					'Please take the time to rate our service.'
   				)
	

def book(request):
	return processForm(
   					request,
   					OrderForm,
   					"Your order has been recorded, thank you!",
   					"index",
   					'main/book.html',
   					'Please provide the details of your booking.'
   				)


def contact(request):
	return processForm(
   					request,
   					ContactForm,
   					"We received your message, we'll get back to you very soon. Thank you!",
   					"index",
   					'main/contact.html',
   					'Please feel free to contact us.'
   				)
