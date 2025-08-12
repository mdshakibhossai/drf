from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id','username','first_name', 'last_name')

class CourseSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    total_courses =serializers.SerializerMethodField()
    def get_total_courses(self,obj):
        return Enrollcourse.objects.filter(student=obj).count()
    class Meta :
        model = Student
        fields = '__all__'
        depth = 1


class StudentDetailSerializer(serializers.ModelSerializer):
    enrolled_coruses = serializers.SerializerMethodField()
    def get_enrolled_coruses(self,obj):
        course_ids = Enrollcourse.objects.filter(student=obj).values_list('course_id', flat = True)
        courses = Course.objects.filter(id__in=course_ids)
        serializer = CourseSerialzer(courses, many=True)
        return serializer.data

    created_by = UserSerializer()
    class Meta :
        model = Student
        fields = '__all__'
        depth = 1