from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile #model to be serialized
        fields = ('id','email','name','password') #fields to be serialized
        extra_kwargs = {
            'password':{
                'write_only':True, #password is write only
                'style':{'input_type':'password'} #password input type is password
            }
        }
    
    def create(self,validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'], #get email from validated_data
            name = validated_data['name'], #get name from validated_data
            password = validated_data['password'] #get password from validated_data
        )
        return user
    
    def update(self,instance,validated_data):
        """Handle updating user account"""
        if 'password' in validated_data: #if password is in validated_data
            password = validated_data.pop('password') #get password from validated_data
            instance.set_password(password) #set password
        return super().update(instance,validated_data) #return instance

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem #model to be serialized
        fields = ('id','user_profile','status_text','created_on') #fields to be serialized
        extra_kwargs = {'user_profile':{'read_only':True}} #user_profile is read only