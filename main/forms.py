from django import forms
from models import Review, Order, Contact
from datetimewidget.widgets import DateTimeWidget
class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['author', 'rating', 'reviewText']
		help_texts = {
			'reviewText': 'If you have tried our service please let us know what you think.'
		}

		
class OrderForm(forms.ModelForm):
	
	class Meta:
		def make_array(item, num, initial_text):
			i = 1
			lst = [('', initial_text)]
			while i <= num:
				lst += [(i, '{} {}'.format(i, item))]
				i += 1
			return lst
		
		BEDROOM_CHOICES = make_array('Bedroom', 6, "How many bedrooms?")
		BATHROOM_CHOICES = make_array('Bathroom', 6, "How many bathrooms?")
		EXTRA_CHOICES = [
			('fridge', 'Inside Fridge'),
			('oven', 'Inside Oven'),
			('basement', 'Basement')
		]
		HOWOFTEN_CHOICES = [
			('onetime', '1 time'),
			('everyweek', 'Every Week'),
			('every2weeks', 'Every 2 weeks'),
			('every4weeks', 'Every 4 weeks'),
		]
		model = Order
		fields = '__all__'
		widgets = {
			'bedroomNumber': forms.Select(choices=BEDROOM_CHOICES, attrs={'onchange': 'addToPrice(this);'}),
			'bathroomNumber': forms.Select(choices=BATHROOM_CHOICES, attrs={'onchange': 'addToPrice(this);'}),
			'extras': forms.CheckboxSelectMultiple(choices=EXTRA_CHOICES, attrs={'onchange': 'addToPriceExtras(this);'}),
			#'howOften': forms.CheckboxSelectMultiple(choices=HOWOFTEN_CHOICES),
			'dateOfService': DateTimeWidget(options={'startDate': '+1d'},attrs={'required': 'required'}),
			'phone': forms.TextInput()
		}

		help_texts = {
			'address': 'The address of the space to be cleaned.',
			'city': 'We only provide service in Yerevan at this time.',
			'dateOfService': 'Please set the date and the time of your cleaning.'
		}
	


class ContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contactReason'].help_text2 = 'some help text'
	class Meta:
		model = Contact
		fields = '__all__'

		CONTACTCHOICES = [
			(0, "I have a question before I book"),
			(1, "I have a question about my paypent"),
			(2, "I would like to change my booking"),
			(3, "I am confused about how something works"),
			(4, "I have a customer service comment"),
			(5, "Other")
		]

		widgets = {
			'contactReason': forms.Select(choices=CONTACTCHOICES)
		}

		help_texts = {
			'contactReason': [
				'What do you need help with?',
				'This helps us make sure you get the right answer as fast as possible'
			],
			'text': [
				'What\'s your question, comment or issue?',
				'Give us as much detail as you can. The more we know, the better we can help you.'
			],
			'email': [
				'What\'s your email address?',
				'We need this so we can reply to you. Please make sure that it\'s right.'
			]
		}

	def clean_contactReason(self):
		data = self.cleaned_data['contactReason']
		i, data = self.Meta.CONTACTCHOICES[int(data)]
		return data