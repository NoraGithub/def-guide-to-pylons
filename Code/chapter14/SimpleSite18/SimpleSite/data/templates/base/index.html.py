from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1225714207.058404
_template_filename='/media/disk/Pylons Book/Code/chapter08/SimpleSite12/SimpleSite/simplesite/templates/base/index.html'
_template_uri='/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'flash', 'title', 'tabs', 'menu', 'footer', 'header', 'breadcrumbs', 'heading']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n"http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n    <title>')
        # SOURCE LINE 7
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 8
        __M_writer(escape(self.head()))
        __M_writer(u'\n</head>\n<body>\n    ')
        # SOURCE LINE 11
        __M_writer(escape(self.header()))
        __M_writer(u'\n    ')
        # SOURCE LINE 12
        __M_writer(escape(self.tabs()))
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(escape(self.menu()))
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(escape(self.heading()))
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(escape(self.breadcrumbs()))
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(escape(self.flash()))
        __M_writer(u'\n    ')
        # SOURCE LINE 17
        __M_writer(escape(next.body()))
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(escape(self.footer()))
        __M_writer(u'\n</body>\n</html>\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n    ')
        # SOURCE LINE 24
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/main.css'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flash(context):
    context.caller_stack._push_frame()
    try:
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        if session.has_key('flash'):
            # SOURCE LINE 34
            __M_writer(u'    <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\n    ')
            # SOURCE LINE 35

            del session['flash']
            session.save()
                
            
            # SOURCE LINE 38
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'SimpleSite')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'<p><a href="#top">Top ^</a></p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'<a name="top"></a>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'<h1>')
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()

