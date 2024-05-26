from django.urls import include, path

urlpatterns = [
    path('matches/', include('api.match')),
]
