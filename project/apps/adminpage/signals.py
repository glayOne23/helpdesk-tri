from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.adminpage.models import Ticket, TicketAnswer, TicketCategory, TicketState, TicketStateDetail

# @receiver(post_save, sender=Ticket)
# def ticketstate_created(sender, instance, created, **kwargs):
#     if created:            
#         TicketStateDetail.objects.create()