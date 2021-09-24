
from django.contrib import admin
from django.urls import path
from .views import Index, sub_page
from django.views.generic import TemplateView

urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('sub',sub_page,name='submit_page')
]
