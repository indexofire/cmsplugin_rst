# -*- coding: utf-8 -*-
from operator import not_

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from pygments import highlight
from pygments.util import ClassNotFound
from pygments.lexers import get_lexer_by_name, guess_lexer, TextLexer
from pygments.formatters import HtmlFormatter


class CodeHighlight(Directive) :
    """ReStructured Text Highlight Code Directive
    
    Usage:
    .. code:: python
       :linenos:

       from django.conf import settings

       class MyCode():
           def MyFunction():
           ...
    """
    
    # define directive options
    require_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'linenos' : not_,
        'style' : directives.unchanged,
        'noclasses' : not_,
    }
    
    # define default options
    defaults = {
        'linenos' : False,
        'style' : 'default',
        'noclasses' : False,
    }

    controller = None
    has_content = True

    def run(self) :
        text = u'\n'.join(self.content)

        try :
            # Use the corresponding lexer, if a language was specified.
            lexer = get_lexer_by_name(self.arguments[0])
        except IndexError :
            try :
                # No language was specified, so take an educated guess.
                lexer = guess_lexer(text)
            except ClassNotFound :
                # That didn't work either, use a standard TextLexer; no
                # highlighting.
                lexer = TextLexer()

        # Get current state from controller, supplied options.
        overrides = {}
        # overrides.update(self.controller.state)
        overrides.update(self.options)
        highlighted_text = highlight(text, lexer, HtmlFormatter(**overrides))
        return [nodes.raw('', highlighted_text, format = 'html')]
