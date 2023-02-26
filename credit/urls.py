from django.urls import path

from . import views

app_name = 'credit'

urlpatterns = [
    path('', views.all_credits, name='all_credits'),
    path('customer/<int:id>/', views.credit_detail, name='credit_detail'),
    path('verify/<int:id>/', views.verify, name='verify'),
    path('update-credit-form/<int:id>/', views.update_credit, name='update_credit'),
    path('create/', views.create_customer_credit, name='create_customer_credit'),
]
