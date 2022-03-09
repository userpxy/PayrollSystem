from django.urls import path
from . import views


urlpatterns = [
    #path('login_for_medal/', views.login_for_medal, name='login_for_medal'),
    path('login/', views.login, name='login'),
    path('userappend/', views.userappend, name='userappend'),
    path('user_normal_select/', views.user_normal_select, name='user_normal_select'),
    path('logout/', views.logout, name='logout'),
    path('user_info/', views.user_info, name='user_info'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_select/', views.user_select, name='user_select'),
    # path('attendence_list/<int:user_pk>', views.attendence_list, name='attendence_list'),
    # path('attendence_lists/', views.attendence_lists, name='attendence_lists'),
    path('position_lists/', views.position_lists, name='position_lists'),
    path('staff_type_modify/<int:position_pk>', views.staff_type_modify, name='staff_type_modify'),
    path('staff_type_add/', views.staff_type_add, name='staff_type_add'),
    path('staff_type_delete/<int:position_pk>', views.staff_type_delete, name='staff_type_delete'),
    path('salary_list/<int:user_pk>', views.salary_list, name='salary_list'),
    path('salary_lists/', views.salary_lists, name='salary_lists'),
    path('caculate_salary/', views.caculate_salary, name='caculate_salary'),
    path('salary_normal_select/', views.salary_normal_select, name='salary_normal_select'),
    path('salary_select/', views.salary_select, name='salary_select'),
    #path('change_nickname/', views.change_nickname, name='change_nickname'),
    #path('bind_email/', views.bind_email, name='bind_email'),
    #path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('change_password/', views.change_password, name='change_password'),
    #path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('user_delete/<int:user_pk>', views.user_delete, name='user_delete'),
    path('user_modify/<int:user_pk>', views.usermodify, name='user_modify'),
    # path('attendence_append/', views.attendence_append, name='attendence_append'),
    # path('attendence_select/', views.attendence_select, name='attendence_select'),
    # path('attendence_delete/<int:attendence_pk>', views.attendence_delete, name='attendence_delete'),
    # path('attendence_modify/<int:attendence_pk>', views.attendence_modify, name='attendence_modify'),
    path('sel_pay_m', views.sel_pay_m, name='sel_pay_m'),
]