from django.contrib import admin
from .models import User

# Superuser로 관리하기 위해 만들어 줌.
admin.site.register(User)
