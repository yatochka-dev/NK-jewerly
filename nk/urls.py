"""nk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

handler400 = 'main.views.bad_request'
handler403 = 'main.views.permission_denied'
handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'

urlpatterns = [
	              path('admin/', admin.site.urls),
              ] + i18n_patterns(
	path('i18n/', include('django.conf.urls.i18n')),
	path('', include("main.urls")),
	prefix_default_language=False,
)

# if settings.DEBUG:
# 	urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))

# @TODO REMOVE THIS LINE AFTER DEBUGGING
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
