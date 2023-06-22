from django.db import models

# Create your models here.
# model is meant by a table 
"""
Father Name -> Char 
Father Number -> Char -> +91 9876543210
Mother Name -> Char
Mother Number -> Char 
Student Number -> Char
Gmail -> email 
"""

class StudentContactDetailModel(models.Model):
    father_name = models.CharField(max_length=100)
    father_number = models.CharField(max_length=15)
    mother_name = models.CharField(max_length=100)
    mother_number = models.CharField(max_length=15)
    student_number = models.CharField(max_length=15)
    gmail = models.EmailField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True) 

"""
Name -> char
Rollno -> Int
Dob -> DateField
Branch -> char
year_of_joining -> DateField
"""

class AddressDetailModel(models.Model):
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True) 

class PrevEducationModel(models.Model):
    university = models.CharField(max_length=100) # abc
    degree = models.CharField(max_length=100) # cse
    percentage = models.IntegerField() # 90
    address = models.ForeignKey(AddressDetailModel, on_delete=models.CASCADE, related_name="prev_education_address", null=True) # 1

    created_at = models.DateTimeField(auto_now_add=True)

"lookup operator->lookup fields to compare betweens relations"
class StudentDetailModel(models.Model):
    name          =  models.CharField(max_length=100)
    roll_no       =  models.IntegerField(unique=True)
    date_of_birth =  models.DateField()
    branch        =  models.CharField(max_length=100)
    year_of_joining = models.DateField()
    # obj of studentDetailModel will have connection only for once with any instane of obj StudentContactModel
    # StudentDetailMoldeobj1 -> StudentContactDetailModelobj1
    # StudentDetailMoldeobj2 can't create a relation again with StudentContactDetailModelobj1
    # we are saving list of id 
    prev_education = models.ManyToManyField(PrevEducationModel, related_name="student_prev_education_field", blank=True)
    # # saving id of parent or child class 
    contact_info = models.OneToOneField(
        StudentContactDetailModel, on_delete=models.CASCADE, 
        related_name="student_detail_contact_info", null=True, 
        blank=True) 
    
    
    # # obj of studentDetailModel will have connection only for once with any instane of obj StudentContactModel
    # # StudentDetailMoldelobj1 -> AddressDetailModelobj1
    # # StudentDetailMoldelobj2 -> AddressDetailModelobj1
    # # One to Many
    # # Many to One
    # # saving id of parent or child class
    address = models.ForeignKey(AddressDetailModel,
                                on_delete=models.CASCADE, 
                                related_name="student_detail_address", 
                                null=True, blank=True) 

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    


class StudentPrevEducationModel(models.Model):
    student = models.ForeignKey(StudentDetailModel, on_delete=models.CASCADE, related_name="student_prev_education")
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    percentage = models.IntegerField()
    address = models.ForeignKey(AddressDetailModel, on_delete=models.CASCADE, related_name="student_prev_education_address", null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # obj1 obj2 obj3 -> student1


    # john obj1 -> schooling obj1
    #           -> intermediate obj2

