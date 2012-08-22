from django.conf.urls import patterns, include, url

urlpatterns = patterns('picman.views',
    url(r'^$', 'form'),
)
