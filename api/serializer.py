from rest_framework import serializers
from .models import Programmer


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        # fields=('fulname',)
        fields = '__all__'
