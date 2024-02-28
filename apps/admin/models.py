from django.db import models

#Create your models here

class SiteConfig(models.Model):
    #site configurations

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key
    

#Academic Session
class AcademicSession(models.Model):
    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
    
#Academic Term
class AcademicTerm(models.Model):
    name = models.CharField(max_length = 20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering=["name"]

    def __str__(self):
        return self.name
    
#Subjects
class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering=["name"]

    def __str__(self):
        return self.name
    
#Student class
class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)


    class Meta:
        verbose_name = "class"
        verbose_name_plural = "classes"
        ordering = ["name"]

    def __str__(self):
        return self.name
    