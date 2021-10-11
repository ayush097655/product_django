from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('manage/', views.manage),
    path('logout/', views.logout),
]
