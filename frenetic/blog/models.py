from django.db import models


class Profile(models.Model):
    email = models.CharField(max_length=150)
    bio = models.CharField(max_length=4000)
    phonenum = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class User(models.Model):
    username =  models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField('Date Created')
    edited_date = models.DateTimeField('Edited Date')

    def __str__(self):
        return self.username

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signature = models.CharField(max_length=100)
    
    def __str__(self):
        return self.signature


class CommentAuthor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('Published Date')
    edited_date = models.DateTimeField('Edited Date')
    authors = models.ManyToManyField( Author )

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.CharField(max_length=500)
    timeDate = models.DateTimeField('Comment Date')
    author = models.ForeignKey(CommentAuthor, on_delete=models.CASCADE)
