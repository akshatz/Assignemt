from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect


# Create your views here.
from cart_app.models import Cart, Book, BookOrder


def store(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'base.html', context)



def add_to_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
    else:
        try:
            cart = Cart.objects.get(user=request.user, active=True)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(user=request.user)
            cart.save()
            cart.add_to_cart(book_id)
            return redirect('cart')



def remove_from_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
            return redirect('cart')


def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user_id, active=True)
        orders = BookOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'cart_app/cart.html', context)
