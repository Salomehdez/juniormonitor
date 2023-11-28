#!/usr/bin/env python
import os
import sys

from django.core.servers.basehttp import WSGIRequestHandler

def _header(self):
    return 'Access-Control-Allow-Origin: *'

WSGIRequestHandler.header = _header

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'juniormonitorDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
