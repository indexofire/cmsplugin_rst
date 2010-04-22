# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from cmsplugin_rst.models import ReSTField

class ReSTForm(ModelForm):
    class Meta:
        model = ReSTField
        exclude = ('rst_html',)
