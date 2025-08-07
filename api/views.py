from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def hello(request):
    data = {
        "name":"Shakib",
        "age":20
    }
    return Response(data, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detaila':'student has been create succesfully'}, status=status.HTTP_200_OK)
        return Response(
            {'errors':serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )