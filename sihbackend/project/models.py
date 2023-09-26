from django.db import models
from account.models import CustomUser

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_file = models.FileField(upload_to='project_files/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    languages_used = models.ManyToManyField(ProgrammingLanguage, blank=True)


    def __str__(self):
        return self.name
