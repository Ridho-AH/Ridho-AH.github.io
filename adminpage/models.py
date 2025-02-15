from django.db import models
from django.db.models.functions import Lower
import time
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import make_aware


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    photo = models.ImageField(upload_to='stock_images', default='stock_images/default.png', null=True, blank=True)
    description = models.CharField(max_length=360)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    # updated_at = models.DateTimeField(auto_now=True, default=timezone.now)
    class Meta:
        ordering = [Lower("name")]
    
    def __str__(self):
        return f'{self.name}'
    
    def get_actual_price(self):
        if self.discount != 0:
            price_base = self.price
            disc = int(price_base * self.discount / 100)
            actual = price_base - disc
        else:
            actual = self.price
        return actual

    def get_purchase(self):
        base_link = "https://wa.me/6282324564979?text=Halo+GraciouScent,+saya+ingin+membeli+produk+"
        base_name = self.name
        name_link = base_name.replace(" ", "+")
        final_link = base_link+name_link+"."+"+Apakah+produk+tersebut+masih+tersedia?"
        return final_link



