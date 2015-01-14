from django.template import loader, Context, RequestContext
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
    request.session.flush()
    t = loader.get_template('index.html')
    html = t.render(Context({
        "govuk_template_path": '/static/govuk_template/',
    }))
    return HttpResponse(html)


def question1(request):
    t = loader.get_template('q1.html')
    dashboards = get_local_JSON('dashboards.json', 'title')
    organisations = get_local_JSON('organisations.json', 'name')
    context = RequestContext(request, {
        "govuk_template_path": '/static/govuk_template/',
        "dashboards": dashboards,
        "organisations": organisations
    })
    return HttpResponse(t.render(context))


def dashboard(request):
    slug = request.GET.get('slug')
    data = get_remote_JSON(
        'https://stagecraft.preview.performance.service.gov.uk/' +
        'public/dashboards?slug=' +
        slug
        )
    t = loader.get_template('partial_dashboard.html')
    html = t.render(Context(data))
    return HttpResponse(html)


def question2(request):
    request.session['dashboard_name'] = request.GET.get('dashboard_name')
    request.session['dashboard_description'] = request.GET.get('dashboard_description')
    request.session['dashboard_organisation'] = request.GET.get('dashboard_organisation')
    request.session['new_dashboard_name'] = request.GET.get('new_dashboard_name')
    request.session['new_dashboard_description'] = request.GET.get('new_dashboard_description')
    request.session['new_dashboard_organisation'] = request.GET.get('new_dashboard_organisation')
    t = loader.get_template('q2.html')
    context = RequestContext(request, {
        "govuk_template_path": '/static/govuk_template/',
    })
    return HttpResponse(t.render(context))

def question3(request):
    request.session['contact_name'] = request.GET.get('contact_name')
    request.session['contact_email'] = request.GET.get('contact_email')
    t = loader.get_template('q3.html')
    context = RequestContext(request, {
        "govuk_template_path": '/static/govuk_template/',
    })
    return HttpResponse(t.render(context))

def question4(request):
    request.session['digitalchannels'] = [
        c for c in request.GET.getlist('digitalchannels')]
    request.session['nondigitalchannels'] = [
        c for c in request.GET.getlist('nondigitalchannels')]
    t = loader.get_template('q4.html')
    context = RequestContext(
        request,
        {
            "next_page": (request.GET.get('from') or '/question5'),
            "govuk_template_path": '/static/govuk_template/'
        }
    )
    return HttpResponse(t.render(context))

def download_spreadsheet(request):
    spreadsheet = open("performanceplatformselfserve/static/downloads/example-data-import.xls","rb").read()
    response = HttpResponse(spreadsheet, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="example-data-import.xls"'
    return response

def question5(request):
    if 'channels_use_direct_api' in request.GET:
        request.session['channels_use_direct_api'] = 'yes'
    else:
        request.session['channels_use_direct_api'] = ''
    t = loader.get_template('q5.html')
    context = RequestContext(request, {
        "govuk_template_path": '/static/govuk_template/',
    })
    return HttpResponse(t.render(context))

def summary(request):
    request.session['viewlist'] = [
        c for c in request.GET.getlist('viewlist')]
    request.session['view'] = request.GET.get('view')
    request.session['goallist'] = [
        c for c in request.GET.getlist('goallist')]
    request.session['goal'] = request.GET.get('goal')
    request.session['analytics'] = request.GET.get('analytics')
    request.session['analytics_other_name'] = request.GET.get('analytics_other_name')

    t = loader.get_template('summary.html')
    context = RequestContext(
        request,
        {
            "govuk_template_path": '/static/govuk_template/',
            "dashboard_name": request.session['dashboard_name'],
            "dashboard_description": request.session['dashboard_description'],
            "dashboard_organisation": request.session['dashboard_organisation'],
            "new_dashboard_name": request.session['new_dashboard_name'],
            "new_dashboard_description": request.session['new_dashboard_description'],
            "new_dashboard_organisation": request.session['new_dashboard_organisation'],
            "contact_name": request.session['contact_name'],
            "contact_email": request.session['contact_email'],
            "digitalchannels": request.session['digitalchannels'],
            "nondigitalchannels": request.session['nondigitalchannels'],
            "channels_use_direct_api": request.session['channels_use_direct_api'],
            "viewlist": request.session['viewlist'],
            "view": request.session['view'],
            "goallist": request.session['goallist'],
            "nogoals": len(request.session['goallist']) == 0,
            "goal": request.session['goal'],
            "analytics": request.session['analytics'],
            "analytics_other_name": request.session['analytics_other_name']
        }
    )
    return HttpResponse(t.render(context))


def confirmation(request):
    t = loader.get_template('confirmation.html')
    html = t.render(Context(
        { "govuk_template_path": '/static/govuk_template/', }
    ))
    return HttpResponse(html)


def goal_template(request):
    tmp = open(os.path.join(os.path.dirname(__file__),
               '../templates/partial_goals.html'))
    return HttpResponse(tmp)


def views(request):
    t = loader.get_template('partial_views.html')
    html = t.render(Context({}))
    return HttpResponse(html)


def view_template(request):
    tmp = open(os.path.join(os.path.dirname(__file__),
               '../templates/partial_views.html'))
    return HttpResponse(tmp)
