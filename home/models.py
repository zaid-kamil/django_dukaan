from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    