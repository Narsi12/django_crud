import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import employee
from .serializers import emp
from rest_framework import status

# Set up logging
logger = logging.getLogger(__name__)

#sample api
@api_view(['GET'])
def infouser(request):
    logger.info('Get the all users !! ')
    return Response("Hello")

#post api
@api_view(['POST'])
def create(request):
    logger.info('create endpoint hit with data: %s', request.data)
    serializer = emp(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info('New employee created: %s', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        logger.error('Error in create: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    logger.info('get the all users')
    users = employee.objects.all()
    serializer = emp(users, many=True)
    logger.info('Retrieved users: %d', len(users))
    return Response(serializer.data)

@api_view(['PUT'])
def update_user(request, pk):
    logger.info('update_user endpoint hit for ID: %s', pk)
    try:
        empdata = employee.objects.get(id=pk)
    except employee.DoesNotExist:
        logger.error('Employee with ID %s not found', pk)
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = emp(empdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info('Employee with ID %s updated', pk)
        return Response(serializer.data)
    else:
        logger.error('Error in update_user for ID %s: %s', pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete method
@api_view(['DELETE'])
def delete_user(request, pk):
    logger.info('delete_user endpoint hit for ID: %s', pk)
    try:
        empdata = employee.objects.get(id=pk)
        empdata.delete()
        logger.info('Employee with ID %s deleted', pk)
        return Response({'message': 'Employee deleted'}, status=status.HTTP_204_NO_CONTENT)
    except employee.DoesNotExist:
        logger.error('Employee with ID %s not found for deletion', pk)
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
