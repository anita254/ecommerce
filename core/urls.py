from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    
    #Homepage
    path("", views.index, name="index"),
    path("products/", views.product_list_view, name="product-list" ),
    
    #Category
    path("category/", views.category_list_view, name="category-list" ),
    path("category/<cid>/", views.category_product_list_view, name="category-product-list" ),
    
    #Vendor
    path("vendors/", views.vendor_list_view, name="vendor-list" ),

]
