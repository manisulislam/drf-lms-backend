from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    address=models.TextField()
    class Meta:
        verbose_name_plural = "1.Teachers"
    def __str__(self):
        return f"Teacher Name-{self.full_name}"

class CourseCategory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural = "2.Course Category"
    def __str__(self):
        return f"course title-{self.title}"

class Course(models.Model):
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE,related_name="category")
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name="teacher")
    title=models.CharField(max_length=100)
    description=models.TextField()

    class Meta:
        verbose_name_plural = "3.Courses"

    def __str__(self):
        return f"{self.title}-give by {self.teacher.full_name}"


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    address=models.TextField()
    interested_categories=models.TextField()

    class Meta:
        verbose_name_plural = "4.Students"
    def __str__(self):
        return f"Student Name-{self.full_name}"