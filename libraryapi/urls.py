
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('catalog/', include('libraryapi.catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('admin/', admin.site.urls),
]