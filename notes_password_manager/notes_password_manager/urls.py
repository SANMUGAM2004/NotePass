# notes_password_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from manager.views import home  # Add this import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manager.urls')),
    path('', home, name='root'),  
]
