#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
:copyright: (c) 2014 by Paul Oppenheim
:license: MIT, see LICENSE for more details.

Trivial
`IndieWeb <http://indiewebcamp.com>`_ `webmention <http://webmention.org>`_
receiver in python, wsgi or cgi; echo for webmentions.

"""

import sys
import cgi
try:
    import json
except ImportError:
    import simplejson as json

# must be called "application" to be run by mod_wsgi
def application(environ, start_response):
    #status = '200 OK'
    #headers = [('Content-type', 'text/html; charset=UTF-8')]
    status = '202 Accepted'
    headers = []
    body = ""
    form = cgi.FieldStorage(environ=environ, fp=environ["wsgi.input"])
    err = environ.get("wsgi.errors", sys.stderr)
    
    sentinel = "webmention_recv:"
    source = form.getfirst("source", "").strip()
    target = form.getfirst("target", "").strip()
    remote_host = environ.get("REMOTE_HOST", "")
    
    if source is None or target is None:
        status = '400 Bad Request'
        headers = [('Content-type', 'text/html; charset=UTF-8')]
        body = "source or target form params missing\n"
    result = dict(remote_host=remote_host, source=source, target=target)
    err.write("%s%s\n" % (sentinel, json.dumps(result)))
    
    start_response(status, headers)
    return [body]

# and CGI just runs as a shell executable
def cgi_app():
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(application)

if "__main__" == __name__:
    cgi_app()


