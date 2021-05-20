from django.db import models
from django.db.models.base import Model
from django.db.models.query import FlatValuesListIterable

# Create your models here.
class bill(models.Model):
    bill_id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False)
    uname = models.CharField(max_length=45, unique=True, blank=False)
    bill_status = models.BooleanField(blank=False)
    bill_amount = models.FloatField(blank=False)
    paid_amount = models.FloatField(blank=False)


class item(models.Model):
    units = (
        ('gm', 'gm '),
        ('kg', 'kg'),
    )
    item_id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False)
    item_name = models.CharField(max_length=45, blank=False) 
    item_unit = models.CharField(max_length=45, blank=False, choices=units)
    item_price = models.FloatField(blank=False)
    item_stock = models.FloatField(blank=False)

class bill_detail(models.Model):
    units = (
        ('gm', 'gm '),
        ('kg', 'kg'),
    )
    detail_id = models.PositiveIntegerField(primary_key=True, unique=True, blank=False)
    bill_id = models.ForeignKey(bill, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    item_quantity = models.FloatField(blank=False)
    item_unit = models.CharField(max_length=20, blank=False, choices=units)