from django.urls import path, include

from cart_app.views import cart

urlpatterns = [
    path('',cart, name="cart")
]