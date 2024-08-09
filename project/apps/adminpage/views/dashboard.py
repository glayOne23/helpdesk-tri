import json

from django.shortcuts import render
from django.db.models import Count, Prefetch



from apps.adminpage.models import Ticket, TicketAdmin, TicketCategory, TicketState




# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================

def index(request):
    context = {}
    # ===[Load a CSS And JS File]===
    context['datatables']       = False
    context['tinydatepicker']   = False
    context['datetimepicker']   = False
    context['select2']          = False
    context['chosen']           = False
    context['dropzone']         = False
    context['summernote']       = False
    context['fullcalendar']     = False
    context['photoswipe']       = False
    context['maxlength']        = False
    context['inputmask']        = False
    context['moment']           = False
    context['duallistbox']      = False
    context['daterange']        = False
    context['countdown']        = False
    context['chart']            = True


    # Example Notification
    # extra_tags is optional, used in the notif function located in -> (apps\adminpage\templates\adminpage\layout\javascript.html)

    if request.user.groups.filter(name__in=['admin']).exists() or request.user.is_superuser:
        dataticket = Ticket.objects.all()
    elif request.user.groups.filter(name__in=['bpsdm']).exists():
        ticketcategories = TicketAdmin.objects.filter(user=request.user).values('ticketcategory')
        dataticket = Ticket.objects.filter(category__in=ticketcategories)
    else:
        dataticket = Ticket.objects.filter(user=request.user)

    context['totalticket'] = dataticket.count()
    context['stateticket'] = (
        TicketState.objects
        .prefetch_related(Prefetch('ticket_set', queryset=dataticket))
        .annotate(ticket_count=Count('ticket'))
        .values('name', 'ticket_count')
    )
    context['stateticket'] = json.dumps(list(context['stateticket']))

    # ===[Render Template]===
    return render(request, 'adminpage/index.html', context)
