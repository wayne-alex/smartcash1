from django.contrib import admin
from .models import Account, Referral, Withdraw, Deposit,Package

admin.site.register(Account)
admin.site.register(Referral)
admin.site.register(Deposit)
admin.site.register(Package)
admin.site.register(Withdraw)
