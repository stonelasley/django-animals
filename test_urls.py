from django.conf.urls import include, url

urlpatterns = [
    url(r'^pups/', include('animals.urls', namespace='animals')),
]
