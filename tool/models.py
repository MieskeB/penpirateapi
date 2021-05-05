from django.db import models


# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=200)
    code = models.TextField()
    tool = models.ForeignKey('Tool', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
