from .models import bill, bill_detail, item
from django.contrib import admin

admin.site.register(item)
admin.site.register(bill_detail)
admin.site.register(bill)
