from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'store'

urlpatterns = [
    path('', views.IndexView, name='store'),
    path('products/', views.ProductListView, name='list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('cart/', views.CartView, name='cart'),
    path('checkout/', views.CheckoutView, name='checkout'),
    path('formdata/', views.CostumerForm, name="form"),
    path('success/', views.success, name='success'),
    path('faq/', views.FAQView, name='faq'),
]
urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
