from django.db import models
import PIL

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    disc = models.TextField(max_length=560)
    pic = models.ImageField(blank=True, upload_to='')
    image1 = models.ImageField(blank=True, upload_to='')
    image2 = models.ImageField(blank=True, upload_to='')
    image3 = models.ImageField(blank=True, upload_to='')
    category = models.CharField(max_length=50, default="", blank=False, choices=[
        ("Tea Lights", "Tea Lights"),
        ("Lamps", "Lamps"),
        ("Pen Stand","Pen Stand"),
        ("Planter Bottle","Planter Bottle"),
        ("Planter Testube","Planter Testube")
    ])
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Costumer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=560, null=True)
    city = models.CharField(max_length=560, null=True)
    state = models.CharField(max_length=560, null=True)
    zipcode = models.CharField(max_length=560, null=True)

    def __str__(self) -> str:
        return self.email


class Order(models.Model):
    costumer = models.ForeignKey(
        Costumer, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(max_length=560, null=True, blank=False)
    transaction_id = models.CharField(max_length=560, null=True, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return ("By: " + self.costumer.name+"\tCompleted:" + str(self.complete))

    @property
    def get_cart_total(self):
        orderitems = self.order_item_set.all()
        total = sum([item.egt_total for item in orderitems])
        return total

    @property
    def get_cart_item(self):
        orderitems = self.order_item_set.all()
        total = sum([item.quantity for item in orderitems])


class Order_item(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=0, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

    def __str__(self) -> str:
        return ("BY: "+self.order.costumer.name+" Product:" + self.product.name)
