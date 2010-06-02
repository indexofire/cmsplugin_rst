# -*- coding: utf-8 -*-
from django.conf import settings
from django.forms.widgets import Media
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_rst.models import ReSTField
from cmsplugin_rst.forms import ReSTForm


class ReSTPlugin(CMSPluginBase):
    model = ReSTField
    name = _('ReST')
    form = ReSTForm
    render_template = 'cmsplugin_rst/rst.html'
    change_form_template = "cmsplugin_rst/text_plugin_change_form.html"

    def render(self, context, instance, placeholder):
        context.update({'object': instance, 'placeholder': placeholder})
        return context

    #class PluginMedia:
    #    css = {'all': ('media/cmsplugin_rst.css',)}
    
    def get_plugin_media(self, request, context, plugin):
        return Media(css = {'all': ('cmsplugin_rst/css/cmsplugin_rst.css',),})

plugin_pool.register_plugin(ReSTPlugin)
