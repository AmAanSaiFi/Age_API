from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    path('', views.index, name = 'index'),
    path('result/',views.result,name = 'result'),
    path('viewApi/',views.viewApi.as_view(),name='viewApi'),
]