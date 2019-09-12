from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

DEPARTMENTS = (("MBA", "Management"),
               ("MCA", "PG"),
               ("BTech","Bachelors"),
               ("MTech", "Masters"))

BRANCHES = (("ECE", "Electronics"),
            ("EEE", "Electrical"),
            ("CSE", "Computers"),
            ("CSIT", "Information Tech"),
            ("Civil", "Civil Engg"),
            )

GENDER = (("M", "Male"),
          ("F", "Female"))


class DjUser(AbstractUser):

    #user = models.OneToOneField(User)

    department = models.CharField(max_length=20, choices=DEPARTMENTS, default="BTech")
    branch = models.CharField(max_length=20, choices=BRANCHES, default="CSE")
    gender = models.CharField(max_length=10, choices=GENDER)
    rollno = models.CharField(max_length=20)
    doj = models.DateField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_num = models.CharField(max_length=15)
    address = models.TextField(max_length=255, blank=True)


class Book(models.Model):

    book_user = models.ForeignKey(DjUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    edition = models.CharField(max_length=5)
    publisher = models.CharField(max_length=20)
    issue_date = models.DateField()

    def __str__(self):
        return self.name