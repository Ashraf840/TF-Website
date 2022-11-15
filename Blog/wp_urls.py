from django.urls import path, re_path
from Blog import views


urlpatterns = [
    # re_path(r'^category/$', views.categoryView, name='category'),
    # re_path(r'^category/(?P<name>\w+)/$', views.categoryView, name='category'),

    # path('articles/', views.postView, name='articles'),
    # path('articles/<slug:name>/', views.postView, name='articles'),
    # re_path(r'^articles/$', views.postView, name='articles'),
    # re_path(r'^articles/(?P<name>.+)/$', views.postView, name='articles'),
    re_path(r'^blogs/personal_cybersecurity/(?P<name>.+)/$', views.postView, name='articles'),
    re_path(r'^blogs/business_cybersecurity/(?P<name>.+)/$', views.postView, name='articles'),
    re_path(r'^blogs/(?P<name>.+)/$', views.postView, name='articles'),
    re_path(r'^case_studies/(?P<name>.+)/$', views.postView, name='articles'),
]


