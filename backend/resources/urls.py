from django.urls import path

from resources.views import resource, resources


urlpatterns = [
    path('', resources, name='resources'),
    path('<int:user_id>/', resource, name='resource'),
]
