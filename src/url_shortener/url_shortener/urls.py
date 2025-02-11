from django.urls import path, include

urlpatterns = [
    path('shrt/', include('shortener.urls')),
]
