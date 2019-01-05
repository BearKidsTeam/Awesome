#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.getenv("CI") is not None:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.test")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
