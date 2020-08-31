from rest_framework import serializers
from .models import Category, Project, Pledge
from django.utils.timezone import now
from datetime import datetime, timedelta

class ProjectSerialiser(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.id')
    owner = serializers.ReadOnlyField(source='owner.username')
    #owner = serializers.HyperlinkedRelatedField(read_only=True, view_name = 'id', lookup_field='id')
    date_created = serializers.ReadOnlyField()
    is_open = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_is_open(self,obj):
        if obj.pub_date is None:
            return False
        return (obj.pub_date + timedelta(obj.duration)) > now()

class PledgeSerialiser(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')
    #supporter = serializers.StringRelatedField()
    date_sent = serializers.ReadOnlyField()
    
    class Meta:
        model = Pledge
        fields = '__all__'

 
class PledgeUserSerialiser(serializers.ModelSerializer):
    #supporter = serializers.ReadOnlyField(source='supporter.username')
    date_sent = serializers.ReadOnlyField()
    
    class Meta:
        model = Pledge
        fields = '__all__'



class ProjectUserSerialiser(serializers.ModelSerializer):
    #supporter = serializers.ReadOnlyField(source='supporter.username')
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerialiser(ProjectSerialiser):
    project_pledges = PledgeSerialiser(many=True, read_only=True)



#from django.utils.text import slugify

#https://stackoverflow.com/questions/56015369/slug-field-in-django-rest-framework
# class CatSlugSerializer(serializers.ModelSerializer):
#     name_slug = serializers.SerializerMethodField()

#     def get_name_slug(self, instance):
#         return slugify(instance.name)

#     class Meta:
#         model = Category
#         fields = ("name_slug", )



class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'name'}
        # }

"""
data = {
    "name": "delete",
    "description": "testing the shell"
}

new_item = CategorySerialiser(data=data)

if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""

class CategoryDetailSerialiser(CategorySerialiser):
    cat_projects = ProjectSerialiser(many=True, read_only=True)
    

 