from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    mail = serializers.EmailField()
    phone = serializers.CharField(max_length=12)
    dept = serializers.CharField(max_length=50)
    job = serializers.CharField(max_length=50)
    doj = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.job=validated_data.get('job',instance.job)
        instance.phone  = validated_data.get('phone',instance.phone)
        instance.dept = validated_data.get('dept',instance.dept)
        instance.doj = validated_data.get('doj',instance.doj)
        instance.save()
        return instance