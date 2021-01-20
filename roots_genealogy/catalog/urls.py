from django.urls import path
from . import views

urlpatterns = [
    path("", views.produse_index, name="produse_index"),
    path("<int:pk>/", views.produse_detail, name = "produse_detail"),
]