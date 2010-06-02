# -*- coding: utf-8 -*-
from os.path import join

from django.conf import settings
from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from cms.plugins.text import settings as text_settings
from django.utils.translation.trans_real import get_language


class MarkItUpWidget(Textarea):
    """MarkItUp Widget class
    
    """
    class Media:
        js = (
            'markitup/jquery.markitup.pack.js',
            'markitup/sets/restructuredtext/set.js',
        )
        css = {
            'all': (
                'markitup/sets/restructuredtext/style.css',
                'markitup/skins/simple/style.css',
            )
        }

    def __init__(self, attrs=None):
        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
        super(Textarea, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<textarea id="markItUp" name="rst"%s>%s</textarea>' % 
            (flatatt(final_attrs), conditional_escape(force_unicode(value))))

class AdminMarkItUpWidget(MarkItUpWidget, AdminTextareaWidget):
    """Add vLargeTextarea class to MarkItUpWidget so it looks more
    similar to other admin textareas.

    """
    pass
