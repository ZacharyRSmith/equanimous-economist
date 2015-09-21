from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'equanimous_economist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('main.urls')),
    url(r'^about/$', views.about, name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
