django_queryset_decorate
=========================

Allows you to register a decorating function with a Django QuerySet 
that will be executed only when the QuerySet itself has been evaluated.

This allows you to add attributes to individual QuerySet items,
while still benefiting from Django's lazy QuerySet evaluation.

For example:
    
    qs = Item.objects.filter(name__contains = 'e').decorate(lamba item: item.foo = 1)
    
    for item in qs:
        print item, item.foo

Originally inspired by http://github.com/simonw/django-queryset-transform
The difference between django-queryset-transform and this variant,
is that this one operates on single model instances instead of the while list.
It also keeps the iterator pattern intact this way.
