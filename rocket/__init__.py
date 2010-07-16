#!/usr/bin/env python

__doc__ = """rocket - implementing api's with a quickness

For more information, see: http://github.com/extensionfm/rocket

Rocket has one external dependency: simplejson

To install simplejson:

    pip install simpljson

Or http://undefined.org/python/#simplejson
"""

__all__ = [ 'rocket' ]

from rocket import Rocket, json, generate_proxies
