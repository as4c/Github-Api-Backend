from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    avatar = models.URLField()
    location = models.CharField(max_length=255)
    bio = models.TextField()
    twitter = models.CharField(max_length=255, blank=True)

# class Repository(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     languages = models.CharField(max_length=255)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Profile(models.Model):
#     image_url=models.CharField(max_length=100,blank=True,null=True) #avatar_url
#     username=models.CharField(max_length=100) #name
#     bio=models.CharField(max_length=500)
#     location=models.CharField(max_length=50)
#     social_media_url = models.CharField(max_length=100)
#     github_url = models.CharField(max_length=100)
#     follower=models.IntegerField()
#     following=models.IntegerField()
#     def __str__(self):
#         return self.username

# class Repositories(models.Model):
#     username= models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
#     repo_name = models.CharField(max_length=100)
#     discription=models.CharField(max_length=500)
#     language=models.CharField(max_length=20)
#     created_at = models.CharField(max_length=50)
#     updated_at=models.CharField(max_length=50)
#     pushed_at=models.CharField(max_length=50)
#     stars=models.IntegerField()
#     watchers=models.IntegerField()
#     repo_url=models.CharField(max_length=100)
#     issues=models.IntegerField()

#     def __str__(self):
#         return self.repo_name