from django.contrib import admin
from .models import User, SubjectNames, Uroki
# Register your models here.
# admin.register((User, SubjectNames), admin.site)
admin.site.register((User, SubjectNames, Uroki))
