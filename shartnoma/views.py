from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from shartnoma.models import Student
from .serializers import *

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ["ism", "id", "familiya", "jins", "tel1", "tel2"]
    ordering_fields = ["id", "jins","ism",]
class UstozViewSet(ModelViewSet):
    queryset = Ustoz.objects.all()
    serializer_class = UstozSerializer

class KursViewSet(ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class ShartnomaViewSet(ModelViewSet):
    queryset = Shartnoma.objects.all()
    serializer_class = ShartnomaSerializer





