from django.contrib import admin
from django.urls import path

admin.site.site_header = "Управление магазином"

admin.site.site_title = "админ панель магазина"

admin.site.index_title = "Добро пожаловать в админ панель магазина"

urlpatterns = [
    path('admin/', admin.site.urls),
]

