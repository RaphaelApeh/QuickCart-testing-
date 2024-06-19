from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name='home'),
    path('new/',views.formView,name='new'),
    path('edit/<str:pk>/',views.updateView,name='update'),
    path('delete/<str:pk>/',views.deleteView,name='delete'),
    path('detail/<str:pk>/',views.detailView,name='detail'),
    path('category/<str:pk>/',views.category_view,name='category'),
    path('user/item/',views.user_detail,name='user_item')

]