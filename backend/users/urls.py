from django.urls import path

from users.views import user, users


urlpatterns = [
    path('', users, name='users'),
    path('login/', users, name='login'),
    path('logout/', users, name='logout'),
    path('<int:user_id>/', user, name='user'),
]
