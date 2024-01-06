from django import forms
from apps.adminpage.models import Ticket, TicketAnswer, TicketCategory, TicketState, TicketStateDetail
from django.utils.translation import gettext_lazy as _

class TicketCategoryCreateForm(forms.ModelForm):
  class Meta:
    model   = TicketCategory
    fields  = ('name',)
    labels  = {
      'name'        : _('Nama Kategori'),      
    }


class TicketStateCreateForm(forms.ModelForm):
  class Meta:
    model   = TicketState
    fields  = ('code', 'name', 'priority', 'description')
    labels  = {
      'code'        : _('Kode'),
      'name'        : _('Nama'),      
      'priority'    : _('Prioritas'),      
      'description' : _('Deskripsi'),
    }

    
class TicketCreateForm(forms.ModelForm):
  class Meta:
    model   = Ticket
    fields  = ('title', 'category', 'description', 'file')
    labels  = {
      'title'        : _('Judul keluhan'),
      'category'        : _('Kategori'),      
      'description'    : _('Detail keluhan'),      
      'file' : _('File attachment'),
    }    

    # def save(self, commit=True):
    #     instance = super(TicketCreateForm, self).save(commit=False)                
    #     request = getattr(self, 'request', None)

    #     if commit:
    #         instance.save(request=request)

    #     return instance    


class TicketAnswerCreateForm(forms.ModelForm):
  class Meta:
    model   = TicketAnswer
    fields  = ('description', 'file')
    labels  = {
      'description'    : _('Jawaban'),      
      'file' : _('File attachment'),
    }  