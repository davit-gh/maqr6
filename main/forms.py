# -*- coding: utf-8 -*-
from django import forms
from models import Review, Order, Contact
from datetimewidget.widgets import DateTimeWidget
from django.utils.translation import ugettext as _

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['author', 'rating', 'reviewText']
		help_texts = {
			'reviewText': _('If you have tried our service please let us know what you think.'),
			'rating'	: _('Please rate the service')
		}	
		labels = {
			'author'	: _('Your name'),
			'reviewText': _('Any feedback?')
		}


class PhoneInput(forms.widgets.Input):
	input_type = "tel"
		
class OrderForm(forms.ModelForm):
	
	dateOfService = forms.DateTimeField(
						widget = DateTimeWidget(
									options={'startDate': '+1d'},
									attrs={'required': 'required'}
								),
						label = _('Date and time'),
						input_formats=['%d/%m/%Y %H:%M'],
						help_text=_('Please set the date and the time of your cleaning.')
					)
	class Meta:
		def make_array(item, num, initial_text):
			i = 1
			lst = [('', initial_text)]
			while i <= num:
				lst += [(i, '%s %s'%(i, item))]
				i += 1
			return lst
		
		BEDROOM_CHOICES = make_array(_('Bedroom'), 6, _("How many bedrooms?"))
		BATHROOM_CHOICES = make_array(_('Bathroom'), 6, _("How many bathrooms?"))
		EXTRA_CHOICES = [
			('fridge', _('Inside Fridge')),
			('oven', _('Inside Oven')),
			('basement', _('Basement'))
		]
		HOWOFTEN_CHOICES = [
			('onetime', _('1 time')),
			('everyweek', _('Every Week')),
			('every2weeks', _('Every 2 weeks')),
			('every4weeks', _('Every 4 weeks')),
		]
		model = Order
		fields = '__all__'
		widgets = {
			'bedroomNumber': forms.Select(choices=BEDROOM_CHOICES, attrs={'onchange': 'addToPrice(this);'}),
			'bathroomNumber': forms.Select(choices=BATHROOM_CHOICES, attrs={'onchange': 'addToPrice(this);'}),
			'extras': forms.CheckboxSelectMultiple(choices=EXTRA_CHOICES, attrs={'onchange': 'addToPriceExtras(this);'}),
			#'howOften': forms.CheckboxSelectMultiple(choices=HOWOFTEN_CHOICES),
			'phone': PhoneInput(),
			'email': forms.EmailInput(attrs={'onblur': 'verifyEmail(this)'})
		}
		labels = {
			'fullName': _('Your full name'),
			'phone': _('Your mobile'),
			'email': _('Your email'),
			'address': _('Address')
		}
		help_texts = {
			'address': _('The address of the space to be cleaned.'),
			'city': _('We provide service only in Yerevan at this time.')
		}
	


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

		CONTACTCHOICES = [
			(0, _("I have a question before I book")),
			(1, _("I have a question about my payment")),
			(2, _("I would like to change my booking")),
			(3, _("I am confused about how something works")),
			(4, _("I have a customer service comment")),
			(5, _("Other"))
		]

		widgets = {
			'contactReason': forms.Select(choices=CONTACTCHOICES),
			'email': forms.EmailInput(attrs={'onblur': 'verifyEmail(this)'})
		}

		help_texts = {
			'contacetReason': [
				_('What do you need help with?'),
				_('This helps us make sure you get the right answer as fast as possible')
			],
			'text': [
				_('What\'s your question, comment or issue?'),
				_('Give us as much detail as you can. The more we know, the better we can help you.')
			],
			'email': [
				_('What\'s your email address?'),
				_('We need this so we can reply to you. Please make sure that it\'s right.')
			]
		}
		
		labels = {
			'email': _('Your email')
		}

	def clean_contactReason(self):
		data = self.cleaned_data['contactReason']
		i, data = self.Meta.CONTACTCHOICES[int(data)]
		return data