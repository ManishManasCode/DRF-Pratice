from django.urls import path 
from .views import dummy_api, DummyRestAPIView, DummyRestAPIIDView, StudentUserRegistrationGenericAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("student-register-api/", StudentUserRegistrationGenericAPIView.as_view(), name="StudentUserRegistrationGenericAPIView"),
    path("dummy-api/", dummy_api, name="dummy_api"),
    path("dummy-rest-api/", DummyRestAPIView.as_view(), name="dummy_rest_api"),
    path("dummy-rest-api/<id>/", DummyRestAPIIDView.as_view(), name="dummy_rest_api"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
