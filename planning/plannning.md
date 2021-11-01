# UShop.com

## Description

ECommerce Api:
Where authenticated users can do full crud operations on products, reviews, orders.
Users authentications is applied.
As an Admin can do full crud operations on users, products, orders.

## Technologies used:
Django | postgresql

## Models
Product, review, order, orderItem, shipping
### example
class Product(models.Model):
    # owner = models.ForeignKey(
    #     'users.User', related_name='products', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/default.jpg')
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReview = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

## URLS
### BaseURLS
    all api paths are given 
    Product, orders, orderItem, shipping, reviews
### Project URLS
- url to admin, api-auth, to users and to main app are given
