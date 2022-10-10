from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(question)
admin.site.register(result)
admin.site.register(group_choice_change)
admin.site.register(RIASEC)
admin.site.register(report_purchase_successful)
admin.site.register(coupon)