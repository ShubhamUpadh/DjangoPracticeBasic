from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length=100, blank = True)
    last_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    