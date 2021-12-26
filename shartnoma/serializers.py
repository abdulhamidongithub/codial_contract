from rest_framework.serializers import ModelSerializer
from .models import *


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class UstozSerializer(ModelSerializer):
    class Meta:
        model = Ustoz
        fields = "__all__"

class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = "__all__"

class ShartnomaSerializer(ModelSerializer):
    ustoz = UstozSerializer()
    kurs = KursSerializer()
    student = StudentSerializer()
    class Meta:
        model = Shartnoma
        fields = "__all__"

