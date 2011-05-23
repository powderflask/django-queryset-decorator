django_queryset_decorator
=========================

Allows you to register a decorating function with a Django QuerySet 
that will be executed only when the QuerySet itself has been evaluated.

This allows you to add attributes to individual QuerySet items,
while still benefiting from Django's lazy QuerySet evaluation.

For example:

    qs = Item.objects.all().decorate(lamba item: item.is_active = (item.status == 'A'))
    
    for item in qs:
        print item, item.is_active

This is particulary useful when the QuerySet is passed to a template,
or in case there is data in the view which you don't want to pass to the model layer.
Instead of having to pass that data, you can attach a lambda expression that does the
relevant work for you once the upper layer is requesting the QuerySet results.

Originally inspired by http://github.com/simonw/django-queryset-transform
The difference between django-queryset-transform and this variant,
is that this one operates on single model instances instead of the while list.
It also keeps the iterator pattern intact this way.
