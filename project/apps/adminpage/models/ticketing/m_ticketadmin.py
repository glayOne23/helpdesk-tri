from django.db import models
from django.contrib.auth.models import User
from apps.adminpage.models import Ticket, TicketCategory


    
class TicketAdmin(models.Model):
    ticketcategory = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticketadmin_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):        
        return f"{self.ticketcategory.name} - {self.user.username}"