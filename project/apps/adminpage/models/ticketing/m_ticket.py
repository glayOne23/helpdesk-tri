from django.db import models, transaction
from django.contrib.auth.models import User

from apps.adminpage.models import TicketCategory, TicketState
    

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(TicketState, on_delete=models.SET_NULL,  blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(TicketCategory, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to='ticketing/attachments', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    __original_state = None

    class Meta:
        ordering    = ['id']

    def __str__(self):        
        return self.title
    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__original_state = self.state


    # @transaction.atomic
    # def save(self, request, *args, **kwargs):
    #     from apps.adminpage.models import TicketStateDetail

    #     if self.state != self.__original_state:
    #         try:                
    #             TicketStateDetail.objects.create(
    #                 ticket = self,
    #                 state = self.state,
    #                 user = request.user
    #             )
    #         except Exception as e:
    #             print(str(e))                

    #     super().save(*args, **kwargs)  # Call the "real" save() method.

    #     self.__original_state = self.state    
