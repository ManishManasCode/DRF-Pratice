from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import views , status, generics
from .serializers import StudentUserRegistrationSerializer
from django.contrib.auth import get_user_model


class StudentUserRegistrationGenericAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = StudentUserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "User Registered"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




"""

Authentication and Authorization 
Authentication
user/login-api/ 
body {
"username" : "jfjf",
"password" : "sjnfdjs"
}
username and password are valid 
token

Authorization 
is_user_active
Permissions 


"""



























data = {
    "name" : "First API",
    "format" : "Json",
    "category" : "http",
    "framework" : "django"
}

# Create your views here.
def dummy_api(request):
    if request.method == "POST":
        pass
    elif request.method == "PUT":
        pass 
    elif request.method == "DELETE":
        pass 
    else:
        return JsonResponse(data)



class DummyRestAPIView(views.APIView):
    # Read
    def get(self, request):
        return Response(data, status=status.HTTP_200_OK)
    # Create
    def post(self, request):
        req_data = request.data
        return Response(req_data, status=status.HTTP_200_OK)
    # Update
    def put(self, request):
        req_data = request.data
        return Response(req_data, status=status.HTTP_200_OK)
    # Delete
    def delete(self, request):
        return Response({"message" : "Id is deleted"})

    
# 200_OK & 400_BAD_REQUEST
    


class DummyRestAPIIDView(views.APIView):

    def get(self, request, id):
        return Response({"id" : id})
