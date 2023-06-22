from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

"""
Authentication and Authorization
Authentication
login -> username/password -> token 
                           -> Incorrect Password

Authorization
username/password
user_instance = get_user_model().objects.get(username=username)
if user_instance.is_active -> token : -> No active user found
SIT University Portal

Student's Portal 

Teacher's Portal 
 -> a student tried to login in teacher portal 
    * user_instance = get_user_model().objects.get(username=username)
    * if user_instance.is_active -> 
    * if user_instance.is_staff -> token : -> No active user found



Custom User Model

Manager -> Class which takes care of create Method

ex : Model.objects.create(**data)

UserModel
id
email
username/phone_number
password        User  Admin   Staff
is_active     = True = True  = True
is_superuser  = False = True = False
is_staff      = False = True  =  True

get_user_model().objects.create(**data)
python manage.py createsuperuser


"""
# from django.contrib.auth.models import User 
# from users.models import UserModel

class CustomUserManager(BaseUserManager):

    def create_superuser(self, email,password, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        print("create superuser")
        print(extra_fields)
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_employee", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_student", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_student(self, email,  username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        print("create_student")
        print(extra_fields)
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_employee", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_student", True)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    


"""
JWT -> Json Web Token 
request users/api/login/
data = {
    "username" : data["username"],
    "password" : data["password"]
}
response -> JWT
this jwt token is used for authentication  

JWT -> Refresh and Access

Access token is the token used for authentication 

Refresh token is used to generate a new access Token

Access token always has less life time then Refresh token so when a access token is
expired we will generate new access token using Refresh token

fb -> Access, Refresh 
1 api -> access, refresh i.e. login
2 api -> takes refresh and return access
"""