#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2019-10-28
Describe:api path config
"""

from django.urls import path
from sign import views_if, views_if_sec


urlpatterns = [
    # sign system interface
    # ex : api/add_event/
    # path('add_event/',views_if.add_event, name='add_event'),
    path('sec_add_event/',views_if_sec.sec_add_event, name='sec_add_event'),
    # ex : api/add_guest/
    path('add_guest/',views_if.add_guest, name='add_guest'),
    # ex : api/get_event_list/
    # path('get_event_list/', views_if.get_event_list, name='get_event_list'),
    path('get_event_list/', views_if_sec.get_event_list, name='get_event_list'),
    # ex : api/get_guest_list/
    path('sec_get_guest_list/', views_if_sec.get_guest_list, name='get_guest_list'),
    # ex : api/user_sign/
    path('user_sign/', views_if.user_sign, name='user_sign'),
]