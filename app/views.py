from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import employee
from .serializers import emp
from rest_framework import status

@api_view(['GET'])
def info(request):
    return Response("Hello")

@api_view(['POST'])
def create(request):
    serializer = emp(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def get_users(request):
    users = employee.objects.all()
    serializer = emp(users,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user(request,pk):
    empdata = employee.objects.get(id = pk)
    serializer = emp(empdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_user(request,pk):
    empdata = employee.objects.get(id=pk)
    empdata.delete()
    return Response('emp deleted')
