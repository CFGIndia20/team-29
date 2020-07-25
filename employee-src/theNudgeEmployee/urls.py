from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
<<<<<<< HEAD
]
=======
    path('', include('accounts.urls')),
]
>>>>>>> d483562cc79ffe1c27ca5fa37de893b6d5f45d24
