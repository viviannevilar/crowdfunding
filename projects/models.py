from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length = 15, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"



class Project(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True) 
    duration = models.IntegerField()
    pub_date =  models.DateTimeField(null=True,blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'owner_projects',
    )
    category = models.ForeignKey(
        Category, 
        on_delete = models.SET_DEFAULT,
        default='Other',
        related_name = 'cat_projects'
    )

    # You can override the save method on your model to check and update the field before saving.
    # def save(self, *args, **kwargs):
    #     if self.pledge >= self.target
    #     self.complete=True
    #     return super().save(*args, **kwargs)

    #https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield



class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_sent = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='project_pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )