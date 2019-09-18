from django.urls import path

from . import views
 
# url пути
urlpatterns = [
 	path('', views.index, name = 'index'),
 	path('test/', views.test, name = 'test')

]
