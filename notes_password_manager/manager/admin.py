from django.contrib import admin

# Register your models here.
from .models import Note
from .models import Password
from .models import Profile 


admin.site.register(Note)
admin.site.register(Password)
admin.site.register(Profile)
