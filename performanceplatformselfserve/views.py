from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def default(request):
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def question1(request):
    t = get_template('q1.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def question2(request):
    t = get_template('q2.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def question3(request):
    t = get_template('q3.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def question4(request):
    t = get_template('q4.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def question5(request):
    t = get_template('q5.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def summary(request):
    t = get_template('summary.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def confirmation(request):
    t = get_template('confirmation.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def goals(request):
    t = get_template('partial_goals.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def views(request):
    t = get_template('partial_views.html')
    html = t.render(Context({}))
    return HttpResponse(html)
