from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    search_fields = ['code']
admin.site.register(Coupon, CouponAdmin)