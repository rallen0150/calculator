from django.contrib import admin
from app.models import Operation, Profile

# Register your models here.

admin.site.register([Operation, Profile])
