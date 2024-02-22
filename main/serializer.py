from rest_framework import serializers
from .models import Teacher,CourseCategory,Course,Student

class TeacherSerializer(serializers.ModelSerializer):
    category=CourseCategorySerializer(many=True)
    course=s=CourseSerializer(many=True)
    class Meta:
        model = Teacher
        fields = '__all__'
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'