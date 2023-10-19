from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('savvydata.urls')),  # This includes all URLs from the 'savvydata' app
    # Add other paths for your project
]