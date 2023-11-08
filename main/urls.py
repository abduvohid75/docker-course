from django.contrib import admin
from django.urls import path, include
from habits.views import index
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('habits.urls', namespace='habits')),
    path('api/account/', include('users.urls', namespace='users')),
]
