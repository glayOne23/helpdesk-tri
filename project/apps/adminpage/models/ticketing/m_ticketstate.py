from django.db import models

    
class TicketState(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    priority = models.SmallIntegerField(default=1, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):        
        return self.name
    
    @staticmethod
    def get_pending():
        return TicketState.objects.get(code='pending')