from django.contrib import admin
from django.urls import include, path
from genres import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]
