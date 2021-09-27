
from django.contrib import admin
from django.urls import path
from .views import Index, sub_page
from django.http import HttpResponse

def okay(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')
urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('sub',sub_page,name='submit_page'),
    path('favicon.ico', okay),

]
