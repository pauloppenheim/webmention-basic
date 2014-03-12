
webmention-basic
================

Trivial
`IndieWeb <http://indiewebcamp.com>`_ `webmention <http://webmention.org>`_
receiver in python, wsgi or cgi; echo for webmentions.


What does it do?
================

Simply receives mentions and logs calls to stderr, does not implement any
fetching, parsing, or other verification.
No examination of the path is done; assuming that is managed outside of the app.
If you want that, check out
`Dainin <https://github.com/bear/dainin>`_ or
`Ronkyuu <https://github.com/bear/ronkyuu>`_.



Why would you want this?
========================

The IndieWeb is about leaving social networking sites and using our own websites
again. However, aside from someone sending an email, there's not an easy way to
get a notification of a reply, like, repost, private message, or any of the
other notifications a social networking site might give you.

WebMentions can be that messaging glue, for normal websites. There are older
protocols (Traceback, Pingback) but this is the one that people use now.
Interacting with WebMentions requires having a webmentions endpoint on your site.

I thought to myself "what is the simplest possible thing that could work?" and
unix pipes and syslog came to mind. This takes a webmention and outputs it onto
stderr, which means the webmention will probably get put into your site's
error.log, where you can grep for it. For example

.. code:: bash

	pauloppenheim@host:~$ grep "webmention:" ~/logs/pauloppenheim.com/http/error.log 
	[Sat Mar 08 19:41:49 2014] [error] [client 50.184.87.59] webmention:http://localhost/a\thttp://localhost/b
	[Sat Mar 08 19:42:23 2014] [error] [client 50.184.87.59] webmention:http://localhost/a\thttp://localhost/b

etc.

The format might change, but the simplicity is still there. Now you have your
mentions stored somewhere, and you can use other unix tools to do something
with them. Because this is such a simple script, you could also write a wrapper
script that logs to another file, or directly starts to add the mention on a
post, or even send a text message. Your handler can be decoupled from
receiving the message.



Why return JSON? Isn't that too complex for a UNIX program?
===========================================================

First there was a simple key-value format. Then my next thought was,
"how do I parse this?" The answer to that question should be reasonable,
more like ``sed`` or ``grep``, not ``awk`` or ``perl``.
I didn't want to emit several lines per webmention to facilitate simple
key-value parsing. So the result is something like:

.. code:: bash

	cat msg.log | sed 's/.*webmention_recv:\(.*\)/\1/' | python -m json.tool

which sadly isn't entirely simple, but does facilitate a unix pipeline style.

There are several JSON programs for handling the final step, such as
`jshon <http://kmkeen.com/jshon/>`_



Install
=======

Simple!

CGI
---

Copy the ``webmention_basic.py`` script to your cgi-bin dir, possibly also
changing the file extension to ``.cgi``, depending on your web server configuration.


WSGI
----

Copy the ``webmention_basic.py`` script to your wsgi path, possibly also
changing the file extension to ``.wsgi``, depending on your web server configuration.



Run from shell
==============

Since ``__main__`` runs as a CGI script, you can run this from the command line.
To see how it handles the example from the webmentions example, try this

.. code:: bash

	(export REQUEST_METHOD=POST ; export REQUEST_URI="/" ; echo -e \
	"source=http://bob.host/post-by-bob&target=http://alice.host/post-by-alice"\
	| python webmention_basic.py )

or even

.. code:: bash

	python webmention_basic.py

to see how it runs with no params or environment.



Roadmap
=======

.. role:: strike

* :strike:`get working`
* more testing



Contributors
============

* `Paul Oppenheim <http://pauloppenheim.com>`_



Requires
========
Python v2.5+ and possibly earlier. `requirements.txt`_ is currently empty.



