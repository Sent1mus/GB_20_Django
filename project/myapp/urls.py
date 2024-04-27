from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/', views.order_list, name='orders_list'),
    path('ordered_products/<int:client_id>/<slug:period>/', views.ordered_products_list, name='ordered_products'),
    path('ordered_products_unique/<int:client_id>/<slug:period>/', views.ordered_products_unique, name='ordered_products_unique'),
    path('products_list/', views.products_list, name='products_list'),
    path('edit_products/', views.edit_product_and_add_photo, name='edit_product_and_add_photo'),
]