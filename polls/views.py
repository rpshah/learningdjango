# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question

def index(request):
	first_five_questions = Question.objects.order_by('pub_date')[:5] 
	context = {'questions_list' : first_five_questions}
	#return render(request, 'polls/index.html', context)
	
	template = loader.get_template('polls/index.html')
	return HttpResponse(template.render(context,request)) 

def detail(request, question_id):
	return HttpResponse("Displaying question %s" % question_id)

def results(request, question_id):
	return HttpResponse("Poll stats for question %s" % question_id)

def vote(request, question_id):
	return HttpResponse("Vote for question %s" % question_id)

# Create your views here.
