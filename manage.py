#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
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

# todo: BURAYA DİKKAT !!! ÖNCE OKU   !!!

"""Eğer bu projeyi başka bir bilgisayarda ve PyCharm'da açmışsan. Setting>Proje:dindefterimsitesi>Python Interpreter> [bölümünden projeye ayiy 
ne kadar paket varsa kur. Bukadar.] """

"""Eğer bu projeyi başka bir bilgisayarda ve PyCharm'da açmışsan <Edit Run Configuration:dindefterimsitesi> menüsünü bul ve
<Environment variables> kısmından <DJANGO_SETTINGS_MODULE> bolümünün karşısındaki hücreye <config.settings.development> yaz. BİTTİ"""
# development
# production
