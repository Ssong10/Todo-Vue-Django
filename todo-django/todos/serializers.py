from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','user','is_completed')

class UserSerializers(serializers.ModelSerializer):
    todo_set = TodoSerializers(many=True)
    class Meta:
        model = get_user_model()
        fields = ('id','username','todo_set')