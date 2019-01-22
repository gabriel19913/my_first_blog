# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:27:22 2019

@author: Documentos
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]