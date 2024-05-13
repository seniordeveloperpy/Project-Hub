from main.models import *
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['name', 'phone']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['name', 'phone', 'start_work', 'end_work', 'salary']