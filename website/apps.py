import sys
from copy import copy as copy_object
from django.apps import AppConfig


def _patch_template_context_copy_for_python_314():
    """
    Django 4.2's BaseContext.__copy__ uses copy(super()), which breaks on
    Python 3.14+ because super() objects became copyable (see Django #35844).
    Mirror the fix from Django 5.2+ so inclusion tags and {% include ... with %}
    do not crash when the request context is copied.
    """
    from django.template.context import BaseContext

    def __copy__(self):
        duplicate = BaseContext()
        duplicate.__class__ = self.__class__
        duplicate.__dict__ = copy_object(self.__dict__)
        duplicate.dicts = self.dicts[:]
        return duplicate

    BaseContext.__copy__ = __copy__


class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'

    def ready(self):
        if sys.version_info >= (3, 14):
            _patch_template_context_copy_for_python_314()
