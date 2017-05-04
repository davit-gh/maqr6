from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

class FormClass(object):
	"""docstring for FormClass"""
	def __init__(self, form, title, strapline):
		super(FormClass, self).__init__()
		self.context = {
			'form': form,
			'pageHeader': {
				'title': title,
				'strapline': strapline
			}
		}
	def getContext(self):
		return self.context

	def addContext(self, **kwargs):
		for k, v in kwargs.items():
			self.context[k] = v

	def processForm(self, request, message, redirectViewName, tplName):
		
		f = self.context['form']
		if request.method == 'POST':
			sampleForm = f(request.POST)
#			import pdb;pdb.set_trace()
			if sampleForm.is_valid():
				sampleForm.save()
				messages.success(request, message)
				return redirect(reverse(redirectViewName))
		else:
			sampleForm = f()
		self.addContext(**{'form':sampleForm})
		return render(request, tplName, self.getContext())
