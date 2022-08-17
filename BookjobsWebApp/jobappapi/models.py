from django.db import models

class all_jobs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    creationDate = models.DateTimeField(auto_now = True, blank = False)

    def __str__(self):
        return self.title
