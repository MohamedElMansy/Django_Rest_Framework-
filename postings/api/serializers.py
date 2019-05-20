from rest_framework import serializers
from postings.models import BlogPost
from rest_auth.models import TokenModel
from rest_auth.serializers import UserDetailsSerializer

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model =BlogPost
        fields= '__all__'

        read_only_fields=['user']

class TokenSerializer(serializers.ModelSerializer):
   
    user = UserDetailsSerializer(many=False, read_only=True)  # this is add by myself.
    class Meta:
        model = TokenModel
        fields = ('key', 'user')