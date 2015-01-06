from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import json
import os
import urllib2


def get_local_JSON(filename, sort_key=None):
    json_data = open(
        os.path.join(os.path.dirname(__file__), 'data/' + filename))
    data1 = json.load(json_data, "utf-8")
    if sort_key is not None:
        data1 = sorted(data1, key=lambda k: k[sort_key])
    json_data.close()
    return data1


def get_remote_JSON(path):
    url = urllib2.urlopen(path)
    data = json.load(url, "utf-8")
    return data


def default(request):
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)


def question1(request):
    t = get_template('q1.html')
    dashboards = get_local_JSON('dashboards.json', 'title')
    organisations = get_local_JSON('organisations.json', 'name')
    html = t.render(Context({
        "dashboards": dashboards,
        "organisations": organisations
    }))
    return HttpResponse(html)


def dashboard(request):
    slug = request.GET.get('slug')
    data = get_remote_JSON(
        'https://stagecraft.preview.performance.service.gov.uk/' +
        'public/dashboards?slug=' +
        slug
        )
    t = get_template('partial_dashboard.html')
    html = t.render(Context(data))
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
    model = get_local_JSON('model.json')
    t = get_template('summary.html')
    html = t.render(Context(model))
    return HttpResponse(html)


def confirmation(request):
    model = get_local_JSON('model.json')
    t = get_template('confirmation.html')
    html = t.render(Context(model))
    return HttpResponse(html)


def goals(request):
    t = get_template('partial_goals.html')
    html = t.render(Context({}))
    return HttpResponse(html)


def views(request):
    t = get_template('partial_views.html')
    html = t.render(Context({}))
    return HttpResponse(html)


def view_template(request):
    tmp = open(os.path.join(os.path.dirname(__file__),
               'templates/partial_views.html'))
    return HttpResponse(tmp)
