from django.contrib import admin
from django.urls import include, path

import django_eventstream

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api')),
    path('sse/matches/<match_id>/', include(django_eventstream.urls), {'format-channels': ['match-{match_id}']}),
    path('', include('views')),
]
