from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from performanceplatformselfserve.views import default

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'performanceplatformselfserve.views.default', name='default'),
    url(r'^question1/', 'performanceplatformselfserve.views.question1', name='question1'),
    url(r'^dashboard/', 'performanceplatformselfserve.views.dashboard', name='dashboard'),
    url(r'^question2/', 'performanceplatformselfserve.views.question2', name='question2'),
    url(r'^question3/', 'performanceplatformselfserve.views.question3', name='question3'),
    url(r'^question4/', 'performanceplatformselfserve.views.question4', name='question4'),
    url(r'^question5/', 'performanceplatformselfserve.views.question5', name='question5'),
    url(r'^summary/', 'performanceplatformselfserve.views.summary', name='summary'),
    url(r'^confirmation/', 'performanceplatformselfserve.views.confirmation', name='confirmation'),
    url(r'^goals/', 'performanceplatformselfserve.views.goals', name='goals'),
    url(r'^views/', 'performanceplatformselfserve.views.views', name='views'),
    url(r'^view_template/', 'performanceplatformselfserve.views.view_template', name='view_template'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
