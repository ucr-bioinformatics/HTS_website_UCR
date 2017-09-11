from rest_framework import serializers
from management.models import Project


class ProjectSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    title = serializers.CharField()
    date = serializers.DateField()
    time = serializers.TimeField()
    status = serializers.CharField()
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=15)
    pi = serializers.CharField(max_length=100)
    billing_account = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.status = validated_data.get('status', instance.status)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.pi = validated_data.get('pi', instance.pi)
        instance.billing_account = validated_data.get('billing_account', instance.billing_account)
        instance.department = validated_data.get('department', instance.department)
        instance.save()
        return instance
