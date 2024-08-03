from django.contrib import admin
from .models import Campaign, Donation, Transaction
# Register your models here.
admin.site.register(Campaign)
admin.site.register(Donation)