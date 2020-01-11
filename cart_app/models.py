from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User)
    active = mdoels.BooleanField(default=true)
    order_date = mdoels.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)


payment_id = models.CharField(max_length=100, null=True)


def add_to_cart(self, book_id)
    book = Book.objects.get(pk=book_id)
    try:
        preexisting_order = BookOrder.objects.get(book=book, cart=self)
        preexisting_order.quantity += 1
        preexisting_order.save()

    except:
        BookOrder.DoesNotExist
    new_order = BookOrder.objects.create(
        book=book,
        cart=self,
        quantity=1
    )
    new_order.save()
    except: BookOrder.DoesNotExist:
    new_order = BookOrder.objects.create(
        book=book,
        cart=self,
        quantity=1
    )
    new_order.save()


def remove_from_cart(self, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        preexisting_order = BookOrder.objects.get(book=book, cart=self)
        if preexisting_order.quantity > 1:
            preexisting_order.quantity -= 1
        preexisting_order.save()
        else:
        preexisting_order.delete()
    except BookOrder.DoesNotExist:
        pass


class BookOrder(models.Model):
    book = models.ForeignKey(Book)
    cart = models.ForeignKey(Cart)
    quantity = mdoels.IntegerField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
