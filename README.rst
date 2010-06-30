This is a plugin of django-cms-2.0 for add restructured text to your articles. 

It's based on *BSD License*, so please share it as what you want.

Requirement:
----------------------------

It supports pygment code highlight. You need to install pygment first

Install:
----------------------------

1. copy `media/cmsplugin_rst` and `media/markitup` folders to your media folder
2. add `cmsplugin_rst` into INSTALLED_APP of your settings
3. run ./manage.py syncdb

Usage:
-----------------------------

::

  .. code:: python
     :linenos:

     import os, path
     from django.conf import settings

     class MyNewCode(object):
         pass

ps: if you don't like the line numbers, just get rid of `:linenos:`. from \

version 0.0.2 alaph, editor support prompt a dialog to input your code. So you 

don't need to write `.. code:: python` every time.

If you want to custom style, change `cmsplugin_rst.css` to fit for your site.
