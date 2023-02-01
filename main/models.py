from django.db import models


class Aluno(models.Model):

    nome= models.CharField(max_length=255)
    telefone = models.IntegerField()
    email = models.EmailField()
    data_nascimanteo = models.DateField(null=True)
    descriptions = models.TextField()




    def __str__(self):
        return self.name

# Create your models here.
