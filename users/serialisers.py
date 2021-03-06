# users/serializers.py
from rest_framework import serializers 
from django.contrib.auth import get_user_model
from projects.serialisers import (
    PledgeSerialiser,
    PledgeUserSerialiser,
    ProjectUserSerialiser)

User = get_user_model()

class CustomUserSerialiser(serializers.ModelSerializer):
    """
    'views.UserList'
    'views.UserCreate'
    'views.UserRetrieveUpdateDestroy'
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        lookup_field = 'username'

        # Write only field
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}


    def create(self, validated_data):
        """ ensures the password is created correctly, otherwise won't be able to login with user created, and in admin get the error "Invalid password format or unknown hashing algorithm."
        """
        user = super(CustomUserSerialiser, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerialiser(serializers.ModelSerializer):
    """ 
    This is so the user can create a profile, add information such as bio, pic, etc 
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'pic', 'bio', 'first_name','last_name')
        lookup_field = 'username'

        read_only_fields = ('username',)


class UserDisplaySerialiser(serializers.ModelSerializer):
    """ 
    'views.UserProfile': when request user IS NOT owner of account 
    """
    owner_projects = ProjectUserSerialiser(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'date_joined', 'last_login', 'owner_projects', 'bio', 'first_name', 'last_name', 'pic'] 


class UserProfileSerialiser(serializers.ModelSerializer):
    """ 
    'views.UserProfile': when request user IS owner of account 
    """ 
    supporter_pledges = PledgeUserSerialiser(many=True, read_only=True)
    owner_projects = ProjectUserSerialiser(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'date_joined', 'last_login', 'owner_projects', 'supporter_pledges', 'bio', 'email', 'first_name', 'last_name', 'pic']
