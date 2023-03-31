from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product-details/', views.product_details, name='product-details'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('contact-us/', views.contact, name='contact-us'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('404/', views.opps, name='404')
    
]