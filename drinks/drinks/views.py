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

@api_view(['GET','PUT','DELETE'])
def person_details(request,id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    