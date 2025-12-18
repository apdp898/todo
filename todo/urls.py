from django.urls import path
from . import views
urlpatterns=[
path('',views.index),
path('complete/<int:pk>/',views.complete),
path('delete/<int:pk>/',views.delete)
]
