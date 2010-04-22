# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.utils.encoding import smart_str, force_unicode

from cms.models import CMSPlugin
from cmsplugin_rst.directives.code import CodeHighlight

class ReSTField(CMSPlugin):
    rst = models.TextField(_('Body'))
    rst_html = models.TextField(editable=False, blank=True)

    def __unicode__(self):
        return u'%s' %(truncate_words(strip_tags(self.rst_html), 3)[:30]+'...')

    def save(self, *args, **kwargs):
        self.rst_html = self.parse(self.rst)
        return super(ReSTField, self).save(*args, **kwargs)

    def parse(self, value):
        try:
            from docutils.core import publish_parts
            from docutils.parsers.rst import directives, Directive
        except ImportError:
            if settings.DEBUG:
                raise template.TemplateSyntaxError("Error in {% restructuredtext %} filter: The Python docutils library isn't installed.")
            return force_unicode(value)
        else:
            docutils_settings = getattr(settings, 'RESTRUCTUREDTEXT_FILTER_SETTINGS', {},)
            directives.register_directive('code', CodeHighlight)
            parts = publish_parts(source=smart_str(value),
                                  writer_name="html4css1",
                                  settings_overrides=docutils_settings,
                                  )
            return force_unicode(parts["body"])
