from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import views
from .models import *

import random
# Create your views here.

def home(request):
    return HttpResponse('Hello')
# {
#     'status':True
#     'data':[
#         {},
#     ]
# }

def get_quiz(request):
    try:
        question_objs=list(Question.objects.all())
        data=[]
        random.shuffle(question_objs)
        for question_objs in question_objs:
            data.append({
                'category':question_objs.category.category_name,
                'question':question_objs.question,
                'marks':question_objs.marks

            })
            payload={'status':True,'data':data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse('STH WENT WRONG')