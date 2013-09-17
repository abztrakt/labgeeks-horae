from labgeeks_horae.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class TimePeriodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(BaseShift)
admin.site.register(ShiftType)
admin.site.register(DefaultShift)
admin.site.register(WorkShift)
admin.site.register(TimePeriod, TimePeriodAdmin)
