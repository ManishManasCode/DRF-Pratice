from django.urls import path 
from .views import StudentDetailModelReadView, SingleStudentDetailModelReadView, StudentDetailModelReadRestAPIView, StudentDetialModelUpdateRestAPIView, StudentDetailModelReadRestGenericAPIView, StudentDetialModelUpdateGenericAPIView, StudentDetailModelListAPIView, StudentDetailModelCreateAPIView, StudentDetailModelListCreateAPIView
# from .views import StudentDetailModelUpdateAPIView
urlpatterns = [
    path("student-details-read/", StudentDetailModelReadView.as_view(), name="StudentDetailModelReadView"),
    path("student-details-read/<id>/", SingleStudentDetailModelReadView.as_view(), name="SingleStudentDetailModelReadView"),
    path("student-details-rest-api/", StudentDetailModelReadRestAPIView.as_view(), name="StudentDetailModelReadRestAPIView"),
    path("student-details-rest-api/<id>/", StudentDetialModelUpdateRestAPIView.as_view(), name="StudentDetialModelUpdateRestAPIView"),
    path("student-details-generic-api/", StudentDetailModelReadRestGenericAPIView.as_view(), name="StudentDetailModelReadRestGenericAPIView"),
    path("student-details-generic-api/<id>/", StudentDetialModelUpdateGenericAPIView.as_view(), name="StudentDetialModelUpdateGenericAPIView"),
    path("student-details-list-api/", StudentDetailModelListAPIView.as_view(), name="StudentDetailModelListAPIView"),
    path("student-details-create-api/", StudentDetailModelCreateAPIView.as_view(), name="StudentDetailModelCreateAPIView"),
    path("student-details-list-create-api/", StudentDetailModelListCreateAPIView.as_view(), name="StudentDetailModelListCreateAPIView"),
    # path("student-details-list-update-api/", StudentDetailModelUpdateAPIView.as_view(), name="StudentDetailModelUpdateAPIView"),

]