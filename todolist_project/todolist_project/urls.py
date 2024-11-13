from django.contrib import admin
from django.urls import path, include
from todos.views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),  # Include todos app URLs
]
