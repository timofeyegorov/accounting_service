from django.urls import path
from billapp import views

urlpatterns = [
    path('', views.main_view, name='index'),
    path('enter/', views.enter_expenses, name='enter'),
    path('contacts/', views.contacts, name='contacts'),
    path('success/', views.enter_expenses, name='success')
]
