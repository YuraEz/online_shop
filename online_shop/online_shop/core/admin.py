from django.contrib import admin
from .models import Good, Cart
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Good)
admin.site.register(Cart)
# admin.site.register(Buyer, UserAdmin)
