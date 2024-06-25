from django.contrib import admin

# Register your models here.
from .models import Photo

# admin 페이지에서 모델 관리
admin.site.register(Photo)
