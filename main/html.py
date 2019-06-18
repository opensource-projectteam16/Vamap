import base64
import json
import warnings
from collections import OrderedDict
from uuid import uuid4
from six import binary_type, text_type
from jinja2 import Environment, PackageLoader, Template
from branca.element import CssLink, Element, Figure, JavascriptLink, MacroElement
from folium import Map

import time
import warnings
_default_js = [
    ('leaflet',
     'https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.js'),
    ('jquery',
     'https://code.jquery.com/jquery-1.12.4.min.js'),
    ('bootstrap',
     'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js'),
    ('awesome_markers',
     'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js'),  # noqa
    ]

_default_css = [
    ('leaflet_css',
     'https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.css'),
    ('bootstrap_css',
     'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'),
    ('bootstrap_theme_css',
     'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css'),  # noqa
    ('awesome_markers_font_css',
     'https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css'),  # noqa
    ('awesome_markers_css',
     'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css'),  # noqa
    ('awesome_rotate_css',
     'https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css'),  # noqa
    ]

ENV = Environment(loader=PackageLoader('branca', 'templates'))


class elementover(Map):
    def __init__(self,map):
        super(elementover, self).__init__(location=map.location, zoom_start=map.zoom_start)
    def save(self, outfile, width, height, close_file=True, **kwargs):
        """Saves an Element into a file.

        Parameters
        ----------
        outfile : str or file object
            The file (or filename) where you want to output the html.
        close_file : bool, default True
        Whether the file has to be closed after write.
        """
        self.width=width
        self.height=height
        if isinstance(outfile, text_type) or isinstance(outfile, binary_type):
            fid = open(outfile, 'wb')
        else:
            fid = outfile
        root = self.get_root()
        html = root.render(**kwargs)
        fid.write(html.encode('utf8'))
        if close_file:
            fid.close()

    def render(self, **kwargs):
        """Renders the HTML representation of the element."""
        figure = self.get_root()
        assert isinstance(figure, Figure), ('You cannot render this Element '
                                            'if it is not in a Figure.')

        # Set global switches
        figure.header.add_child(self.global_switches, name='global_switches')

        # Import Javascripts
        for name, url in _default_js:
            figure.header.add_child(JavascriptLink(url), name=name)

        # Import Css
        for name, url in _default_css:
            figure.header.add_child(CssLink(url), name=name)
        widthdata = 'width:'+str(self.width)+'%;\n'
        heightdata = 'height:'+str(self.height)+'%;\n'
        bodydata = '<style>html, body {\n'+widthdata + heightdata + \
            'margin: 0;\n' + 'padding: 0;\n' + '}\n'+'</style>\n'
        print (bodydata)
        figure.header.add_child(Element(
            bodydata
        ), name='css_style')

        figure.header.add_child(Element(
            '<style>#map {'
            'position:absolute;'
            'top:0;'
            'bottom:0;'
            'right:0;'
            'left:0;'
            '}'
            '</style>'), name='map_style')        
        
        super(Map, self).render(**kwargs)
