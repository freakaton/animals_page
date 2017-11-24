from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.name + 's'

    def my_animals(self):
        animals = self.animal_set.all()
        return animals
    

class Animal(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=500, blank=True)
    type = models.ForeignKey('Type',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(null=True)