from django.urls import path

from courses.views import course, courses


urlpatterns = [
    path('', courses, name='courses'),
    path('<int:user_id>/', course, name='course'),
]
