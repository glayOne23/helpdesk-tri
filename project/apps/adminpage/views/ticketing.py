import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.db.models import Count, Sum


from apps.services.decorators import group_required, update_ticket, show_ticket
from apps.adminpage.models import Ticket, TicketCategory, TicketAnswer, TicketState, TicketStateDetail
from apps.adminpage.forms.ticketing import TicketCategoryCreateForm, TicketStateCreateForm, TicketCreateForm

from json import dumps



# **********************************************************
#                           SETTING
# **********************************************************
@group_required('admin', 'bpsdm')
def category_table(request):
    context = {}
    # ===[Load a CSS And JS File]===
    context['datatables']       = True
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

    # ===[Fetch Data]===
    context['dataticketcategory']     = TicketCategory.objects.all()

    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/category/table.html', context)



@group_required('admin', 'bpsdm')
def category_add(request):
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

    # ===[Load Form]===
    context['formcategoryticket']     = TicketCategoryCreateForm(request.POST or None, request.FILES or None)


    # ===[Insert Logic]===
    if request.POST:
        if context['formcategoryticket'].is_valid():
            context['formcategoryticket'].save()
            messages.success(request, 'Data Added Successfully', extra_tags=dumps({
                'redirect'      : reverse('adminpage:setting.ticketing.category.table'), 
                'confbtntxt'    : 'Check Data',
                'cnclbtntxt'    : 'Cancel',
            }))
            return redirect('adminpage:setting.ticketing.category.add')
        else:
            messages.error(request, context['formcategoryticket'].errors)
    
    
    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/category/add.html', context)    



@group_required('admin', 'bpsdm')
def category_edit(request, id):
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

    # ===[Check ID IsValid]===
    try:
        getcategoryticket = TicketCategory.objects.get(id=id)
    except TicketCategory.DoesNotExist:
        messages.error(request, 'Data Tidak Ditemukan!')
        return redirect('adminpage:setting.ticketing.category.table')


    # ===[Load Form]===
    context['formcategoryticket']     = TicketCategoryCreateForm(request.POST or None, instance=getcategoryticket)


    # ===[Edit Logic]===
    if request.POST:
        if context['formcategoryticket'].is_valid():
            context['formcategoryticket'].save()

            messages.success(request, 'Data Berhasil Dirubah', extra_tags=dumps({
                'redirect'      : reverse('adminpage:setting.ticketing.category.table'), 
                'confbtntxt'    : 'Check Data',
                'cnclbtntxt'    : 'Cancel',
            }))
            return redirect('adminpage:setting.ticketing.category.edit', id=id)
        else:
            messages.error(request, context['formcategoryticket'].errors)


    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/category/add.html', context)    



@group_required('admin', 'bpsdm')
def category_deletelist(request):
    if request.POST and request.POST.getlist('list_id'):
        list_id = request.POST.getlist('list_id')
        
        try:
            with transaction.atomic():
                for id in list_id:
                    TicketCategory.objects.get(id=id).delete()
                messages.success(request, 'Data Berhasil Dihapus')

        except TicketCategory.DoesNotExist:
            messages.error(request, 'There is an error')
    else:
        messages.error(request, 'Invalid request!')

    # ===[Redirect]===
    return redirect('adminpage:setting.ticketing.category.table')




@group_required('admin', 'bpsdm')
def state_table(request):
    context = {}
    # ===[Load a CSS And JS File]===
    context['datatables']       = True
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

    # ===[Fetch Data]===
    context['dataticketstate']     = TicketState.objects.all()

    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/state/table.html', context)



@group_required('admin', 'bpsdm')
def state_add(request):
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

    # ===[Load Form]===
    context['formstateticket']     = TicketStateCreateForm(request.POST or None, request.FILES or None)


    # ===[Insert Logic]===
    if request.POST:
        if context['formstateticket'].is_valid():
            context['formstateticket'].save()
            messages.success(request, 'Data Added Successfully', extra_tags=dumps({
                'redirect'      : reverse('adminpage:setting.ticketing.state.table'), 
                'confbtntxt'    : 'Check Data',
                'cnclbtntxt'    : 'Cancel',
            }))
            return redirect('adminpage:setting.ticketing.state.add')
        else:
            messages.error(request, context['formstateticket'].errors)
    
    
    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/state/add.html', context)    



@group_required('admin', 'bpsdm')
def state_edit(request, id):
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

    # ===[Check ID IsValid]===
    try:
        getstateticket = TicketState.objects.get(id=id)
    except TicketState.DoesNotExist:
        messages.error(request, 'Data Tidak Ditemukan!')
        return redirect('adminpage:setting.ticketing.state.table')


    # ===[Load Form]===
    context['formstateticket']     = TicketStateCreateForm(request.POST or None, instance=getstateticket)


    # ===[Edit Logic]===
    if request.POST:
        if context['formstateticket'].is_valid():
            context['formstateticket'].save()

            messages.success(request, 'Data Berhasil Dirubah', extra_tags=dumps({
                'redirect'      : reverse('adminpage:setting.ticketing.state.table'), 
                'confbtntxt'    : 'Check Data',
                'cnclbtntxt'    : 'Cancel',
            }))
            return redirect('adminpage:setting.ticketing.state.edit', id=id)
        else:
            messages.error(request, context['formstateticket'].errors)


    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/state/add.html', context)    



@group_required('admin', 'bpsdm')
def state_deletelist(request):
    if request.POST and request.POST.getlist('list_id'):
        list_id = request.POST.getlist('list_id')
        
        try:
            with transaction.atomic():
                for id in list_id:
                    TicketState.objects.get(id=id).delete()
                messages.success(request, 'Data Berhasil Dihapus')

        except TicketState.DoesNotExist:
            messages.error(request, 'There is an error')
    else:
        messages.error(request, 'Invalid request!')

    # ===[Redirect]===
    return redirect('adminpage:setting.ticketing.state.table')



# **********************************************************
#                         AJUAN
# **********************************************************
@login_required()
def user_ajuan_table(request):
    context = {}
    # ===[Load a CSS And JS File]===
    context['datatables']       = True
    context['tinydatepicker']   = False
    context['datetimepicker']   = False
    context['select2']          = True
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
    
    # tahun
    distinct_years = Ticket.objects.dates('created_at', 'year')
    years_list = [date.year for date in distinct_years]
    context['datatahun'] = reversed(years_list)
    context['tahun_terpilih'] = datetime.datetime.now().year    

    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/user/ajuan/table.html', context)


@login_required()
@transaction.atomic
def user_ajuan_add(request):
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

    # ===[Load Form]===
    context['formticket']     = TicketCreateForm(request.POST or None, request.FILES or None)


    # ===[Insert Logic]===
    if request.POST:
        if context['formticket'].is_valid():
            # basic
            ticket = context['formticket'].save(commit=False)
            ticket.user = request.user
            ticket.state = TicketState.get_pending()
            ticket.save()            
            # set ticket state detail ketika pertama kali buat ticket atau ketika state berubah
            TicketStateDetail.objects.create(ticket=ticket, state=ticket.state, user=request.user)

            messages.success(request, 'Tiket berhasil diajukan')
            return redirect('adminpage:ticketing.user.ajuan.table')
        else:
            messages.error(request, context['formticket'].errors)
    
    
    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/user/ajuan/add.html', context)


@login_required()
def user_ajuan_json(request):    
    queryset = Ticket.objects.filter(user=request.user)
    if request.POST and request.POST.get('tahun'):
        queryset = queryset.filter(created_at__year=request.POST.get('tahun'))
        data = queryset.values('id', 'user', 'user__username', 'state', 'state__code', 'state__name', 'title', 'description', 'category', 'category__name', 'file', 'created_at', 'updated_at')        
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse([], safe=False)
    


@login_required()
@show_ticket()
def user_ajuan_show(request, id):
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

    # ===[Check ID IsValid]===
    try:
        getticket = Ticket.objects.get(id=id)
        context['dataticket'] = getticket
    except Ticket.DoesNotExist:
        messages.error(request, 'Data Tidak Ditemukan!')
        return redirect('adminpage:ticketing.user.ajuan.table')    
    
    context['dataticketstatedetail'] = TicketStateDetail.objects.filter(ticket=getticket)

    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/user/ajuan/show.html', context)    


@login_required()
@update_ticket()
def user_ajuan_edit(request, id):
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

    # ===[Check ID IsValid]===
    try:
        getticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        messages.error(request, 'Data Tidak Ditemukan!')
        return redirect('adminpage:ticketing.user.ajuan.table')


    # ===[Load Form]===
    context['formticket']     = TicketCreateForm(request.POST or None, request.FILES or None, instance=getticket)


    # ===[Edit Logic]===
    if request.POST:
        if context['formticket'].is_valid():
            context['formticket'].save()

            messages.success(request, 'Tiket Berhasil Dirubah')
            return redirect('adminpage:ticketing.user.ajuan.table')
        else:
            messages.error(request, context['formticket'].errors)


    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/user/ajuan/add.html', context)


@login_required()
@update_ticket()
def user_ajuan_delete(request, id):    
    try:
        Ticket.objects.get(id=id).delete()
        messages.success(request, 'Data Berhasil Dihapus')
    except Ticket.DoesNotExist:
        messages.error(request, 'There is an error')    

    # ===[Redirect]===
    return redirect('adminpage:ticketing.user.ajuan.table')



# **********************************************************
#                   BPSDM - AJUAN
# **********************************************************
@login_required()
@group_required('admin', 'bpsdm')
def bpsdm_ajuan_table(request):
    context = {}
    # ===[Load a CSS And JS File]===
    context['datatables']       = True
    context['tinydatepicker']   = False
    context['datetimepicker']   = False
    context['select2']          = True
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

    # ===[Fetch Data]===    
    # status    
    context['dataticketstate'] = TicketState.objects.annotate(total_tickets=Count('ticket'))    
    context['state'] = request.GET.get('state')    
    # tahun
    distinct_years = Ticket.objects.dates('created_at', 'year')
    years_list = [date.year for date in distinct_years]
    context['datatahun'] = reversed(years_list)
    context['tahun_terpilih'] = datetime.datetime.now().year    

    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/admin/ajuan/table.html', context)


@login_required()
@group_required('admin', 'bpsdm')
def bpsdm_ajuan_json(request):    
    queryset = Ticket.objects.all()
    if request.POST:
        if request.POST.get('state'):
            queryset = queryset.filter(state__code=request.POST.get('state'))
        if request.POST.get('tahun'):
            queryset = queryset.filter(created_at__year=request.POST.get('tahun'))
        data = queryset.values('id', 'user', 'user__username', 'ticketstatedetail__user__username', 'state', 'state__code', 'state__name', 'title', 'description', 'category', 'category__name', 'file', 'created_at', 'updated_at')        
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse([], safe=False)
    

@login_required()
@show_ticket()
def bpsdm_ajuan_show(request, id):
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

    # ===[Check ID IsValid]===
    try:
        getticket = Ticket.objects.get(id=id)
        context['dataticket'] = getticket
    except Ticket.DoesNotExist:
        messages.error(request, 'Data Tidak Ditemukan!')
        url = reverse('adminpage:ticketing.bpsdm.ajuan.table') + '?state=pending'
        return redirect(url)
    
    context['dataticketstatedetail'] = TicketStateDetail.objects.filter(ticket=getticket)

    # ===[Render Template]===
    return render(request, 'adminpage/ticketing/admin/ajuan/show.html', context)    
    

@login_required()
@group_required('admin', 'bpsdm')
def bpsdm_edit_state(request, id):
    # ===[Check ID IsValid]===
    try:
        getticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        messages.error(request, 'Data Tidak Ditemukan!')
        url = reverse('adminpage:ticketing.bpsdm.ajuan.table') + '?state=pending'
        return redirect(url)
            
    getticket.state = TicketState.get_in_process()
    getticket.save()            
    # set ticket state detail ketika pertama kali buat ticket atau ketika state berubah
    TicketStateDetail.objects.create(ticket=getticket, state=getticket.state, user=request.user)
    
    return redirect('adminpage:ticketing.bpsdm.ajuan.show', id=id)
    
