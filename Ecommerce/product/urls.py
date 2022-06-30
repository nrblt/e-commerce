from django.urls import path,include

from .views import *

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetails.as_view()),
    path('products/<slug:category_slug>/', CategoryDetails.as_view()),


]