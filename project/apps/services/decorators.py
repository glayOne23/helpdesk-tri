# =========================================
# Created by Ridwan Renaldi, S.Kom. (rr867)
# =========================================
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied


from django.shortcuts import get_object_or_404
from apps.adminpage.models import Ticket, TicketCategory, TicketAnswer, TicketState, TicketStateDetail


def cek_group(user, groups: list):
    if user:
        return user.groups.filter(name__in=groups).count() > 0
    return False


def group_required(*groups):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=[x.strip() for x in groups]).exists() | request.user.is_superuser :
                return function(request, *args, **kwargs)
            else:
                messages.warning(request, 'You Don\'t Have Permission')
                return redirect('authentication:signout')
                
        return wrapper
    return decorator


def isloggedin(url):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(url)
            else:
                return function(request, *args, **kwargs)
                
        return wrapper
    return decorator


def show_ticket():
    def decorator(function):
        def wrapper(request, *args, **kwargs):                        
            ticket = get_object_or_404(Ticket, id=kwargs.get('id'))            
            if ticket.user == request.user or cek_group(request.user, ['bpsdm']):
                return function(request, *args, **kwargs)                                
            else:
                raise PermissionDenied
        return wrapper
    return decorator


def update_ticket():
    def decorator(function):
        def wrapper(request, *args, **kwargs):                        
            ticket = get_object_or_404(Ticket, id=kwargs.get('id'))            
            if (ticket.user == request.user or cek_group(request.user, ['bpsdm'])) and ticket.state == TicketState.get_pending():
                return function(request, *args, **kwargs)                                
            else:
                raise PermissionDenied
        return wrapper
    return decorator