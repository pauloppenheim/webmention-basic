#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
:copyright: (c) 2014 by Paul Oppenheim
:license: MIT, see LICENSE for more details.

Trivial listener for
`IndieWeb <http://indiewebcamp.com>`_ `webmentions <http://webmention.org>`_
in python.

  webmention
"""

import sys
import cgi

# must be called "application" to be run by mod_wsgi
def application(environ, start_response):
    #status = '200 OK'
    #headers = [('Content-type', 'text/html; charset=UTF-8')]
    status = '202 Accepted'
    headers = []
    body = ""
    
    source, target = None, None
    form = cgi.FieldStorage(environ=environ, fp=environ["wsgi.input"])
    if form:
        source=form.getfirst("source").strip()
        target=form.getfirst("target").strip()
    if source is None or target is None:
        status = '400 Bad Request'
        headers = [('Content-type', 'text/html; charset=UTF-8')]
        body = "source or target form params missing\n"
    print >> sys.stderr, "%s\t%s" % (source, target)
    
    start_response(status, headers)
    return [body]

# and CGI just runs as a shell executable
def cgi_app():
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(application)

if "__main__" == __name__:
    cgi_app()


