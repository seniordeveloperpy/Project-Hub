from . import serializers
from main import models

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def home(request):
    data = models.Home.objects.all()
    serializer = serializers.HomeSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def portfolio(request):
    data = models.Portfolio.objects.all()
    serializer = serializers.PortfolioSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team(request):
    data = models.Team.objects.all()
    serializer = serializers.TeamSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def message_create(request):
    if request.method == 'POST':
        serializer = serializers.MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def vacancy(request):
    data = models.Vacancy.objects.all()
    serializer = serializers.VacancySerializer(data, many=True)
    return Response(serializer.data)




