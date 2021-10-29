from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),

    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

    path('orders/', views.OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order_detail'),

    path('orderItems/', views.OrderItemList.as_view(), name='orderItem_list'),
    path('orderItems/<int:pk>', views.OrderItemDetail.as_view(),name='orderItem_detail'),

    path('shippingAddresses/', views.ShippingAddressList.as_view(),name='shippingAddress_list'),
    path('shippingAddresses/<int:pk>',
         views.ShippingAddressDetail.as_view(), name='shippingAddress_detail'),

    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken'))

]
