from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('product/', views.product, name='dashboard-product'),
    path('staff/', views.staff, name = 'dashboard-staff'),
    path('order/', views.order, name='dashboard-order'),
    path('product/delete/<int:pkey>/',views.delete_product, name = 'dashboard-delete-product'),
    path('product/update/<int:pkey>/',views.update_product, name = 'dashboard-update-product'),
    
]