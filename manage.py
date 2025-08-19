#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import types

# Temporary fix for removed cgi module in Python 3.13
if sys.version_info >= (3, 13):
    sys.modules['cgi'] = types.ModuleType("cgi")
    sys.modules['cgi'].FieldStorage = object


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taxi_Booking.settings')
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
