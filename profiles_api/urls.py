from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter() #create a router object
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset') #register HelloViewSet with router
router.register('profile',views.UserProfileViewSet) #register UserProfileViewSet with router
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls)) #include router urls in urlpatterns
]