from django.urls import path

from core.api import views

urlpatterns = [
    path('',views.itemApi),
    path('<str:pk>/',views.itemDetailApi),
]
