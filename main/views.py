# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import ReviewForm, OrderForm, ContactForm
from models import Review
from includes.viewinclude import FormClass
from django.shortcuts import render

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


def rate(request):
	form =  FormClass(
				ReviewForm, 
				"Maqr6", 
				'Please take the time to rate our service.'
			)
   	return  form.processForm(
				request,		
				"Your review has been saved, thank you!",
				"index",
				"main/rate.html",
			)
	

def book(request):
	form =  FormClass(
				OrderForm, 
				"Maqr6", 
				'Please provide the details of your booking.'
			)
	return  form.processForm(
				request,
				"Your order has been recorded, thank you!",
				"index",
				'main/book.html'
   			)


def contact(request):
	form  = FormClass(
				ContactForm, 
				'Questions? We are happy to answer!',
				'There are exactly 4 ways you can reach us.'
			)
	contact_methods = {
		'method1': 'Get fast answers on Facebook: <a href="https://facebook.com">Maqr6</a>',
		'method2': 'Email us directly at: support@maqr6.am',
		'method3': 'TEXT us on mobile at: 094 43-34-16'
	}

	form.addContext(**contact_methods)

	return  form.processForm(
				request,
				"We received your message, we'll get back to you very soon. Thank you!",
				"index",
				'main/contact.html'
   			)
	