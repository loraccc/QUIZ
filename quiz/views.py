from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from . import views
from .models import *
import random
# Create your views here.

def home(request):
    context={'categories':Category.objects.all}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request,'home.html',context)


def quiz(request):
    return render(request,'quiz.html')
# {
#     'status':True
#     'data':[
#         {},
#     ]
# }

def get_quiz(request):
    try:
        question_objs=Question.objects.all()
        
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category')) #filtering to get the desired ans category is related name and db underscore helps to access foreignkey element 
        question_objs=list(question_objs) #if doesnt get the filter
        data=[]
        random.shuffle(question_objs)
        for question_objs in question_objs:
            data.append({
                'category':question_objs.category.category_name,
                'question':question_objs.question,
                'marks':question_objs.marks,
                'answers':question_objs.get_answers(),

            })
            payload={'status':True,'data':data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse('STH WENT WRONG')