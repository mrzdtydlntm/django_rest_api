from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
# router.register('login', views.UserLoginApiView, basename='login')
#first parameter is name of API we want to call
#second parameter is name of viewset that we want to assign to this router

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('login/',views.UserLoginApiView.as_view())
]