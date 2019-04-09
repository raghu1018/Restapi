from rest_framework import serializers
class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField()
    esal = serializers.FloatField()
    eaddr = serializers.CharField()

