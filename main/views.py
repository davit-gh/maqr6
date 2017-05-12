# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from forms import ReviewForm, OrderForm, ContactForm
from models import Review
from includes.viewinclude import FormClass
from django.shortcuts import render

# Create your views here.
def index(request):
	reviews = Review.objects.filter(id__lte=14).filter(id__gte=12)
	context = {
		'reviews': reviews,
		'pageHeader': {
			'title': _('Maqr6'),
			'strapline': _('Shine like your house will!')
		}
	}
	return render(request, 'main/index.html', context)


def rate(request):
	form =  FormClass(
				ReviewForm, 
				_('Maqr6'), 
				_('Please take the time to rate our service.')
			)
   	return  form.processForm(
				request,		
				_('Your review has been saved, thank you!'),
				'index',
				'main/rate.html',
			)
	

def book(request):
	form =  FormClass(
				OrderForm, 
				_('Maqr6'), 
				_('Please provide the details of your booking.')
			)
	return  form.processForm(
				request,
				_('Your order has been recorded, thank you! If this is your first order we\'ll call you for verification.'),
				'index',
				'main/book.html'
   			)


def contact(request):
	form  = FormClass(
				ContactForm, 
				_('Questions? We are happy to answer!'),
				_('There are exactly 4 ways you can reach us.')
			)
	contact_methods = {
		'method1': _('Get fast answers on Facebook: <a href="https://facebook.com">Maqr6</a>'),
		'method2': _('Email us directly at: support@maqr6.am'),
		'method3': _('TEXT us on mobile at: 094 43-34-16')
	}

	form.addContext(**contact_methods)

	return  form.processForm(
				request,
				_('We received your message, we\'ll get back to you very soon. Thank you!'),
				'index',
				'main/contact.html'
   			)
	