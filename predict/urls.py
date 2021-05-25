from django.urls import path, include
from predict import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preview', views.pre, name='pre'),
    path('preview1', views.preview, name='preview'),
    path('predict/', views.predict, name='predict'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('cam_front/', views.cam_front, name='cam_front'),
]
