from django.urls import path
from . import views

app_name = 'site'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path("featured/",views.Featured.as_view(),name="featured"),
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path("gallery/",views.Gallery.as_view(), name="gallery"),
    path("projects/previous/", views.PrevProjectView, name="prev"),
    path('projects/current/', views.CurrProjectView, name='curr'),
    path('projects/current/imdaad', views.ImdaadView, name='imdaad'),
    path('projects/current/irtiqa', views.IrtiqaView, name='irtiqa'),
    path('projects/current/shrimati', views.Shrimati.as_view(), name='shrimati'),
    path("blogs/", views.BlogListView, name="blog_list"),
    path("blogs/bamboo", views.BambooView, name="bamboo"),
    path("blog/mensuration", views.MensurationView, name="mensuration"),
    path("blog/myth",views.MythView, name="myth"),
    path("blog/climate",views.ClimateView,name="climate"),
    path("blog/water",views.WaterView,name="water"),
    path("blogs/sanitation", views.SanotationView, name="sanitation"),
    path("blogs/women", views.WomenView, name="women"),
    

    path("blogs/category", views.BlogCategory, name="blog_cat"),
    path("blog/<int:pk>", views.BlogDetailView.as_view(), name="blog_detail")
]
