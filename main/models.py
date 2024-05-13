from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='home/')


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    user_img = models.ImageField(upload_to='team/')
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    about_project = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    grafik = models.IntegerField()
    start_work = models.DateTimeField(auto_now_add=True)
    end_work = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    requirements = models.TextField()
    tasks = models.TextField()
    texnology = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    resume = models.FileField(upload_to='vacancy/')

    def __str__(self):
        return self.name
