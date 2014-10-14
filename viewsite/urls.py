from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views import generic


urlpatterns = patterns(
    '',
    url(r'^$', generic.TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
