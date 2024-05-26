from django.urls import include, path

urlpatterns = [
    path('match/', include('views.match')),
]
