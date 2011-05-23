from django.db import models
from django.db.models.query import QuerySet


class DecoratingQuerySet(QuerySet):
    def __init__(self, *args, **kwargs):
        super(DecoratingQuerySet, self).__init__(*args, **kwargs)
        self._decorate_funcs = []

    def _clone(self, klass=None, setup=False, **kw):
        c = super(DecoratingQuerySet, self)._clone(klass, setup, **kw)
        c._decorate_funcs = self._decorate_funcs[:]
        return c

    def decorate(self, fn):
        if fn not in self._decorate_funcs:
            self._decorate_funcs.append(fn)
        return self

    def iterator(self):
        base_iterator = super(DecoratingQuerySet, self).iterator()
        for obj in base_iterator:
            # Apply the decorators
            for fn in self._decorate_funcs:
                fn(obj)

            yield obj


class DecoratorManager(models.Manager):
    def get_query_set(self):
        return DecoratingQuerySet(self.model)
