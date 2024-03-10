from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST','PUT'])
def person_list(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    