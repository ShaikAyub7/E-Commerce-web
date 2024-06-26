from . import views
from django.contrib import admin
from django.urls import path
from myapp.urls import *
from django.urls import path
from django.contrib.auth import views as auth_views
# urls.py
from django.urls import path
# from .views import PasswordResetView, PasswordResetConfirmView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',views.profile_page,name='profile_page.html'),
    path('profile/edit/',views.edit_profile, name='edit-profile.html'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('cart/', views.cart_view, name='cart_view'),
    path('login/',views.login_page,name='login.html'),
    path('cart/',views.cart, name='cart.html'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register,name='register.html'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('',views.index,name='index.html'),
    path('product/<slug:slug>/', views.product, name='product'),

]