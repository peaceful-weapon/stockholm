from django.conf.urls import patterns, include, url
from django.contrib import admin
from Courses import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', views.main_page),
    url(r'^course/(?P<course_title>\w+)/$',views.course_view), 
)
