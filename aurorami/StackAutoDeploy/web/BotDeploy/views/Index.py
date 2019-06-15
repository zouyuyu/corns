from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):

    return render(request, 'html/index.html')

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('static/html/index.html')
    # context = {
    # }
    # return HttpResponse(template.render(context, request))