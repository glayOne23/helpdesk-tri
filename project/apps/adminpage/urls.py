from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.adminpage.views import (
    services,
    profile,
    account,
    dashboard,
    category,
    ticketing
)

app_name = 'adminpage'

urlpatterns = [
  path('dashboard',                             login_required(dashboard.index),            name='dashboard'),
  path('service/setprofilesync',                login_required(services.setprofilesync),    name='setprofilesync'),
  path('profile',                               login_required(profile.index),              name='profile'),


  path('account/', include([
      # =================================================[ LOAD PAGE ]=================================================
      path('table',                             login_required(account.table),              name='account_table'),
      path('role',                              login_required(account.role),               name='account_role'),
      path('add',                               login_required(account.add),                name='account_add'),        
      path('edit/<int:id>',                     login_required(account.edit),               name='account_edit'),
      path('edit_group/<int:id>',               login_required(account.edit_group),         name='account_edit_group'),
      
      # ==================================================[ SERVICE ]==================================================
      path('delrole/<int:userid>/<int:groupid>',login_required(account.delrole),            name='account_delrole'),
      path('deletelist',                        login_required(account.deletelist),         name='account_deletelist'),
      path('setisactive/<str:mode>',            login_required(account.setisactive),        name='account_setisactive'),
  ])), 


  path('category/', include([
      # =================================================[ LOAD PAGE ]=================================================
      path('table',                             login_required(category.table),             name='category_table'),
      path('add',                               login_required(category.add),               name='category_add'),
      path('edit/<int:id>',                     login_required(category.edit),              name='category_edit'),

      # ==================================================[ SERVICE ]==================================================
      path('deletelist',                        login_required(category.deletelist),        name='category_deletelist'),
  ])),    


path('setting/', include([
    path('tiket/', include([        
        path('kategori/table',                            login_required(ticketing.category_table),             name='setting.ticketing.category.table'),
        path('kategori/add',                              login_required(ticketing.category_add),               name='setting.ticketing.category.add'),
        path('kategori/<int:id>/edit',                    login_required(ticketing.category_edit),              name='setting.ticketing.category.edit'),
        path('kategori/deletelist',                       login_required(ticketing.category_deletelist),        name='setting.ticketing.category.deletelist'),

        path('tahap/table',                             login_required(ticketing.state_table),             name='setting.ticketing.state.table'),
        path('tahap/add',                              login_required(ticketing.state_add),               name='setting.ticketing.state.add'),
        path('tahap/<int:id>/edit',                    login_required(ticketing.state_edit),              name='setting.ticketing.state.edit'),
        path('tahap/deletelist',                       login_required(ticketing.state_deletelist),        name='setting.ticketing.state.deletelist'),        
    ])),    
])),

path('tiket/', include([      
    path('table',                             login_required(ticketing.user_ajuan_table),             name='ticketing.user.ajuan.table'),
    path('user_ajuan_json',                   login_required(ticketing.user_ajuan_json),             name='ticketing.user.ajuan.json'),
    path('add',                               login_required(ticketing.user_ajuan_add),               name='ticketing.user.ajuan.add'),
    path('<int:id>/edit/',                    login_required(ticketing.user_ajuan_edit),              name='ticketing.user.ajuan.edit'),      
    path('<int:id>/show/',                    login_required(ticketing.user_ajuan_show),              name='ticketing.user.ajuan.show'),      
    path('<int:id>/delete/',                  login_required(ticketing.user_ajuan_delete),        name='ticketing.user.ajuan.delete'),

    path('bpsdm/table',                        login_required(ticketing.bpsdm_ajuan_table),             name='ticketing.bpsdm.ajuan.table'),
    path('bpsdm/ajuan_json',                   login_required(ticketing.bpsdm_ajuan_json),             name='ticketing.bpsdm.ajuan.json'),
    path('<int:id>/bpsdm/show/',                    login_required(ticketing.bpsdm_ajuan_show),              name='ticketing.bpsdm.ajuan.show'),      
    path('<int:id>/bpsdm/edit_state',          login_required(ticketing.bpsdm_edit_state),             name='ticketing.bpsdm.ajuan.edit_state'),
  ])),    
]