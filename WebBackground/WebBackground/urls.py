"""
URL configuration for WebBackground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pages.urls import pagespatterns
from Profiles.urls import Profiles_patterns
from Messenger.urls import Messenger_patterns
from django.conf import settings

urlpatterns = [
    path('',include('core.urls'),name="core"),
    path('pages/',include(pagespatterns)),
    path('admin/', admin.site.urls),
    #path authentication
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('registration.urls')),
    path('profiles/',include(Profiles_patterns)),
    path('messenger/',include(Messenger_patterns)),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
