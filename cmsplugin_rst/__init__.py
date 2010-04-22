VERSION = (0,0,1,'alpha', 1)
__version__ = '.'.join(map(str, VERSION))

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version

# patch settings
try:
    from conf import patch_settings
    from django.conf import settings
    patch_settings()
except ImportError:
    """
    This exception means that either the application is being built, or is
    otherwise installed improperly. Both make running patch_settings
    irrelevant.
    """
    pass
except AttributeError:
    """
    Same as Above
    """
    pass

"""
from django.db import models
from django.contrib import admin
from cmsplugin_rst.widgets.markitup_widget import ReSTEditor
from cmsplugin_rst.models import ReSTField
 
class ReSTFieldAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': ReSTEditor},
    }
"""
