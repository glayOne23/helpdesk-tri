from django.db import models
from django.contrib.auth.models import User
from apps.adminpage.models import Ticket


    
class TicketAnswer(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    ticket_answer = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    file = models.FileField(upload_to='ticketing/answers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):        
        return self.description[:20]