from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_staged/', views.get_staged_name),
    path('set_staged/', views.set_staged_name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]