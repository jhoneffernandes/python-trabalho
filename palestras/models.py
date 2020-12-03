from django.db import models

# Create your models here.
class Palestra(models.Model):
    title = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    datetimeStart = models.DateTimeField()
    datetitmeEnd = models.DateTimeField()
    
    def __str__(self):
        return self.title



class Ouvinte(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Inscricao(models.Model):
    palestrafk = models.ForeignKey(Palestra, on_delete=models.CASCADE)
    ouvintefk = models.ForeignKey(Ouvinte, on_delete=models.CASCADE)
