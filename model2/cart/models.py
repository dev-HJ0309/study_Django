from django.db import models

from member.models import Member
from model2.models import Period
from product.models import Product


# Create your models here.
class Cart(Period):
    product_count = models.IntegerField(null=True)
    member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_cart"

    def __str__(self):
        return self.product.product_name
