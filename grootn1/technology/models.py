from django.db import models

# Model for AI Technologies
class AIModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name

# Model for Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f"Message from {self.name}"

    
