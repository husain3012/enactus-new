from django.http import request, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators import csrf
from django.views.generic import ListView, DetailView, TemplateView, CreateView
import datetime
from . import models
import json
import razorpay
# from . import config

def IndexView(request):
    products = models.Product.objects.all()
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {
        "get_cart_total": 0,
        "get_cart_item": 0,
    }
    cartItems = order["get_cart_item"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = models.Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_item"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "pic": product.pic,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)
        except:
            pass
    context = {"items": items, "order": order,
               "cartItems": cartItems, "products": products}
    return render(request, 'store/index.html', context)


def ProductListView(request):
    products = models.Product.objects.all()
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {
        "get_cart_total": 0,
        "get_cart_item": 0,
    }
    cartItems = order["get_cart_item"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = models.Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_item"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "pic": product.pic,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)
        except:
            pass
    context = {"items": items, "order": order,
               "cartItems": cartItems, "products": products}
    return render(request, 'store/product_list.html', context)


class ProductDetailView(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        try:
            cart = json.loads(self.request.COOKIES['cart'])
            # cart = {"1": {"quantity": 8}, "2": {"quantity": 1}}
        except:
            cart = {}
        items = []
        order = {
            "get_cart_total": 0,
            "get_cart_item": 0,
        }
        cartItems = order["get_cart_item"]

        for i in cart:
            try:
                cartItems += cart[i]["quantity"]
                product = models.Product.objects.get(id=i)
                total = product.price * cart[i]["quantity"]

                order["get_cart_total"] += total
                order["get_cart_item"] += cart[i]["quantity"]

                item = {
                    "product": {
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                        "pic": product.pic,
                    },
                    "quantity": cart[i]["quantity"],
                    "get_total": total,
                }
                items.append(item)
            except:
                pass
        # context['book_list'] = Book.objects.all()
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        # print(context)
        # print(cart)
        return context


def FAQView(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {
        "get_cart_total": 0,
        "get_cart_item": 0,
    }
    cartItems = order["get_cart_item"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = models.Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_item"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "pic": product.pic,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)
        except:
            pass
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, 'store/faq.html', context)


def CartView(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {
        "get_cart_total": 0,
        "get_cart_item": 0,
    }
    cartItems = order["get_cart_item"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = models.Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_item"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "pic": product.pic,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)
        except:
            pass
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, 'store/shopping-cart.html', context)


def CheckoutView(request):
    costumer = models.Costumer.objects.all()
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {
        "get_cart_total": 0,
        "get_cart_item": 0,
    }
    cartItems = order["get_cart_item"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = models.Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_item"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "pic": product.pic,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)
        except:
            pass

    amount = order["get_cart_total"]

    # razorpay integration

    client = razorpay.Client(
        auth=(config.test_key, config.test_secret)
    )
    payment = client.order.create(
        {
            "amount": int(amount) * 100,
            "currency": "INR",
            "payment_capture": "1",
        }
    )
    # print(payment)

    context = {
        'costumers': costumer,
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "payment": payment,
    }
    return render(request, 'store/checkout.html', context)


def CostumerForm(request):
    data = json.loads(request.body)
    # print("submitted")
    # print(data)
    cart = data['form']['cart']

    name = data["form"]["name"]
    email = data["form"]["email"]

    costumer, created = models.Costumer.objects.get_or_create(
        email=email, name=name, address=data['form']["address"], city=data['form']['city'], state=data['form']['state'], zipcode=data['form']['zipcode'])
    # costumer.save()

    transaction_id = datetime.datetime.now().timestamp()

    order = models.Order.objects.create(
        costumer=costumer, transaction_id=transaction_id, order_id=data['form']['paymentId'], complete=False)
    order.save()
    for item in cart.keys():
        product, create = models.Product.objects.get_or_create(id=item)
        orderItem = models.Order_item.objects.create(
            product=product, order=order, quantity=cart[item]['quantity'])

    return JsonResponse("submitted", safe=False)


@csrf.csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        # print(a['razorpay_order_id'])
        order = models.Order.objects.get(order_id=a['razorpay_order_id'])
        order.complete = True
        order.save()
        # print("order ", order.complete)

    return render(request, 'store/success.html', {})
