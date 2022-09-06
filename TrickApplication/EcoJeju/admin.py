from django.contrib import admin
from EcoJeju.models import user
from EcoJeju.models import worker

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        #'user_pwd',
        'user_name',
        'register_date'
    )

@admin.register(worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'worker_id',
        #'worker_pwd',
        'worker_name',
        'register_date'
    )