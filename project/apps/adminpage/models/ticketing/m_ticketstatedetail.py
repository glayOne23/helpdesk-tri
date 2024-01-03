from django.db import models
from django.contrib.auth.models import User
from apps.adminpage.models import Ticket, TicketState

    
class TicketStateDetail(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)    
    state = models.ForeignKey(TicketState, on_delete=models.CASCADE)    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):        
        return self.name